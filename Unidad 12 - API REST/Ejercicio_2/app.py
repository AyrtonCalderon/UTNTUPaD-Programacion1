from flask import Flask
from autores_routes import autores_bp
from libros_routes import libros_bp

app = Flask(__name__)

# Registramos los Blueprints (las rutas de cada módulo)
app.register_blueprint(autores_bp)
app.register_blueprint(libros_bp)

if __name__ == '__main__':
    app.run(debug=True)