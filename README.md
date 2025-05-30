# SGASIS-Hosp Página de Descarga

Página web para la descarga del Sistema de Gestión de Asistencia Hospitalaria (SGASIS-Hosp).

## Características

- Diseño moderno y minimalista con tema oscuro
- Botón de descarga con efectos visuales de voltaje eléctrico
- Instrucciones detalladas de instalación
- Diseño responsive para dispositivos móviles
- Optimización de caché para archivos estáticos
- Manejo seguro de descargas de archivos

## Requisitos

- Python 3.8 o superior
- Flask 3.1.1
- Navegador web moderno con soporte para CSS3

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/sgsis-hosp-descarga-web.git
cd sgsis-hosp-descarga-web
```

2. Crear un entorno virtual:
```bash
python -m venv venv_web
```

3. Activar el entorno virtual:
- Windows:
```bash
venv_web\Scripts\activate
```
- Linux/Mac:
```bash
source venv_web/bin/activate
```

4. Instalar dependencias:
```bash
pip install -r requirements.txt
```

5. Configurar variables de entorno (opcional):
```bash
# Windows
set FLASK_ENV=development
set SECRET_KEY=tu-clave-secreta

# Linux/Mac
export FLASK_ENV=development
export SECRET_KEY=tu-clave-secreta
```

6. Ejecutar la aplicación:
```bash
python web_app.py
```

## Estructura del Proyecto

```
sgsis-hosp-descarga-web/
├── Estatico/
│   ├── css/
│   │   └── estilo.css
│   └── descarga/
│       └── Asistencia.exe
├── Plantillas/
│   └── index.html
├── config.py
├── web_app.py
├── requirements.txt
└── README.md
```

## Configuración

El proyecto utiliza un sistema de configuración basado en clases que permite diferentes entornos:

- `development`: Modo de desarrollo con depuración activada
- `production`: Modo de producción con configuraciones optimizadas

Para cambiar entre entornos, establece la variable de entorno `FLASK_ENV`:
```bash
export FLASK_ENV=production  # Linux/Mac
set FLASK_ENV=production    # Windows
```

## Seguridad

- Validación de nombres de archivo en descargas
- Manejo seguro de rutas para prevenir directory traversal
- Configuración de SECRET_KEY para producción
- Headers de caché configurados correctamente

## Desarrollo

Para contribuir al proyecto:

1. Crea un fork del repositorio
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Realiza tus cambios y haz commit (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto

Tu Nombre - [@tu_twitter](https://twitter.com/tu_twitter) - email@example.com

Link del Proyecto: [https://github.com/tu-usuario/sgsis-hosp-descarga-web](https://github.com/tu-usuario/sgsis-hosp-descarga-web)  
