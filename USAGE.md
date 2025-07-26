# Usage

---

## Kullanım

### Gereksinimler

* Protobuf Compiler (protoc) yüklü olmalı
* Go, Rust, Node.js, Python ortamları kurulu olmalı
* Node.js için: `npm install` ile bağımlılıkları yükleyin
* Python için: sanal ortam açıp `pip install -r requirements.txt` yapın

### Kod Üretimi

Tüm diller için protobuf kodlarını üretmek için:

```bash
make
```

Bu komut:

* Go kodlarını `go/gen` klasörüne,
* Rust kodlarını `rust/src` klasörüne,
* Node.js kodlarını `nodejs/src` klasörüne,
* Python kodlarını `python/src` klasörüne

üretecektir.

---

### Hata ve Çözümler

* Eğer `protoc-gen-xyz` bulunamazsa, ilgili eklentinin yüklü ve PATH'te olduğundan emin olun.
* Node.js için `npm install` komutunu çalıştırmayı unutmayın.
* Python için `python -m grpc_tools.protoc` komutunun çalıştığından emin olun.

---

### İletişim

Herhangi bir sorun ya da öneri için lütfen issue açınız.

---

## Public Paket Olarak Kullanım

### 1. Repo Nasıl Kullanılır?

Bu repo, protobuf tanımlarını ve jenerasyonlarını içerir. Diğer projeler doğrudan bu repoyu bağımlılık olarak alıp, jenerasyonlu kodları kullanabilirler.

---

### Go için

```bash
go get github.com/sentiric/sentiric-core-interfaces/go/gen/...
```

Projede import:

```go
import (
  "github.com/sentiric/sentiric-core-interfaces/go/gen/sentiric/dialplan/v1"
)
```

---

### Rust için

`Cargo.toml` dosyasına ekleyin:

```toml
[dependencies]
sentiric-core-interfaces = { git = "https://github.com/sentiric/sentiric-core-interfaces.git", branch = "main" }
```

Projede kullanımı:

```rust
use sentiric_core_interfaces::sentiric::dialplan::v1::YourMessage;
```

> Not: Rust tarafında crate yapısı için repo düzenlemesi gerekebilir.

---

### Node.js için

```bash
npm install git+https://github.com/sentiric/sentiric-core-interfaces.git
```

Kullanım:

```js
const { YourMessage } = require('sentiric-core-interfaces/nodejs/src/sentiric/dialplan/v1/dialplan_pb');
```

---

### Python için

```bash
pip install git+https://github.com/sentiric/sentiric-core-interfaces.git
```

Veya repoyu klonlayıp:

```bash
export PYTHONPATH=$(pwd)/python/src:$PYTHONPATH
```

sonra:

```python
from sentiric.dialplan.v1 import dialplan_pb2
msg = dialplan_pb2.YourMessage()
```

---

## Önemli Notlar

* Diğer projeler, bu repoyu dependency olarak eklediklerinde, genellikle jenerasyonlu kodlar repoda hazır olacak.
* Kodlar hazır değilse veya protolar güncellenmişse, `make` komutu ile güncelleme yapılabilir.
* Repoyu versiyonlayarak (örn. git tag) ve release oluşturarak stabil sürümlerle çalışılması tavsiye edilir.

---

## Örnek Kullanım — Go

```go
package main

import (
    "fmt"
    dialplan "github.com/sentiric/sentiric-core-interfaces/go/gen/sentiric/dialplan/v1"
)

func main() {
    req := &dialplan.YourMessage{
        Field1: "Hello",
        Field2: 42,
    }
    fmt.Println(req)
}
```

**Çalıştırmak için:**

1. Modülünüze aşağıdaki komutu ekleyin:

```bash
go get github.com/sentiric/sentiric-core-interfaces/go/gen/...
```

2. Yukarıdaki örneği `main.go` olarak kaydedin.
3. `go run main.go` ile çalıştırın.

---

## Örnek Kullanım — Node.js

```js
const { YourMessage } = require('sentiric-core-interfaces/nodejs/src/sentiric/dialplan/v1/dialplan_pb');

const msg = new YourMessage();
msg.setField1('Hello');
msg.setField2(42);

console.log(msg.toObject());
```

