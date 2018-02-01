from . import main
from flask import render_template
from flask_login import login_required


@main.route('/')
@main.route('/index')
@login_required
def index():
    # user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    # return render_template('index.html', title='Home', user=user, posts=posts)
    return render_template("index.html", title='Home Page', posts=posts)



