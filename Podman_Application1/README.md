# 🦭 Hello Podman Uygulaması (Podman_Application1)

Bu proje, Podman kullanarak özel bir imaj oluşturmayı (**build**) ve bu imajı bir konteyner olarak çalıştırmayı (**run**) gösteren temel bir uygulamadır. Çalıştırıldığında ekrana basit bir karşılama mesajı yazdırır.

---

## 🛠️ Nasıl Kurulur ve Çalıştırılır?

Bu projeyi kendi bilgisayarınızda adım adım oluşturmak ve test etmek için aşağıdaki talimatları izleyin.

### 1. Proje Klasörüne Girin

Eğer repoyu klonladıysanız, terminal üzerinden bu projenin klasörüne geçiş yapın:

```bash
cd Podman_Application1
```

---

### 2. İmajı İnşa Edin (Build)

Klasörün içinde bulunan `Containerfile` (veya `Dockerfile`) dosyasını kullanarak kendi lokal imajınızı oluşturun. Sondaki noktayı (`.`) unutmayın!

```bash
podman build -t muhsindolu/hello-podman .
```

> Bu işlem, hafif bir Linux dağıtımı olan Alpine'i indirip içine bizim özel mesaj komutumuzu yerleştirir.

---

### 3. Konteyneri Çalıştırın (Run)

İmaj başarıyla oluşturulduktan sonra, aşağıdaki komutla konteyneri ayağa kaldırıp mesajı görebilirsiniz:

```bash
podman run --rm muhsindolu/hello-podman
```

> **Not:** `--rm` parametresi, işlem tamamlandıktan sonra konteynerin otomatik olarak silinmesini sağlar.

---

## ☁️ (Alternatif) Docker Hub'dan Çalıştırma

Eğer imajı kendiniz oluşturmak istemezseniz, Docker Hub üzerindeki hazır versiyonu kullanabilirsiniz.

### İmajı indirmek (pull)

```bash
podman pull docker.io/muhsindolu/hello-podman
```

### İmajı çalıştırmak (run)

```bash
podman run --rm docker.io/muhsindolu/hello-podman
```
