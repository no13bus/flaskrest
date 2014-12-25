from app import app, login_manager, auth
from flask import render_template, redirect, url_for, flash, jsonify
from forms import LoginForm
from models import User
from flask.ext.login import login_user, login_required, logout_user
from flask.ext.httpauth import HTTPBasicAuth


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

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
    print user
    if user:
        return user.password
    return None

# @auth.hash_password
# def hash_pw(password):
#     return md5(password).hexdigest()


@app.route('/tt')
@auth.login_required
def indextt():
    return "Hello, %s!" % auth.username()

@app.route('/api/v1/test')
@auth.login_required
def test():
    user = User.query.get(1)
    return jsonify(user=user.username, password=user.password)