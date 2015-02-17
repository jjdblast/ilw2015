from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'nickname': 'Blue man'},
            'body': 'Blah, blah, blah!'
        },
        {
            'author': {'nickname': 'Sarah'},
            'body': 'Yey!'
        },
        {
            'author': {'nickname': 'Hulk'},
            'body': "I'm green!"
        }

    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts,
                           active_home=True,
                           active_about_us=False)

@app.route('/about_us')
def about_us():
    students = ["Theo", "Rafael", "Charlie", "Harri"]
    return render_template("about_us.html",
                           title='Home',
                           students=students,
                           active_home=False,
                           active_about_us=True)