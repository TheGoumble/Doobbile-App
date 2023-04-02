from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from doobbile_app.secrets import SECRET_KEY


app = Flask(__name__)

# will be changed when offically deployed
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from doobbile_app import routes