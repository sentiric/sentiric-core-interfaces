# Sentiric Core Interfaces

Bu depo, Sentiric ekosistemindeki tüm mikroservisler arasında paylaşılan API sözleşmelerini (`.proto` dosyaları), temel veri yapılarını ve evrensel sabitleri barındıran **tek doğruluk kaynağıdır.**

## Amaç

*   **Tutarlılık:** Tüm servislerin aynı dil ve veri modelleriyle konuşmasını garanti eder.
*   **Otomasyon:** Farklı diller (Go, Rust, Python) için gRPC istemci ve sunucu kodlarının otomatik olarak üretilmesini sağlar.

## Kullanım

Bu repo, çalışan bir servis değildir; diğer servisler tarafından bir bağımlılık olarak kullanılır.

### Gerekli Araçlar

Kod üretebilmek için aşağıdaki araçların sisteminizde kurulu olması gerekir:
*   `protoc` (Protocol Buffers Compiler)
*   Go için: `protoc-gen-go`, `protoc-gen-go-grpc`
*   Python için: `grpcio-tools`
*   Rust için: `tonic-build` ve `prost-build` (servislerin `build.rs` dosyalarında kullanılır)

### Kod Üretimi

Tüm diller için kodları üretmek için ana dizinde `make` komutunu çalıştırmanız yeterlidir:

```bash
# Tüm diller için üret
make all

# Sadece Go için üret
make gen-go

# Üretilen dosyaları temizle
make clean