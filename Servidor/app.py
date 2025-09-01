import sqlite3
from flask import Flask, g, jsonify, request, url_for
from math import ceil

def dict_factory(cursor, row):
  """Arma un diccionario con los valores de la fila."""
  fields = [column[0] for column in cursor.description]  
  """cursor.description devuelve los nombres de las columnas."""
  return {key: value for key, value in zip(fields, row)}
"""zip(fields, row) junta el nombre de cada columna con su valor en esa fila.
Ejemplo: si la consulta devuelve ("temperatura", 25), lo convierte en {"temperatura": 25}."""

def abrirConexion():
   if 'db' not in g: # Si todavía no hay conexión guardada en 'g'
      g.db = sqlite3.connect("sensores.sqlite") # Abre la BD 'sensores.sqlite'
      g.db.row_factory = dict_factory # Para que cada fila se devuelva como diccionario
   return g.db

def cerrarConexion(e=None):
    db = g.pop('db', None)  # Saca la conexión guardada en 'g'
    if db is not None:      # Si existía conexión
        db.close()          # Se cierra

app = Flask(__name__)
app.teardown_appcontext(cerrarConexion)
"""teardown_appcontext: registra la función cerrarConexion para que se ejecute 
automáticamente cuando termine la petición (así nunca queda la BD abierta)."""

@app.route("/api/test") #Sirve para comprobar que la API está en marcha.
def test():
    return "funcionando!"

@app.route("/api/sensor", methods=['POST'])
def sensor():
    datos = request.json  # Obtiene el cuerpo de la petición en formato JSON
    nombre = datos["nombre"]  # Extrae el campo "nombre"
    valor = datos["valor"]    # Extrae el campo "valor"
    id = datos["id"]
    fecha_hora = datos["fecha_hora"]
    db = abrirConexion()
    db.execute("INSERT INTO datos (nombre, valor), VALUES(?, ?)")
    db.commit()
    cerrarConexion()
    print(f"nombre del sensor {id}, {nombre}, valor: {valor}, Fecha_hora: {fecha_hora}")  # Muestra en consola
    return "OK"

@app.route("/api/sensor", methods=['POST'])
def sensor():
    datos = request.json  # Obtiene el cuerpo de la petición en formato JSON
    nombre = datos["nombre"]  # Extrae el campo "nombre"
    valor = datos["valor"]    # Extrae el campo "valor"
    id = datos["id"]
    fecha_hora = datos["fecha_hora"]
    db = abrirConexion()
    db.execute("INSERT INTO datos (nombre, valor), VALUES(?, ?)")
    db.commit()
    cerrarConexion()
    print(f"nombre del sensor {id}, {nombre}, valor: {valor}, Fecha_hora: {fecha_hora}")  # Muestra en consola
    return "OK"

@app.route('/api/register', methods=('GET'))
def login():
    if request.method == 'POST':
        nombre = request.form['nombre']
        valor = request.form['valor']
        db = abrirConexion
        nombre = db.execute(
            'SELECT * FROM datos WHERE nombre = ?', (nombre,)
        ).fetchold()
        db.commit()