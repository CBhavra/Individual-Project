from . import app, db
from flask import redirect, url_for, request, render_template
from application.models import Stats 
from application.models import Players
from application.models import Team
from application.forms import Teamsform, Playersform, Statsform

# TEAMS

@app.route('/home')
def home():
    teams = Team.query.all()

    result = 'My teams: '
    for team in teams:
        result += f'{team.name}  |  {team.country}  |   {team.league}\n'.format(team)

    return result


@app.route('/create', methods=['GET','POST'])
def create():
    form = Teamsform()
    
    if request.method == 'POST':
        new_team = Team(name=form.name.data, country=form.country.data, league=form.league.data)
        db.session.add(new_team)
        db.session.commit()

        return redirect(url_for('home'))
    else:
        return render_template('create.html', form=form) 
        
    

@app.route('/update/<id>', methods=['GET','POST'])
def update(id):
    teams = Team.query.get(id)
    form = Teamsform()
    
    if request.method == 'POST':
        
        teams.name = form.name.data
        teams.country = form.country.data
        teams.league = form.league.data
        
        db.session.add(teams)
        db.session.commit()

        return redirect(url_for('home'))
    else: 
        return render_template('create.html', form=form)


@app.route('/delete/<id>', methods=['GET','POST'])
def delete(id):
    teams = Team.query.get(id)
    form = Teamsform()
    
  
    db.session.delete(teams)
    db.session.commit()

    return redirect(url_for('home'))
    
# PLAYERS

@app.route('/home/players')
def homeplayers():
    playas = Players.query.all()

    result = 'My players:  '
    for player in playas:
        result += f'{player.name}  |  {player.rating}  |  {player.team_id}\n'.format(player)

    return result


@app.route('/create/players', methods=['GET','POST'])
def create_players():
    form = Playersform()
    
    if form.validate_on_submit():
        new_player = Players(name=form.name.data, rating=form.rating.data, team_id=form.team_id.data)
        db.session.add(new_player)
        db.session.commit()

        return redirect(url_for('homeplayers'))
    else:
        return render_template('create1.html', form=form)


@app.route('/update/players/<id>', methods=['GET','POST'])
def update_players(id):
    playas = Players.query.get(id)
    form = Playersform()
    
    if request.method == 'POST':
        
        playas.name = form.name.data
        playas.rating = form.rating.data 
        playas.team_id = form.team_id.data
        
        
        db.session.commit()

        return redirect(url_for('homeplayers'))
    else: 
        return render_template('create1.html', form=form)



@app.route('/delete/players/<id>', methods=['GET','POST'])
def delete_players(id):
    playas = Players.query.get(id)
    form = Playersform()

    if request.method == 'POST':
        db.session.delete(playas)
        db.session.commit()

        return redirect(url_for('homeplayers'))
    else: 
        return render_template('create1.html', form=form)

