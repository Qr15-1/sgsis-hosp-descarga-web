# web_app.py
from flask import Flask, render_template, send_from_directory, abort
import os
from config import config

def create_app(config_name='default'):
    # Inicialización de la aplicación Flask
    app = Flask(__name__,
                template_folder=config[config_name].TEMPLATE_FOLDER,
                static_folder=config[config_name].STATIC_FOLDER)
    
    # Aplicar configuración
    app.config.from_object(config[config_name])
    
    # Asegurar que existe la carpeta de descargas
    download_path = os.path.join(app.root_path, app.config['DOWNLOAD_FOLDER'])
    if not os.path.exists(download_path):
        os.makedirs(download_path)
        print(f"Carpeta de descargas creada: {download_path}")

    # Rutas de la aplicación
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/descargar/<filename>')
    def download_file(filename):
        try:
            # Validación básica del nombre de archivo
            if not filename or '..' in filename:
                abort(404)
            
            # Configurar headers para caché
            cache_timeout = app.config['SEND_FILE_MAX_AGE_DEFAULT']
            
            return send_from_directory(
                download_path,
                filename,
                as_attachment=True,
                max_age=cache_timeout
            )
        except Exception as e:
            print(f"Error al descargar archivo: {str(e)}")
            abort(404)

    @app.errorhandler(404)
    def not_found_error(error):
        return "Archivo no encontrado.", 404

    @app.errorhandler(500)
    def internal_error(error):
        return "Error interno del servidor.", 500

    return app

# Crear y ejecutar la aplicación
if __name__ == '__main__':
    # Determinar el entorno (development por defecto)
    env = os.environ.get('FLASK_ENV', 'development')
    app = create_app(env)
    app.run()