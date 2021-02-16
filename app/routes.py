from app import app
from flask import render_template, request, flash, redirect, url_for
from app.forms import UsernameForm
from getstats import PlayerStats, TrackerAPI


@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    form = UsernameForm()
    if request.method == 'POST':
        return redirect(url_for('compare'))
    return render_template('index.html', title='Rocket League Stats', form=form)


@app.route('/compare', methods=['GET'])
def compare():
    response1 = TrackerAPI(request.args.get("platform"), request.args.get("username"))
    response2 = TrackerAPI(request.args.get("platform2"), request.args.get("username2"))
    if not response1.response or response2.response:
        if not response1.response:
            flash(f'Error receiving data for {request.args.get("username")}.'
                  f' Please check spelling and platform and try again.')
        if not response2.response:
            flash(f'Error receiving data for {request.args.get("username2")}. '
                  f'Please check spelling and platform and try again.')
        return redirect(url_for('index'))

    user1 = PlayerStats(response1.raw_response_data)
    user2 = PlayerStats(response2.raw_response_data)

    return render_template('compare.html', player1=user1, player2=user2)
