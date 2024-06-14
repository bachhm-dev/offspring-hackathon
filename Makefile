
protobuf:
	python -m grpc_tools.protoc -I./proto --python_out=. --pyi_out=. --grpc_python_out=. ./proto/face_swap.proto

.PHONY: protobuf