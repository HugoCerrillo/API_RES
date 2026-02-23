from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app) # Importante para que React pueda consultar la API

# Configuración de conexión (Obtén estos datos de tu consola de TiDB Cloud)
db_config = {
    'host': 'gateway01.us-east-1.prod.aws.tidbcloud.com',
    'username': '4EpEm4BSHmLBBsU.root',
    'password': 'fQXvQOaUHsAPA9k8',
    'database': 'prueba',
    'port': 4000,    
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/api/productos', methods=['GET'])
def get_usuarios():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos")
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(datos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Esto permite que Render elija el puerto dinámicamente
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)