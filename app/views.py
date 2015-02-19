from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    available_dates = ["09-02-15",
                       "10-02-15",
                       "11-02-15",
                       "12-02-15",
                       "13-02-15",
                       "14-02-15",
                       "15-02-15",
                       "16-02-15",
                       "17-02-15",
                       "19-02-15"]
    return render_template("index.html",
                           title='Home',
                           available_dates=available_dates,
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
    students = ["Theo Pavlakou", "Rafael Karampatsis", "Charlie Nash", "Harri Edwards"]
    return render_template("about_us.html",
                           title='About us',
                           students=students,
                           active_home=False,
                           active_about_us=True)
