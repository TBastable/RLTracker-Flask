from app import app
from flask import render_template, request, flash, redirect, url_for
from app.forms import UsernameForm
from getstats import PlayerStats, TrackerAPI
import requests


@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    form = UsernameForm()
    if request.method == 'POST':
        return redirect(url_for('compare'))
    return render_template('index.html', title='Rocket League Stats', form=form)


def get_user_profile_with_flash_error(username, platform):
    try:
        return TrackerAPI.get_user_profile_data(platform, username)
    except requests.exceptions.HTTPError:
        flash(f'Error receiving data for {username}. '
              f'Please check spelling and platform and try again.')
        return redirect(url_for('index'))


@app.route('/compare', methods=['GET'])
def compare():
    username_1 = request.args.get("username")
    username_1_platform = request.args.get("platform")
    user_1_profile_data = get_user_profile_with_flash_error(platform=username_1_platform, username=username_1)

    username_2 = request.args.get("username2")
    username_2_platform = request.args.get("platform2")
    user_2_profile_data = get_user_profile_with_flash_error(platform=username_2_platform, username=username_2)

    user_1_stats = PlayerStats(user_1_profile_data)
    user_2_stats = PlayerStats(user_2_profile_data)

    return render_template('compare.html', player1=user_1_stats, player2=user_2_stats)
