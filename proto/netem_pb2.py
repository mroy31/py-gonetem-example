# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/netem.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11proto/netem.proto\x12\x05netem\x1a\x1bgoogle/protobuf/empty.proto\"\x90\x01\n\x07\x43opyMsg\x12!\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x13.netem.CopyMsg.Code\x12\r\n\x05prjId\x18\x02 \x01(\t\x12\x0c\n\x04node\x18\x03 \x01(\t\x12\x10\n\x08nodePath\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\x0c\"%\n\x04\x43ode\x12\x08\n\x04INIT\x10\x00\x12\x08\n\x04\x44\x41TA\x10\x01\x12\t\n\x05\x45RROR\x10\x03\"\xca\x01\n\rConsoleCltMsg\x12\'\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x19.netem.ConsoleCltMsg.Code\x12\r\n\x05prjId\x18\x02 \x01(\t\x12\x0c\n\x04node\x18\x03 \x01(\t\x12\r\n\x05shell\x18\x04 \x01(\x08\x12\x10\n\x08ttyWidth\x18\x05 \x01(\x05\x12\x11\n\tttyHeight\x18\x06 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x07 \x01(\x0c\"1\n\x04\x43ode\x12\x08\n\x04INIT\x10\x00\x12\x08\n\x04\x44\x41TA\x10\x01\x12\n\n\x06RESIZE\x10\x02\x12\t\n\x05\x43LOSE\x10\x03\"|\n\rConsoleSrvMsg\x12\'\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x19.netem.ConsoleSrvMsg.Code\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"4\n\x04\x43ode\x12\n\n\x06STDOUT\x10\x00\x12\n\n\x06STDERR\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\t\n\x05\x43LOSE\x10\x03\"v\n\nPullSrvMsg\x12$\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x16.netem.PullSrvMsg.Code\x12\r\n\x05image\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\"$\n\x04\x43ode\x12\t\n\x05START\x10\x00\x12\x06\n\x02OK\x10\x01\x12\t\n\x05\x45RROR\x10\x02\"y\n\rCaptureSrvMsg\x12\'\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x19.netem.CaptureSrvMsg.Code\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"1\n\x04\x43ode\x12\n\n\x06STDOUT\x10\x00\x12\n\n\x06STDERR\x10\x01\x12\x06\n\x02OK\x10\x02\x12\t\n\x05\x45RROR\x10\x03\"\xe4\x02\n\x0eTopologyRunMsg\x12(\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x1a.netem.TopologyRunMsg.Code\x12\r\n\x05total\x18\x02 \x01(\x05\x12\x38\n\x0cnodeMessages\x18\x03 \x03(\x0b\x32\".netem.TopologyRunMsg.NodeMessages\x1a.\n\x0cNodeMessages\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08messages\x18\x02 \x03(\t\"\xae\x01\n\x04\x43ode\x12\x0e\n\nNODE_COUNT\x10\x00\x12\x10\n\x0c\x42RIDGE_COUNT\x10\x01\x12\x0e\n\nLINK_COUNT\x10\x02\x12\x0e\n\nNODE_START\x10\x03\x12\x0e\n\nLINK_SETUP\x10\x04\x12\x10\n\x0c\x42RIDGE_START\x10\x05\x12\x13\n\x0fNODE_LOADCONFIG\x10\x06\x12\x11\n\rNODE_MESSAGES\x10\x07\x12\r\n\tNODE_STOP\x10\x08\x12\x0b\n\x07NODE_RM\x10\t\"\x88\x01\n\x0eProjectSaveMsg\x12(\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x1a.netem.ProjectSaveMsg.Code\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\r\n\x05total\x18\x03 \x01(\x05\"/\n\x04\x43ode\x12\x0e\n\nNODE_COUNT\x10\x00\x12\r\n\tNODE_SAVE\x10\x01\x12\x08\n\x04\x44\x41TA\x10\x02\"\x97\x01\n\x0fProjectCloseMsg\x12)\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x1b.netem.ProjectCloseMsg.Code\x12\r\n\x05total\x18\x02 \x01(\x05\"J\n\x04\x43ode\x12\x0e\n\nNODE_COUNT\x10\x00\x12\x10\n\x0c\x42RIDGE_COUNT\x10\x01\x12\x0e\n\nNODE_CLOSE\x10\x02\x12\x10\n\x0c\x42RIDGE_CLOSE\x10\x03\"W\n\nLinkConfig\x12\r\n\x05peer1\x18\x01 \x01(\t\x12\r\n\x05peer2\x18\x02 \x01(\t\x12\x0c\n\x04loss\x18\x03 \x01(\x02\x12\r\n\x05\x64\x65lay\x18\x04 \x01(\x05\x12\x0e\n\x06jitter\x18\x05 \x01(\x05\"=\n\x0bLinkRequest\x12\r\n\x05prjId\x18\x01 \x01(\t\x12\x1f\n\x04link\x18\x02 \x01(\x0b\x32\x11.netem.LinkConfig\"a\n\x12NodeIfStateRequest\x12\r\n\x05prjId\x18\x01 \x01(\t\x12\x0c\n\x04node\x18\x02 \x01(\t\x12\x0f\n\x07ifIndex\x18\x03 \x01(\x05\x12\x1d\n\x05state\x18\x04 \x01(\x0e\x32\x0e.netem.IfState\"D\n\x14NodeInterfaceRequest\x12\r\n\x05prjId\x18\x01 \x01(\t\x12\x0c\n\x04node\x18\x02 \x01(\t\x12\x0f\n\x07ifIndex\x18\x03 \x01(\x05\"*\n\x0bNodeRequest\x12\r\n\x05prjId\x18\x01 \x01(\t\x12\x0c\n\x04node\x18\x02 \x01(\t\"\x1c\n\x0eProjectRequest\x12\n\n\x02id\x18\x01 \x01(\t\"+\n\x0fWNetworkRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\")\n\x0bOpenRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"8\n\x06Status\x12\x1f\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x11.netem.StatusCode\x12\r\n\x05\x65rror\x18\x02 \x01(\t\",\n\x0b\x41\x63kResponse\x12\x1d\n\x06status\x18\x01 \x01(\x0b\x32\r.netem.Status\";\n\x0c\x46ileResponse\x12\x1d\n\x06status\x18\x01 \x01(\x0b\x32\r.netem.Status\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"A\n\x0fVersionResponse\x12\x1d\n\x06status\x18\x01 \x01(\x0b\x32\r.netem.Status\x12\x0f\n\x07version\x18\x02 \x01(\t\"\xb5\x02\n\x0eStatusResponse\x12\x1d\n\x06status\x18\x01 \x01(\x0b\x32\r.netem.Status\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0e\n\x06openAt\x18\x04 \x01(\t\x12\x0f\n\x07running\x18\x05 \x01(\x08\x12/\n\x05nodes\x18\n \x03(\x0b\x32 .netem.StatusResponse.NodeStatus\x1a\x37\n\x08IfStatus\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1d\n\x05state\x18\x02 \x01(\x0e\x32\x0e.netem.IfState\x1a_\n\nNodeStatus\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07running\x18\x02 \x01(\x08\x12\x32\n\ninterfaces\x18\n \x03(\x0b\x32\x1e.netem.StatusResponse.IfStatus\"\xeb\x01\n\x13\x43onfigFilesResponse\x12\x1d\n\x06status\x18\x01 \x01(\x0b\x32\r.netem.Status\x12\x31\n\x06source\x18\x02 \x01(\x0e\x32!.netem.ConfigFilesResponse.Source\x12\x34\n\x05\x66iles\x18\x03 \x03(\x0b\x32%.netem.ConfigFilesResponse.ConfigFile\x1a(\n\nConfigFile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\"\n\x06Source\x12\x0b\n\x07\x41RCHIVE\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\"\x91\x01\n\x0fPrjListResponse\x12\x1d\n\x06status\x18\x01 \x01(\x0b\x32\r.netem.Status\x12-\n\x08projects\x18\x02 \x03(\x0b\x32\x1b.netem.PrjListResponse.Info\x1a\x30\n\x04Info\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06openAt\x18\x03 \x01(\t\"<\n\x0fPrjOpenResponse\x12\x1d\n\x06status\x18\x01 \x01(\x0b\x32\r.netem.Status\x12\n\n\x02id\x18\x02 \x01(\t*\x1f\n\nStatusCode\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01*\x1b\n\x07IfState\x12\x06\n\x02UP\x10\x00\x12\x08\n\x04\x44OWN\x10\x01\x32\xc8\r\n\x05Netem\x12\x44\n\x10ServerGetVersion\x12\x16.google.protobuf.Empty\x1a\x16.netem.VersionResponse\"\x00\x12\x41\n\x10ServerPullImages\x12\x16.google.protobuf.Empty\x1a\x11.netem.PullSrvMsg\"\x00\x30\x01\x12\x45\n\x15ServerCleanContainers\x12\x16.google.protobuf.Empty\x1a\x12.netem.AckResponse\"\x00\x12\x42\n\x0eProjectGetMany\x12\x16.google.protobuf.Empty\x1a\x16.netem.PrjListResponse\"\x00\x12;\n\x0bProjectOpen\x12\x12.netem.OpenRequest\x1a\x16.netem.PrjOpenResponse\"\x00\x12\x41\n\x0cProjectClose\x12\x15.netem.ProjectRequest\x1a\x16.netem.ProjectCloseMsg\"\x00\x30\x01\x12?\n\x0bProjectSave\x12\x15.netem.ProjectRequest\x1a\x15.netem.ProjectSaveMsg\"\x00\x30\x01\x12\x45\n\x15ProjectGetNodeConfigs\x12\x15.netem.ProjectRequest\x1a\x13.netem.FileResponse\"\x00\x12\x42\n\x10ProjectGetStatus\x12\x15.netem.ProjectRequest\x1a\x15.netem.StatusResponse\"\x00\x12?\n\x0fReadNetworkFile\x12\x15.netem.ProjectRequest\x1a\x13.netem.FileResponse\"\x00\x12@\n\x10WriteNetworkFile\x12\x16.netem.WNetworkRequest\x1a\x12.netem.AckResponse\"\x00\x12<\n\rTopologyCheck\x12\x15.netem.ProjectRequest\x1a\x12.netem.AckResponse\"\x00\x12\x42\n\x0eTopologyReload\x12\x15.netem.ProjectRequest\x1a\x15.netem.TopologyRunMsg\"\x00\x30\x01\x12?\n\x0bTopologyRun\x12\x15.netem.ProjectRequest\x1a\x15.netem.TopologyRunMsg\"\x00\x30\x01\x12?\n\x10TopologyStartAll\x12\x15.netem.ProjectRequest\x1a\x12.netem.AckResponse\"\x00\x12>\n\x0fTopologyStopAll\x12\x15.netem.ProjectRequest\x1a\x12.netem.AckResponse\"\x00\x12G\n\x13NodeReadConfigFiles\x12\x12.netem.NodeRequest\x1a\x1a.netem.ConfigFilesResponse\"\x00\x12=\n\x11NodeCanRunConsole\x12\x12.netem.NodeRequest\x1a\x12.netem.AckResponse\"\x00\x12?\n\x0bNodeConsole\x12\x14.netem.ConsoleCltMsg\x1a\x14.netem.ConsoleSrvMsg\"\x00(\x01\x30\x01\x12\x35\n\tNodeStart\x12\x12.netem.NodeRequest\x1a\x12.netem.AckResponse\"\x00\x12\x34\n\x08NodeStop\x12\x12.netem.NodeRequest\x1a\x12.netem.AckResponse\"\x00\x12\x37\n\x0bNodeRestart\x12\x12.netem.NodeRequest\x1a\x12.netem.AckResponse\"\x00\x12\x41\n\x0eNodeSetIfState\x12\x19.netem.NodeIfStateRequest\x1a\x12.netem.AckResponse\"\x00\x12\x44\n\x0bNodeCapture\x12\x1b.netem.NodeInterfaceRequest\x1a\x14.netem.CaptureSrvMsg\"\x00\x30\x01\x12\x32\n\x0cNodeCopyFrom\x12\x0e.netem.CopyMsg\x1a\x0e.netem.CopyMsg\"\x00\x30\x01\x12\x34\n\nNodeCopyTo\x12\x0e.netem.CopyMsg\x1a\x12.netem.AckResponse\"\x00(\x01\x12\x36\n\nLinkUpdate\x12\x12.netem.LinkRequest\x1a\x12.netem.AckResponse\"\x00\x42*Z(github.com/mroy31/gonetem/internal/protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.netem_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z(github.com/mroy31/gonetem/internal/proto'
  _globals['_STATUSCODE']._serialized_start=2905
  _globals['_STATUSCODE']._serialized_end=2936
  _globals['_IFSTATE']._serialized_start=2938
  _globals['_IFSTATE']._serialized_end=2965
  _globals['_COPYMSG']._serialized_start=58
  _globals['_COPYMSG']._serialized_end=202
  _globals['_COPYMSG_CODE']._serialized_start=165
  _globals['_COPYMSG_CODE']._serialized_end=202
  _globals['_CONSOLECLTMSG']._serialized_start=205
  _globals['_CONSOLECLTMSG']._serialized_end=407
  _globals['_CONSOLECLTMSG_CODE']._serialized_start=358
  _globals['_CONSOLECLTMSG_CODE']._serialized_end=407
  _globals['_CONSOLESRVMSG']._serialized_start=409
  _globals['_CONSOLESRVMSG']._serialized_end=533
  _globals['_CONSOLESRVMSG_CODE']._serialized_start=481
  _globals['_CONSOLESRVMSG_CODE']._serialized_end=533
  _globals['_PULLSRVMSG']._serialized_start=535
  _globals['_PULLSRVMSG']._serialized_end=653
  _globals['_PULLSRVMSG_CODE']._serialized_start=617
  _globals['_PULLSRVMSG_CODE']._serialized_end=653
  _globals['_CAPTURESRVMSG']._serialized_start=655
  _globals['_CAPTURESRVMSG']._serialized_end=776
  _globals['_CAPTURESRVMSG_CODE']._serialized_start=727
  _globals['_CAPTURESRVMSG_CODE']._serialized_end=776
  _globals['_TOPOLOGYRUNMSG']._serialized_start=779
  _globals['_TOPOLOGYRUNMSG']._serialized_end=1135
  _globals['_TOPOLOGYRUNMSG_NODEMESSAGES']._serialized_start=912
  _globals['_TOPOLOGYRUNMSG_NODEMESSAGES']._serialized_end=958
  _globals['_TOPOLOGYRUNMSG_CODE']._serialized_start=961
  _globals['_TOPOLOGYRUNMSG_CODE']._serialized_end=1135
  _globals['_PROJECTSAVEMSG']._serialized_start=1138
  _globals['_PROJECTSAVEMSG']._serialized_end=1274
  _globals['_PROJECTSAVEMSG_CODE']._serialized_start=1227
  _globals['_PROJECTSAVEMSG_CODE']._serialized_end=1274
  _globals['_PROJECTCLOSEMSG']._serialized_start=1277
  _globals['_PROJECTCLOSEMSG']._serialized_end=1428
  _globals['_PROJECTCLOSEMSG_CODE']._serialized_start=1354
  _globals['_PROJECTCLOSEMSG_CODE']._serialized_end=1428
  _globals['_LINKCONFIG']._serialized_start=1430
  _globals['_LINKCONFIG']._serialized_end=1517
  _globals['_LINKREQUEST']._serialized_start=1519
  _globals['_LINKREQUEST']._serialized_end=1580
  _globals['_NODEIFSTATEREQUEST']._serialized_start=1582
  _globals['_NODEIFSTATEREQUEST']._serialized_end=1679
  _globals['_NODEINTERFACEREQUEST']._serialized_start=1681
  _globals['_NODEINTERFACEREQUEST']._serialized_end=1749
  _globals['_NODEREQUEST']._serialized_start=1751
  _globals['_NODEREQUEST']._serialized_end=1793
  _globals['_PROJECTREQUEST']._serialized_start=1795
  _globals['_PROJECTREQUEST']._serialized_end=1823
  _globals['_WNETWORKREQUEST']._serialized_start=1825
  _globals['_WNETWORKREQUEST']._serialized_end=1868
  _globals['_OPENREQUEST']._serialized_start=1870
  _globals['_OPENREQUEST']._serialized_end=1911
  _globals['_STATUS']._serialized_start=1913
  _globals['_STATUS']._serialized_end=1969
  _globals['_ACKRESPONSE']._serialized_start=1971
  _globals['_ACKRESPONSE']._serialized_end=2015
  _globals['_FILERESPONSE']._serialized_start=2017
  _globals['_FILERESPONSE']._serialized_end=2076
  _globals['_VERSIONRESPONSE']._serialized_start=2078
  _globals['_VERSIONRESPONSE']._serialized_end=2143
  _globals['_STATUSRESPONSE']._serialized_start=2146
  _globals['_STATUSRESPONSE']._serialized_end=2455
  _globals['_STATUSRESPONSE_IFSTATUS']._serialized_start=2303
  _globals['_STATUSRESPONSE_IFSTATUS']._serialized_end=2358
  _globals['_STATUSRESPONSE_NODESTATUS']._serialized_start=2360
  _globals['_STATUSRESPONSE_NODESTATUS']._serialized_end=2455
  _globals['_CONFIGFILESRESPONSE']._serialized_start=2458
  _globals['_CONFIGFILESRESPONSE']._serialized_end=2693
  _globals['_CONFIGFILESRESPONSE_CONFIGFILE']._serialized_start=2617
  _globals['_CONFIGFILESRESPONSE_CONFIGFILE']._serialized_end=2657
  _globals['_CONFIGFILESRESPONSE_SOURCE']._serialized_start=2659
  _globals['_CONFIGFILESRESPONSE_SOURCE']._serialized_end=2693
  _globals['_PRJLISTRESPONSE']._serialized_start=2696
  _globals['_PRJLISTRESPONSE']._serialized_end=2841
  _globals['_PRJLISTRESPONSE_INFO']._serialized_start=2793
  _globals['_PRJLISTRESPONSE_INFO']._serialized_end=2841
  _globals['_PRJOPENRESPONSE']._serialized_start=2843
  _globals['_PRJOPENRESPONSE']._serialized_end=2903
  _globals['_NETEM']._serialized_start=2968
  _globals['_NETEM']._serialized_end=4704
# @@protoc_insertion_point(module_scope)
