from . import app, db
from flask import redirect, url_for, request, render_template
from .models import Stats 
from .models import Players
from .models import Team
from .forms import Teamsform, Playersform, Statsform

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

@app.route('/players/home')
def home_players():
    players = Players.query.all()

    result = 'My players'
    for player in players:
        result += f'{player.name}  |  {player.rating}\n'.format(player)

    return result


@app.route('/players/create', methods=['GET','POST'])
def create_players():
    form = Playersform()
    
    if form.validate_on_submit():
        new_player = Players(name=form.name.data, rating=form.rating.data, team_id=form.team_id.data)
        db.session.add(new_player)
        db.session.commit()

        return redirect(url_for('home_players'))
    else:
        return render_template('create1.html', form=form)


@app.route('/players/update/<id>', methods=['GET','POST'])
def update_players(id):
    players = Players.query.get(id)
    form = Playersform()
    
    if request.method == 'POST':
        
        players.name = form.name.data
        players.rating = form.rating.data 
        players.team_id = form.team_id.data
        
        
        db.session.commit()

        return redirect(url_for('home_players'))
    else: 
        return render_template('create1.html', form=form)



@app.route('/players/delete/<id>', methods=['GET','POST'])
def delete_players(id):
    players = Players.query.get(id)
    form = Playersform()

    if request.method == 'POST':
        db.session.delete(players)
        db.session.commit()

        return redirect(url_for('home_players'))
    else: 
        return render_template('create1.html', form=form)

# STATISTICS

@app.route('/stats')
def home_stats():
    stats = Stats.query.all()

    result = 'My stats'
    for stat in stats:
        result += f'{stat.description}     {stat.completed}\n'

    return result


@app.route('/stats/create', methods=['GET','POST'])
def create_stats(stat):
    stats = Stats.query.all()
    form = Statsform()
    
    if request.method == 'POST':
        new_stat = Stats(stat=form.stat.data, runs=form.runs.data, wickets=form.wickets.data)
        db.session.add(new_stat)
        db.session.commit()

        return redirect(url_for('home'))
    else: 
        return render_template('create.html', form=form)


@app.route('/stats/update', methods=['GET','POST'])
def update_stats(description, id):
    stat = Stats.query.get(id)
    form = Statsform

    if request.method == 'POST':
        stat.description = description 
        db.session.add(stat=form.stat.data, runs=form.runs.data, wickets=form.wickets.data)
        db.session.commit()

        return redirect(url_for('home'))
    else: 
        return render_template('create.html', form=form)



@app.route('/stats/delete', methods=['GET','POST'])
def delete_stats(id):
    stat = Stats.query.get(id)
    form = Statsform()
    
    if request.method == 'POST':
        db.session.delete(stat=form.stat.data, runs=form.runs.data, wickets=form.wickets.data)
        db.session.commit()

        return redirect(url_for('home'))
    else: 
        return render_template('create.html', form=form)
