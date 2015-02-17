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
                           posts=posts)
