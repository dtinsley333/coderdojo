from flask import render_template
from mysite import mysite

@mysite.route('/')
@mysite.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("index.html",
        title = 'Home',
        user = user)