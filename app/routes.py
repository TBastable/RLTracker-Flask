from app import app
from flask import render_template, request, flash, Flask, redirect, url_for
from app.forms import UsernameForm
from getstats import PlayerStats


@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    form = UsernameForm()
    if form.validate_on_submit():
            username = request.form['username']
            username2 = request.form['username2']
            platform = request.form['platform']
            platform2 = request.form['platform2']
            return redirect(url_for(compare(username, platform, username2, platform2)))
    return render_template('index.html', title='Rocket League Stats', form=form)


@app.route('/compare', methods=['GET', 'POST'])
def compare(user1, platform1, user2, platform2):
    user1 = str.replace(user1, " ", "%20")
    print(user1)
    return render_template('compare.html')
