"""
Podman örneği için basit Flask REST API.
Birden fazla endpoint, ortam değişkeni kullanımı ve log içerir.
"""
import logging
import os
import platform
import socket
from datetime import datetime

from flask import Flask, jsonify, request

# Logging ayarları
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Ortam değişkenleri (Containerfile veya `podman run -e` ile override edilebilir)
APP_NAME = os.getenv("APP_NAME", "Podman Demo API")
APP_PORT = int(os.getenv("APP_PORT", "5000"))
APP_ENV = os.getenv("APP_ENV", "development")

# Basit in-memory veri (gerçek bir DB yerine demo amaçlı)
items = [
    {"id": 1, "name": "Birinci öğe"},
    {"id": 2, "name": "İkinci öğe"},
]


@app.route("/")
def index():
    """Ana sayfa - servisin çalıştığını doğrular."""
    logger.info("Ana sayfa isteği alındı")
    return jsonify({
        "app": APP_NAME,
        "env": APP_ENV,
        "message": "Podman içinde çalışan Flask API'ye hoş geldiniz.",
        "endpoints": ["/", "/health", "/info", "/api/items"],
    })


@app.route("/health")
def health():
    """Healthcheck endpoint'i - Containerfile içindeki HEALTHCHECK bunu kullanır."""
    return jsonify({"status": "ok", "timestamp": datetime.utcnow().isoformat()})


@app.route("/info")
def info():
    """Container/sistem bilgisi - Podman içinden bakıldığında neyin görüldüğünü gösterir."""
    return jsonify({
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
        "python_version": platform.python_version(),
        "env": APP_ENV,
    })


@app.route("/api/items", methods=["GET", "POST"])
def items_handler():
    """GET: tüm öğeleri döndürür. POST: yeni öğe ekler."""
    if request.method == "POST":
        data = request.get_json(silent=True) or {}
        name = data.get("name")
        if not name:
            return jsonify({"error": "'name' alanı zorunlu"}), 400
        new_id = max((i["id"] for i in items), default=0) + 1
        new_item = {"id": new_id, "name": name}
        items.append(new_item)
        logger.info("Yeni öğe eklendi: %s", new_item)
        return jsonify(new_item), 201
    return jsonify({"count": len(items), "items": items})


if __name__ == "__main__":
    logger.info("Uygulama başlatılıyor: %s (port=%s, env=%s)", APP_NAME, APP_PORT, APP_ENV)
    app.run(host="0.0.0.0", port=APP_PORT)
