from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/sensor", methods=["POST"])
def proceso_json():
    if request.is_json:  # verifica que el Content-Type sea application/json
        data = request.json
        nombre = data.get('Nombre : Luxometr0')
        valor = data.get('Valor: 135555')
        print(f"{nombre}, {valor}")
        return "Ok" 