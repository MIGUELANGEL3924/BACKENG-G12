from flask import Flask
from db import db
from sqlalchemy import column, Integer, String

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"


class Products(db.Model):
    id = column(Integer, primary_key=True)
    name = column(String(45))
    stock = column(Integer)

    @app.before_firts_request
    def first_request():
        db.create_all()


@app.route('/')
def index():
    return 'hello world'


@app.route("/products")
def products():
    return "esta es la ruta productos"


if __name__ == '__main__':
    app.run(debug=True)
