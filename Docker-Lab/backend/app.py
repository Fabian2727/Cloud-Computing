from flask import Flask, request, jsonify
from flask_cors import CORS  # <-- IMPORTANTE
import mysql.connector

app = Flask(__name__)
CORS(app)  # <-- ESTO HABILITA CONEXIONES DESDE OTRA IP/PUERTO

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = data['user']
    password = data['pass']
    
    conn = mysql.connector.connect(
        host='db',
        user='root',
        password='root',
        database='users'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (user, password))
    result = cursor.fetchone()
    
    if result:
        return jsonify({"message": "Login correcto"})
    else:
        return jsonify({"message": "Credenciales inválidas"}), 401
