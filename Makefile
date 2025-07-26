.PHONY: all go rust nodejs python

all: go rust nodejs python

go:
	@echo "Generating Go code..."
	protoc -I=proto \
	  --go_out=go/gen --go_opt=paths=source_relative \
	  --go-grpc_out=go/gen --go-grpc_opt=paths=source_relative \
	  proto/sentiric/dialplan/v1/dialplan.proto \
	  proto/sentiric/media/v1/media.proto \
	  proto/sentiric/user/v1/user.proto

rust:
	@echo "Generating Rust code..."
	protoc -I=proto \
	  --prost_out=rust/src \
	  proto/sentiric/dialplan/v1/dialplan.proto \
	  proto/sentiric/media/v1/media.proto \
	  proto/sentiric/user/v1/user.proto

nodejs:
	@echo "Generating Node.js code..."
	npx grpc_tools_node_protoc \
		--js_out=import_style=commonjs,binary:nodejs/src \
		--grpc_out=nodejs/src \
		-I proto \
		proto/sentiric/dialplan/v1/dialplan.proto \
		proto/sentiric/media/v1/media.proto \
		proto/sentiric/user/v1/user.proto

python:
	@echo "Generating Python code..."
	python -m grpc_tools.protoc \
		-I proto \
		--python_out=python/src \
		--grpc_python_out=python/src \
		proto/sentiric/dialplan/v1/dialplan.proto \
		proto/sentiric/media/v1/media.proto \
		proto/sentiric/user/v1/user.proto