from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_result(self):
        players = ["Henry", "Ozil", "Bergkamp", "Fabregas"]
        teams = ["Chelsea", "Totenham", "ManchesterUnited", "Liverpool"]
        result = ["Fabregas will score 2 goals", "Fabregas will score 2 goals", "Fabregas will score 2 goals", "Fabregas will score 2 goals",
                "Henry will not score", "Henry will score a hat-trick", "Henry will score a hat-trick", "Henry will score a hat-trick", 
                "Ozil will not score", "Ozil will score a freekick", "Ozil will not score", "Ozil will score a freekick", 
                "Bergkamp will not score", "Bergkamp will not score", "Bergkamp will not score", "Bergkamp will score a tap in"]
        i = 0
        for player in players:
            for team in teams:
                response=self.client.post(url_for("result"), json={"player" : player, "team" : team})
                self.assertIn(response.data.decode(), result)
                i+=1
