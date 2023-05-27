from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from base_de_datos import conexion
from models.usuarios_models import UsuarioModel
from models.mascotas_model import MascotaModel
from controllers.usuario_controller import UsuariosController

app = Flask(__name__)
# estaremos agregando nuestra librerias de flask_restful a nuestro proyecto de flask
api = Api(app=app)
# dialecto://username:password@host:port/db_name
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/mascotas'

# utilizamos la variable de conexion a la base de datos para setearla en nuestra conexion de sql alchemy
conexion.init_app(app)

# Aca inicializamos el proceso de migraciones
Migrate(app, conexion)


# definir las rutas utilizando la clase Api
api.add_resource(UsuariosController, '/usuarios', '/otra _ruta_usuarios')

if __name__ == '__main__':
    app.run(debug=True)
