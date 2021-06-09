from application import app
from flask import request, Response
import random

@app.route("/team", methods=["GET"])
def get_team():
    teams = ["Arsenal", "Chelsea", "Fulham", "Liverpool"]
    return Response(str(random.choice(teams)), mimetype='text/plain')


