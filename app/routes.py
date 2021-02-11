from app import app
from flask import render_template, request, flash, Flask
from app.forms import UsernameForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    form = UsernameForm()
    if request.method == 'POST':
        username = request.form['username']
        print(username)

    if form.validate():
        flash('Hello ' + username)
    else:
        flash('Please ensure all fields are filled')

    return render_template('index.html', form=form)