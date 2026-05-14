# Imaj oluşturuluyor
podman build -t flask-uygulamasi .

# Konteynerin 5000 portunu makinenizin 8080 portuna bağlıyoruz
'podman run -d -p 8080:5000 flask-uygulamasi'
