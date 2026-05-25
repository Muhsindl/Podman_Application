# Podman Application 6 — Flask REST API

Bu proje, **Podman** ile bir Python (Flask) uygulamasının nasıl konteynerleştirileceğini gösteren bir örnektir. İçinde küçük bir REST API, healthcheck, ortam değişkeni kullanımı ve root olmayan kullanıcı konfigürasyonu yer alır.

## 📁 Dizin Yapısı

```
Podman_Application6/
├── app.py            # Flask uygulaması
├── requirements.txt  # Python bağımlılıkları
├── Containerfile     # Container imajı tanımı
└── README.md         # Bu dosya
```

## 🔧 Gereksinimler

- Podman 4.0+ (`podman --version` ile kontrol edebilirsiniz)
- Linux / macOS / Windows (WSL2)

> Docker biliyorsanız Podman komutları neredeyse birebir aynıdır. `docker` yerine `podman` yazmanız yeterli.

## 🚀 Hızlı Başlangıç

### 1. İmajı oluştur

```bash
podman build -t podman-demo-api:latest .
```

`-t` ile imaja isim ve etiket veriyoruz. `.` ise build context'in mevcut dizin olduğunu söyler.

### 2. Container'ı çalıştır

```bash
podman run -d \
  --name demo-api \
  -p 5000:5000 \
  podman-demo-api:latest
```

| Bayrak | Açıklama |
|--------|----------|
| `-d`   | Detached (arka planda) çalıştır |
| `--name` | Container'a isim ver |
| `-p 5000:5000` | Host'un 5000 portunu container'ın 5000'ine bağla |

### 3. Test et

```bash
curl http://localhost:5000/
curl http://localhost:5000/health
curl http://localhost:5000/info
curl http://localhost:5000/api/items
curl -X POST http://localhost:5000/api/items \
     -H "Content-Type: application/json" \
     -d '{"name":"Yeni öğe"}'
```

## 🛠️ Sık Kullanılan Komutlar

### Container yönetimi

```bash
podman ps                  # Çalışan container'ları listele
podman ps -a               # Tüm container'ları (durmuş olanlar dahil) listele
podman logs demo-api       # Logları görüntüle
podman logs -f demo-api    # Logları canlı takip et
podman stop demo-api       # Durdur
podman start demo-api      # Tekrar başlat
podman restart demo-api    # Yeniden başlat
podman rm demo-api         # Sil (önce durdurulmalı)
podman rm -f demo-api      # Zorla sil
```

### Container'ın içine girmek

```bash
podman exec -it demo-api /bin/bash
```

### İmaj yönetimi

```bash
podman images              # Lokal imajları listele
podman rmi podman-demo-api # İmajı sil
podman image prune         # Kullanılmayan imajları temizle
```

### Detaylı bilgi

```bash
podman inspect demo-api    # Container hakkında JSON detay
podman stats demo-api      # CPU/RAM kullanımı (canlı)
podman top demo-api        # Container içindeki süreçler
podman healthcheck run demo-api  # Healthcheck'i manuel tetikle
```

## ⚙️ Ortam Değişkenleri ile Özelleştirme

Containerfile'da tanımlı varsayılanları `-e` ile override edebilirsiniz:

```bash
podman run -d \
  --name demo-api \
  -p 8080:5000 \
  -e APP_NAME="Üretim API" \
  -e APP_ENV=production \
  podman-demo-api:latest
```

## 💾 Volume Kullanımı

Container silindiğinde verilerin kaybolmaması için volume bağlayabilirsiniz:

```bash
# Named volume oluştur
podman volume create demo-data

# Volume ile çalıştır
podman run -d \
  --name demo-api \
  -p 5000:5000 \
  -v demo-data:/app/data \
  podman-demo-api:latest

# Volume'leri listele
podman volume ls
podman volume inspect demo-data
```

Host dizinini bind mount olarak bağlamak için:

```bash
podman run -d -v $(pwd)/logs:/app/logs:Z podman-demo-api:latest
```

> `:Z` SELinux etkin sistemlerde (RHEL/Fedora) gereklidir.

## 🌐 Network

```bash
# Özel network oluştur
podman network create demo-net

# Container'ı bu network'e bağla
podman run -d --name demo-api --network demo-net -p 5000:5000 podman-demo-api:latest

# Network'leri listele
podman network ls
podman network inspect demo-net
```

## 🔍 Sorun Giderme

| Sorun | Çözüm |
|-------|-------|
| `port already in use` | Host port'unu değiştirin: `-p 5001:5000` |
| Logda hata görünmüyor | `podman logs --tail 100 demo-api` |
| Container hemen kapanıyor | `podman logs demo-api` ile hatayı görün, `podman run` komutunda `-d` yerine geçici olarak interactive çalıştırın |
| İmaj güncellenmiyor | `--no-cache` ile rebuild edin: `podman build --no-cache -t podman-demo-api .` |
| Healthcheck FAIL | `podman inspect demo-api --format '{{.State.Health}}'` ile detayı görün |

## 🧹 Temizlik

```bash
podman stop demo-api && podman rm demo-api
podman rmi podman-demo-api:latest
podman system prune -a       # Tüm kullanılmayan kaynakları sil
```

## 📝 Notlar

- **Rootless mod:** Podman varsayılan olarak root yetkisi olmadan çalışır — bu Docker'a karşı en büyük güvenlik avantajıdır.
- **Daemonless:** Podman'da merkezi bir daemon yoktur, her komut bağımsız bir süreç olarak çalışır.
- **Pod desteği:** Birden fazla container'ı Kubernetes mantığında "pod" olarak gruplayabilirsiniz (`podman pod create`).
- **Compose:** `podman-compose` veya `podman play kube` ile çoklu container senaryoları yönetilebilir.
