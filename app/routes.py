from app import app
from flask import render_template, request, flash, Flask, redirect, url_for
from app.forms import UsernameForm
from getstats import PlayerStats


@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    form = UsernameForm()
    if request.method == 'POST':
            return redirect(url_for('compare'))
    return render_template('index.html', title='Rocket League Stats', form=form)


@app.route('/compare', methods=['GET'])
def compare():
    user1 = str.replace(request.args.get("username")," ","%20")
    user2 = str.replace(request.args.get("username2")," ","%20")
    platform1 = request.args.get("platform")
    platform2 = request.args.get("platform2")

    account1 = PlayerStats()
    player_stats1 = account1.generate_response(user1, platform1)
    account1.extract_player_stats_from_response(player_stats1)
    account2 = PlayerStats()
    player_stats2 = account1.generate_response(user2, platform2)
    account2.extract_player_stats_from_response(player_stats2)

    return render_template('compare.html', player1=account1, player2=account2)


