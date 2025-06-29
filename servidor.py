from flask import Flask, request, jsonify, render_template_string
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)

# Crear base de datos y tabla de usuarios
def init_db():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario TEXT UNIQUE NOT NULL,
                    contraseña TEXT NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/registro', methods=['POST'])
def registrar_usuario():
    data = request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    if not usuario or not contraseña:
        return jsonify({"error": "Datos incompletos"}), 400

    contraseña_hash = generate_password_hash(contraseña)

    try:
        conn = sqlite3.connect('usuarios.db')
        c = conn.cursor()
        c.execute('INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)', (usuario, contraseña_hash))
        conn.commit()
        return jsonify({"mensaje": "Usuario registrado con éxito"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "El usuario ya existe"}), 409
    finally:
        conn.close()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('SELECT contraseña FROM usuarios WHERE usuario = ?', (usuario,))
    fila = c.fetchone()
    conn.close()

    if fila and check_password_hash(fila[0], contraseña):
        return jsonify({"mensaje": "Inicio de sesión exitoso"}), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401

@app.route('/tareas', methods=['GET'])
def tareas():
    html = "<h1>Bienvenido al sistema de tareas</h1><p>Acceso autorizado</p>"
    return render_template_string(html)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
