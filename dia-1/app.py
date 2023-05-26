from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# "postgresql://username:password@localhost:5432/dbname"
app.config['SQLALCHEMY_DATABASE_URI']


@app.route('/')
def index():
    return 'hello world'


@app.route('/about')
def about():
    return 'about page'


if __name__ == '__main__':
    app.run(debug=True)
