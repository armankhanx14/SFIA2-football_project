from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock 

from application import app, db
from application.models import Players

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///data.db")
        return app
    
    def setUp(self):
        db.create_all()
        db.session.add(Players(name="Fabregas", team="Liverpool", result="Faberegas will score"))
        db.session.commit()

    def tearDown(self):
        db.drop_all()
        db.session.remove()

class TestResponse(TestBase):
    def test_index(self):
        with requests_mock.mock() as m:
            m.get("http://football_player_backend:5000/player", text='Henry')
            m.get("http://football_team_backend:5000/team", text='Chelsea')
            m.post("http://football_result_backend:5000/result", text='Henry will score')
            response = self.client.get(url_for('index'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Henry will score', response.data)
