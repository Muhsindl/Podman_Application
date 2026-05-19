# Podman Network Tester

Bu proje, Podman kullanarak çalışan basit bir container uygulamasıdır. Container başlatıldığında sistem bilgilerini gösterir ve `google.com` adresine ping testi yapar.

## Kullanılan Teknolojiler

* Podman
* Alpine Linux
* Bash Script

## Proje Dosyaları

* `Containerfile` → Container yapılandırması
* `entrypoint.sh` → Çalışan ana script
* `README.md` → Dokümantasyon

## Kurulum

Repoyu klonlayın:

```bash
git clone https://github.com/Muhsindl/Podman_Application.git
cd Podman_Application3
```

İmajı oluşturun:

```bash
podman build -t net-tester .
```

Container'ı çalıştırın:

```bash
podman run --rm net-tester
```

## Geliştirici

Muhsin DOLU
