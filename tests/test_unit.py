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
        team1 = Team(name='Birmingham bears', country= 'England', league= 'international')
        db.session.add(team1)    
    
        db.session.commit()

    def tearDown(self):
        db.drop_all()

class TestViews(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)

    def test_create(self):
        response = self.client.get(url_for('create'))
        self.assert200(response)

    def test_update(self):
        response = self.client.get(url_for('update', id=1))
        self.assert200(response)

    
class TestRead(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))
        
        assert 'Birmingham bears' in response.data.decode()
        assert 'England' in response.data.decode()
        assert 'international' in response.data.decode() 

class TestCreate(TestBase):
    def test_create(self):
        response = self.client.post(
            url_for('create'),
            data={'name': 'Add a team name'},
            follow_redirects=True

        )

        assert 'Add a team name' in response.data.decode()
        
class TestUpdate(TestBase):
    def test_update(self):
        response = self.client.post(
            url_for('update', id=1),
            data={'name': 'Add a team name'},
            follow_redirects=True

        )       

        assert 'Add a team name' in response.data.decode()
        assert 'Add a team name' in response.data.decode()
        assert 'Run unit tests' not in response.data.decode()

class TestDelete(TestBase):
    def test_delete(self):
        response = self.client.get(
            url_for('delete', id=1),
            follow_redirects=True
        )
        
        assert '' in response.data.decode()
        assert 'Run unit tests' not in response.data.decode()