from flask import Flask
app = Flask(__name__)

@app.route('/')
def merhaba():
    return "Podman'den Merhaba!"

if __name__ == '__main__':
    # Uygulamayı dışarıya açmak için host='0.0.0.0' kullanıyoruz
    app.run(host='0.0.0.0', port=5000)
