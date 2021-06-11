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
        result = [b"Fabregas will score 2 goals", b"Fabregas will score 2 goals", b"Fabregas will score 2 goals", b"Fabregas will score 4 goals",
                b"Henry will not score", b"Henry will score a hat-trick", b"Henry will score a hat-trick", b"Henry will score a hat-trick", 
                b"Ozil will not score", b"Ozil will score a freekick", b"Ozil will not score", b"Ozil will score a freekick", 
                b"Bergkamp will not score", b"Bergkamp will not score", b"Bergkamp will not score", b"Bergkamp will score a tap in"]
        i = 0
        for player in players:
            for team in teams:
                response=self.client.post(url_for("result"), json={"player" : player, "team" : team})
                self.assertEqual(response.data, result[i])
                i+=1
