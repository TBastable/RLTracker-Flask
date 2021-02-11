from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class UsernameForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
