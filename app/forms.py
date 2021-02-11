from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class UsernameForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    username2 = StringField('Username2: ', validators=[DataRequired()])
    platform = SelectField('Platform', choices=["Xbox", "Steam", "Playstation"])
    platform2 = SelectField('Platform2', choices=["Xbox", "Steam", "Playstation"])
    submit = SubmitField('Submit')
