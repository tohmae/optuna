# You can set these variables from the command line.
PYTHON = python

protobuf:
	$(PYTHON) -m grpc_tools.protoc -I./ --python_out=../ --grpc_python_out=../ optuna/protobuf/*.proto
	sed -i '1s/^/# flake8: NOQA\n/' ../optuna/protobuf/*.py
