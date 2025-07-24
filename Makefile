.PHONY: all clean gen-go gen-rust gen-python

# Araçlar - Geliştiricinin bunları kurduğu varsayılır.
PROTOC = protoc
# Go
GO_OUT_DIR = ../gen/go
# Rust
RUST_OUT_DIR = ../gen/rust
# Python
PYTHON_OUT_DIR = ../gen/python

# Tüm diller için kod üretir
all: gen-go gen-rust gen-python

# Go için kod üretir
gen-go:
	@echo "Generating Go stubs..."
	@mkdir -p $(GO_OUT_DIR)
	$(PROTOC) --proto_path=proto \
		--go_out=$(GO_OUT_DIR) --go_opt=paths=source_relative \
		--go-grpc_out=$(GO_OUT_DIR) --go-grpc_opt=paths=source_relative \
		proto/sentiric/**/*.proto

# Rust için kod üretir (tonic-build ile)
gen-rust:
	@echo "Generating Rust stubs... (Note: Rust generation is typically handled by build.rs)"
	@echo "To generate manually for inspection, you'd use tonic_build."
	@echo "This target is a placeholder. Add a build.rs to each Rust service instead."

# Python için kod üretir
gen-python:
	@echo "Generating Python stubs..."
	@mkdir -p $(PYTHON_OUT_DIR)
	python -m grpc_tools.protoc --proto_path=proto \
		--python_out=$(PYTHON_OUT_DIR) \
		--grpc_python_out=$(PYTHON_OUT_DIR) \
		proto/sentiric/**/*.proto

# Üretilen tüm dosyaları temizler
clean:
	@echo "Cleaning generated files..."
	@rm -rf ../gen