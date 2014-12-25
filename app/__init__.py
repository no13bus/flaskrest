import os
import json
from flask import Flask, request, Response
from flask import render_template, send_from_directory, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager, ProcessingException
from flask.ext.login import current_user, login_user, LoginManager, UserMixin
from flask.ext.httpauth import HTTPBasicAuth

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

users1 = {
    "john": "hello",
    "susan": "bye"
}




# Define pre- and postprocessor functions as described below.
def pre_get_single(**kw): pass
def pre_get_many(**kw): pass
def post_patch_many(**kw): pass
def pre_delete(**kw): pass


from models import Person, Computer, User
api_manager = APIManager(app, flask_sqlalchemy_db=db)

def auth_func(**kw):
    if not current_user.is_authenticated():
        raise ProcessingException(description='Not Authorized', code=401)

api_manager.create_api(Person,
                   # Allow GET, PATCH, and POST requests.
                   methods=['GET', 'DELETE', 'PUT', 'POST'],
                   # Allow PATCH requests modifying the whole collection.
                   allow_patch_many=True,
                   # A list of preprocessors for each method.
                   
                   # A list of postprocessors for each method.
                   postprocessors={
                       'PATCH_MANY': [post_patch_many]
                       }
                   )

api_manager.create_api(Computer, methods=['GET', 'POST'])
api_manager.create_api(User, methods=['GET', 'POST'])

login_manager = LoginManager()
login_manager.setup_app(app)


import views

