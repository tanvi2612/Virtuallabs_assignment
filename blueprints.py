from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SelectField

#Initialise the flask app and the db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accuracy.db'
app.config['SECRET_KEY'] = 'any secret string'
db = SQLAlchemy(app)