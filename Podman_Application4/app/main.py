from flask import Flask, render_template
import datetime
import random

app = Flask(__name__)

GREETINGS = [
    "Merhaba, dünyama hoş geldin!",
    "Podman konteynerı  çalışıyor!",
    "Selamlar! Bugün harika bir gün."
]

@app.route("/")
def home():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    greeting = random.choice(GREETINGS)
    
    return render_template("index.html", time=current_time, greeting=greeting)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
