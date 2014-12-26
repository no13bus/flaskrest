from app import app, login_manager, auth
from flask import render_template, redirect, url_for, flash, jsonify, make_response
from forms import LoginForm
from models import *
from flask.ext.login import login_user, login_required, logout_user
from flask.ext.httpauth import HTTPBasicAuth


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)


@app.route('/', methods=['GET'])
def index():
    # return render_template('index.html')
    return make_response(open('app/templates/index.html').read())

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username, password = form.username.data, form.password.data
        matches = User.query.filter_by(username=username, password=password).all()
        if len(matches) > 0:
            login_user(matches[0])
            return redirect(url_for('index'))
        flash('Username and password pair not found')
    return render_template('login.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@auth.get_password
def get_pw(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return user.password
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access*****'}), 401)


@app.route('/topic', methods=['GET', 'POST'])
@auth.login_required
def topic():
    t = Topic.query.all()
    tmp = map(lambda x: x.to_dict(), t)
    return jsonify({"result":tmp}), 200

# @app.route('/api/v1/test')
# @auth.login_required
# def test():
#     user = User.query.all()
#     tmp = map(lambda x: x.to_dict(), user)

#     return jsonify({"result":tmp}), 200



