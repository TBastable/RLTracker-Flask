from app import app
from flask import render_template, request, flash, Flask
from app.forms import UsernameForm



@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    form = UsernameForm()
    if request.method == 'POST':
        username = request.form['username']
        username2 = request.form['username2']
        print(username)


    # if form.validate():
    #     player_stats = ukf_wonderboy.generate_response("UKF%20WONDERBOY", "xbl")


    return render_template('index.html', form=form)
