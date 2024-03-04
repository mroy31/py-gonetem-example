
proto: proto/netem.proto
	python -m grpc_tools.protoc --proto_path=. \
	    --pyi_out=. --python_out=. --grpc_python_out=. \
		proto/netem.proto

.PHONY: proto 