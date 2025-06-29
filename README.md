# Sistema de Gestión de Tareas con API y SQLite

## 📌 Requisitos
- Python 3.x
- Flask
- werkzeug

## 💻 Instalación
1. Clona el repositorio:
```bash
git clone https://github.com/FedeGastaldi/PFO2-Redes.git
cd PFO2-Redes

2. Instalar dependencias:
pip install flask

3. Ejecutar el servidor:
python servidor.py

----------------------------------------------------------
4. Utilizar Postaman o en mi caso voy a utilizar Thunder Client para ejecutar las pruebas



----------------------------------------------------------

Respuestas Conceptuales
¿Por qué hashear contraseñas?
Porque guardar contraseñas en texto plano representa un riesgo de seguridad. Si un atacante accede a la base de datos, podrá ver todas las contraseñas de los usuarios. Hashearlas con algoritmos seguros como bcrypt o el de werkzeug evita que las contraseñas originales puedan ser recuperadas fácilmente, incluso si la base es comprometida.

Ventajas de usar SQLite
Simplicidad: No requiere instalación de servidor.

Liviano: Ideal para proyectos pequeños y prototipos.

Persistencia local: Guarda los datos en archivos .db.

Portabilidad: El archivo puede moverse fácilmente de un entorno a otro.