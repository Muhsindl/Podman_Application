# Podman Dinamik Plot Uygulaması

Bu proje, Flask ve Plotly kullanılarak geliştirilmiş, web arayüzünden girilen frekans değerine göre dinamik olarak güncellenen bir grafik uygulamasıdır. Uygulama, Podman kullanılarak izole bir konteyner ortamında çalışacak şekilde tasarlanmıştır.

## Gereksinimler

* Sisteminizde Podman kurulu olmalıdır.

## Kurulum ve Çalıştırma Adımları

### 1. Projeyi Klonlayın ve Dizine Geçin

Öncelikle GitHub reposunu bilgisayarınıza indirin ve uygulamanın bulunduğu dizine girin:

```bash
git clone https://github.com/Muhsindl/Podman_Application.git
cd Podman_Application/Podman_Application5
```

### 2. Konteyner İmajını Oluşturun (Build)

Aşağıdaki komut, `Containerfile` içerisindeki adımları izleyerek temel Python imajını indirir ve gerekli kütüphaneleri (`Flask`, `Plotly` vb.) kurar.

> Komutun sonundaki `.` karakterini unutmayın.

```bash
podman build -t dinamik-plot-app .
```

### 3. Konteyneri Başlatın (Run)

İmaj başarıyla oluşturulduktan sonra aşağıdaki komut ile konteyneri arka planda başlatın:

```bash
podman run -d -p 5000:5000 --name my-plot-container localhost/dinamik-plot-app
```

Parametre açıklamaları:

* `-d` → Konteyneri arka planda çalıştırır.
* `-p 5000:5000` → Yerel makinedeki 5000 portunu konteyner içindeki 5000 portuna yönlendirir.
* `--name my-plot-container` → Konteynere özel bir isim verir.
* `localhost/dinamik-plot-app` → Oluşturulan yerel Podman imajını belirtir.

### 4. Uygulamayı Görüntüleyin

Konteyner çalıştıktan sonra web tarayıcınızı açın ve aşağıdaki adrese gidin:

```text
http://localhost:5000
```

Bu arayüz üzerinden frekans değerini değiştirerek grafiğin dinamik olarak güncellendiğini test edebilirsiniz.

## Konteyner Yönetimi

Uygulama ile işiniz bittiğinde çalışan konteyneri durdurmak ve silmek için aşağıdaki komutları kullanabilirsiniz.

### Konteyneri Durdurma

```bash
podman stop my-plot-container
```

### Konteyneri Silme

```bash
podman rm my-plot-container
```

## Kullanılan Teknolojiler

* Python
* Flask
* Plotly
* Podman
* HTML / CSS

## Proje Yapısı

```text
Podman_Application5/
├── app.py
├── requirements.txt
├── Containerfile
├── templates/
│   └── index.html
├── README.md
```

## GitHub Repo

[https://github.com/Muhsindl/Podman_Application.git](https://github.com/Muhsindl/Podman_Application.git)
