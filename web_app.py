# web_app.py
from flask import Flask, render_template, send_from_directory
import os

# Configuración de Flask para que encuentre tus carpetas 'Plantillas' y 'Estatico'
app = Flask(__name__, template_folder='Plantillas', static_folder='Estatico')

# Ruta COMPLETA a la carpeta donde se encuentran los archivos para descargar
DOWNLOAD_FOLDER = os.path.join(app.root_path, app.static_folder, 'descarga')

# Asegura que la carpeta de descargas exista al iniciar la aplicación
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)
    print(f"Carpeta de descargas creada: {DOWNLOAD_FOLDER}")

# Ruta para la página de inicio (cuando alguien visita '/')
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la descarga de archivos (cuando alguien visita '/descargar/nombre_archivo.exe')
@app.route('/descargar/<filename>')
def download_file(filename):
    try:
        return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)
    except FileNotFoundError:
        return "Archivo no encontrado.", 404

# Bloque principal para ejecutar la aplicación Flask
if __name__ == '__main__':
    # `debug=True` es útil para el desarrollo: recarga el servidor automáticamente con los cambios
    app.run(debug=True)