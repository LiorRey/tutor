from flask import Flask
from tutor.config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)
