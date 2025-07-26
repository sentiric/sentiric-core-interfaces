# Sentiric Core Interfaces

Bu repo Protobuf dosyalarından Go, Rust, Node.js ve Python için otomatik olarak kaynak kodu üretir.

---

## Gereksinimler

- [Protocol Buffers (protoc)](https://grpc.io/docs/protoc-installation/) kurulu olmalı ve PATH'te bulunmalı.
- Go (1.19+)
- Rust (1.70+)
- Node.js (16+)
- Python 3.8+
- Python sanal ortam (venv) kullanılması tavsiye edilir.

---

## Gerekli Paketlerin Kurulumu

### Python
```bash
python -m venv .venv
.\.venv\Scripts\activate      # Windows
source .venv/bin/activate     # Linux/Mac
pip install grpcio grpcio-tools
````

### Node.js

```bash
npm install --save-dev grpc-tools grpc_tools_node_protoc grpc-web
```

### Rust

```bash
cargo install prost-build
```

### Go

```bash
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
```

---

## Kod Üretimi

Aşağıdaki komut tüm diller için protobuf dosyalarından kod üretir:

```bash
make
```

---

## Alternatif: Tek Dil İçin Kod Üretimi

* Go için:

```bash
make go
```

* Rust için:

```bash
make rust
```

* Node.js için:

```bash
make nodejs
```

* Python için:

```bash
make python
```

---

## Notlar

* `protoc` komutu PATH'te olmalıdır.
* Python için `grpcio-tools` paketinin kurulması gereklidir.
* Node.js tarafında `grpc-tools` ve `grpc-web` yüklü olmalıdır.

---

## İletişim

Herhangi bir sorun veya katkı için lütfen issue açınız.

