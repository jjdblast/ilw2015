from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Home',
                           active_home=True,
                           active_about_us=False)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

@app.route('/about_us')
def about_us():
    students = ["Theo", "Rafael", "Charlie", "Harri"]
    return render_template("about_us.html",
                           title='About us',
                           students=students,
                           active_home=False,
                           active_about_us=True)
