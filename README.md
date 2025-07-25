Here's a professional **README.md** for your project in both English and Turkish:

---

# Sentiric Core Interfaces

Multi-language Protobuf/GRPC interface definitions for Sentiric services.

## 📦 Available Packages
```
proto/
├── sentiric/
│   ├── dialplan/
│   │   └── v1/
│   ├── media/
│   │   └── v1/
│   └── user/
│       └── v1/
```

## 🛠️ Build Instructions

### Requirements
- Protocol Buffers compiler (`protoc`) v3+
- Go (for Go codegen)
- Python (for Python codegen)
- Rust (for Rust codegen)

### Generate All Code
```bash
make all
```

### Language-Specific Targets
```bash
make gen-go      # Generate Go code
make gen-python  # Generate Python code
make gen-rust    # Generate Rust code
```

### Clean Generated Files
```bash
make clean
```

## 📚 Generated Code Structure
```
gen/
├── go/          # Go package
├── python/      # Python package
└── rust/        # Rust crate
```

## 🌍 Multi-Language Support
| Language | Status  | gRPC Support |
|----------|---------|--------------|
| Go       | ✅ Stable | Yes          |
| Python   | ✅ Stable | Yes          |
| Rust     | ⚠️ Experimental | Basic       |

---
