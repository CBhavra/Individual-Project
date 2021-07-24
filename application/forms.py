from application.models import Team
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from . import models

class Teamsform(FlaskForm):
    name = StringField('Add a team name')
    country = StringField('Add a country')
    league = StringField('Add a league')
    submit = SubmitField('Submit')

class Playersform(FlaskForm):
    name = StringField('Add a player name')
    rating = StringField('What is the player rating?')
    team_id = IntegerField('What is the team id?')
    submit = SubmitField('Submit')

class Statsform(FlaskForm):
    description = StringField('Add a statistic')
    submit = SubmitField('Submit')