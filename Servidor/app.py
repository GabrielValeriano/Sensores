from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello; World!</p>"

@app.route("/api/sensores" , methods =["POST"])
def json_Date():
    data = request.json
    nombre = data.get("luxometro")
    valor = data.get(135)
    return print(nombre, valor, "ok")