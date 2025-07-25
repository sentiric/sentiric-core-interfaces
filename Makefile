PROTO_DIR := proto

PROTO_FILES := \
  $(PROTO_DIR)/sentiric/dialplan/v1/dialplan.proto \
  $(PROTO_DIR)/sentiric/media/v1/media.proto \
  $(PROTO_DIR)/sentiric/user/v1/user.proto

.PHONY: all gen-go gen-python gen-rust clean

all: gen-go gen-python gen-rust
	@echo "Tüm diller için protobuf dosyaları üretildi."

gen-go:
	if not exist gen\go mkdir gen\go
	protoc -I=$(PROTO_DIR) --go_out=gen/go --go_opt=paths=source_relative --go-grpc_out=gen/go --go-grpc_opt=paths=source_relative $(PROTO_FILES)
	@echo "Go kodları üretildi."

gen-python:
	if not exist gen\python mkdir gen\python
	python -m grpc_tools.protoc -I=$(PROTO_DIR) --python_out=gen/python --grpc_python_out=gen/python $(PROTO_FILES)
	@echo "Python kodları üretildi."

gen-rust:
	if not exist gen\rust mkdir gen\rust
	protoc -I=$(PROTO_DIR) --rust_out=gen/rust --rust_opt=kernel=upb,experimental-codegen=enabled $(PROTO_FILES)
	@echo "Rust kodları üretildi (temel protobuf)."

clean:
	if exist gen\go rmdir /s /q gen\go
	if exist gen\python rmdir /s /q gen\python
	if exist gen\rust rmdir /s /q gen\rust
	@echo "Üretilen dosyalar temizlendi."