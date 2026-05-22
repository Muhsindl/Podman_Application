from flask import Flask, render_template, request
import plotly
import plotly.graph_objs as go
import numpy as np
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_plot', methods=['POST'])
def update_plot():
    # Arayüzden gelen frekans değerini al
    freq = float(request.form.get('frequency', 1.0))
    
    # X ve Y eksenleri için veri seti oluştur (Sinüs dalgası)
    x = np.linspace(0, 10, 100)
    y = np.sin(freq * x)

    # Plotly grafiğini hazırla
    fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines')])
    fig.update_layout(title=f'Dinamik Sinüs Dalgası (Frekans: {freq})', xaxis_title='X Ekseni', yaxis_title='Y Ekseni')

    # Frontend'e göndermek için JSON formatına çevir
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
