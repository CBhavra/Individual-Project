from os import name
from sqlalchemy.orm import session
from flask_testing import TestCase
from flask import url_for

from application import db, app 
from application.models import Team
from application.models import Players
from application.models import Stats

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///test.db'
        )
        return app

    def setUp(self):
        db.create_all()
        team1 = Team(name='Man United', country= 'England', league= 'international')
        db.session.add(team1)    
    
        db.session.commit()

    def tearDown(self):
        db.drop_all()

class TestRead(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))
        
        assert 'Man United' in response.data.decode()
        assert 'England' in response.data.decode()
        assert 'international' in response.data.decode() 
