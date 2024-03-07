# Standard library imports

# Remote library imports
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Local imports


# Instantiate app, set attributes
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.json.compact = False

# Define metadata, instantiate db

db = SQLAlchemy()
migrate = Migrate(app, db)
db.init_app(app)

#Api.error_router = lambda self, handler, e: handler(e)
# Instantiate REST API
api = Api(app)

# Instantiate CORS
CORS(app)

