import os
import json
from flask import Flask, request, Response
from flask import render_template, send_from_directory, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
api_manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Person, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Computer, methods=['GET'])

import views

