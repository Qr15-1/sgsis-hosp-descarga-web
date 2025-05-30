import os

class Config:
    # Configuración base
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-change-in-production'
    STATIC_FOLDER = 'Estatico'
    TEMPLATE_FOLDER = 'Plantillas'
    
    # Configuración de archivos de descarga
    DOWNLOAD_FOLDER = os.path.join(STATIC_FOLDER, 'descarga')
    
    # Configuración de caché
    SEND_FILE_MAX_AGE_DEFAULT = 31536000  # 1 año en segundos
    
class DevelopmentConfig(Config):
    DEBUG = True
    
class ProductionConfig(Config):
    DEBUG = False
    # En producción, asegúrate de establecer una SECRET_KEY segura
    SECRET_KEY = os.environ.get('SECRET_KEY')  # Debe establecerse en variables de entorno
    
# Configuración por defecto basada en el entorno
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
} 