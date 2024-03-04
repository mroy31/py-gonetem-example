#!/usr/bin/env python3

import argparse
import logging
import sys
import random
import grpc
import tempfile
import os
import tarfile
import signal
import time
from yaspin import yaspin
from google.protobuf import empty_pb2
from proto import netem_pb2
import proto.netem_pb2_grpc as netem_grpc

PRJ_OPEN_NAME = "constellation"
RUNNING = True

def generate_topology(node_count: int, launch_count: int) -> str:
    nodes_idx = list(range(0, node_count))
    launch_idx = random.choices(nodes_idx, k=launch_count)

    nodes = ""
    links = ""
    for idx in nodes_idx:
        launch = idx in launch_idx and "true" or "false"
        nodes += f"  sat{idx}:\n    type: docker.router\n    launch: {launch}\n"
        links += f"- peer1: ground.{idx}\n  peer2: sat{idx}.0\n"

    return f"""
nodes:
  ground:
    type: docker.server
{nodes}
links:
{links}
"""

def generate_project(node_count: int, launch_count: int, dest_dir: str) -> str:
    os.chdir(dest_dir)
    with open("network.yml", "w") as fd:
        fd.write(generate_topology(node_count, launch_count))    
    
    with tarfile.open("project.gnet", "w:gz") as tar:
        tar.add("network.yml")
    
    return os.path.join(dest_dir, "project.gnet")


def open_project(prj: str, client: netem_grpc.NetemStub) -> str:
    logging.info(f"open project {prj}")
    with open(prj, "b+r") as fd:
        request = netem_pb2.OpenRequest()
        request.name = PRJ_OPEN_NAME
        request.data = fd.read()

        res = client.OpenProject(request)
        return res.id


EVENTS = [
    {
        "step": 10,
        "action": "node_restart",
        "node": "sat1"
    },
    {
        "step": 20,
        "action": "link_update",
        "peer1": "ground.1",
        "peer2": "sat1.0",
        "delay": 100,
        "jitter": 10,
        "loss": 0,
    },
]


def run_event(client: netem_grpc.NetemStub, prjId: str, step: int) -> None:
    for evt in EVENTS:
        if evt["step"] == step:
            if evt["action"] == "node_restart":
                logging.info(f"STEP {step} - restart node {evt["node"]}")
                request = netem_pb2.NodeRequest()
                request.prjId = prjId
                request.node = evt["node"]

                try:
                    client.Restart(request)
                except Exception as err:
                    logging.error(f"Unable to restart node {evt["node"]}: {err}")

            elif evt["action"] == "link_update":
                logging.info(f"STEP {step} - update link {evt["peer1"]}--{evt["peer2"]}")
                request = netem_pb2.LinkRequest()
                request.prjId = prjId
                request.link.peer1 = evt["peer1"]
                request.link.peer2 = evt["peer2"]
                request.link.delay = evt["delay"]
                request.link.jitter = evt["jitter"]
                request.link.loss = evt["loss"]

                try:
                    client.LinkUpdate(request)
                except Exception as err:
                    logging.error(f"Unable to update link {evt["peer1"]}--{evt["peer2"]}: {err}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Python Gonetem client to generate/run/modify large network')
    parser.add_argument(
        "-n", "--nodes", type=int, dest="nodes",
        metavar="NODES", default=10,
        help="Number of nodes in the network (default: 10)")
    parser.add_argument(
        "-l", "--launch", type=int, dest="launch",
        metavar="NUMBER", default=1,
        help="Number of nodes started when the network is launched (default: 1)")
    parser.add_argument(
        "-s", "--server", type=str, dest="server",
        metavar="URI", default="localhost:10110",
        help="Server URI (default: localhost:10110)")
    parser.add_argument(
        "-e", "--end", type=int, dest="end",
        metavar="SECONDS", default=60,
        help="Duration in seconds of project launch (0 for infinity, 60 by default)")
    args = parser.parse_args()

    log_format = '%(levelname)s: %(message)s'
    logging.basicConfig(format=log_format, level=logging.INFO)

    if args.launch > args.nodes:
        logging.error("Launch arg is greater than nodes arg")
        sys.exit(1)

    def sig_handler(_signum, _frame):
        global RUNNING
        RUNNING = False
    
    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)

    logging.info(f"Try to connect to gonetem server {args.server}...")
    with grpc.insecure_channel(args.server) as channel:
        client = netem_grpc.NetemStub(channel)
        try:
            version = client.GetVersion(empty_pb2.Empty()).version
            logging.info(f"Connected to server version {version}")
        except Exception as ex:
            logging.error(f"Unable to connect to server {args.server}: {str(ex)}")
            sys.exit(1)

        with tempfile.TemporaryDirectory(prefix="py-gonetem") as dir:
            prj = generate_project(args.nodes, args.launch, dir)

            try:
                prjId = open_project(prj, client)
            except Exception as err:
                logging.error(f"Unable to open project {prj}: {err}")
                sys.exit(1)
            
            request = netem_pb2.ProjectRequest()
            request.id = prjId
            try:
                with yaspin(text="Project launch: Wait ..."):
                    client.Run(request)
            except Exception as err:
                logging.error(f"Unable to run the project: {err}")
                client.CloseProject(request)
                sys.exit(1)
            logging.info("The project is running")
            
            step = 0
            while RUNNING and step < args.end or step == 0:
                run_event(client, prjId, step)
                time.sleep(1.0)
                step += 1

            logging.info("Close the project")
            client.CloseProject(request)

            




