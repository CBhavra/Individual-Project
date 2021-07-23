from . import db 

class Stats(db.Model):
    stats_id = db.Column(db.Integer, nullable=False, primary_key=True)
    runs = db.Column(db.Integer, nullable=False)
    wickets = db.Column(db.Integer, nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.players_id'), nullable=False)
    
class Players(db.Model):
    players_id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    rating = db.Column(db.Integer, nullable=False) 
    team_id = db.Column(db.String(50), db.ForeignKey('team.teams_id'), nullable=False) 
    stats = db.relationship('Stats', backref='players')

class Team(db.Model):
    teams_id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    league = db.Column(db.String(50), nullable=False)
    players = db.relationship('Players', backref='team')

    
    
   
