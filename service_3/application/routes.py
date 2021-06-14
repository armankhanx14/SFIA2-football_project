from application import app
from flask import request, Response
import random

@app.route("/team", methods=["GET"])
def get_team():
<<<<<<< HEAD
    teams = ["Chelsea", "Totenham", "ManchesterUnited", "Liverpool","West-Ham","Fulham","Leeds"]
=======
    teams = ["Chelsea", "Totenham", "ManchesterUnited", "Liverpool","West-Ham"]

>>>>>>> ade1b6e52f5b539d3b1528532612d594bce9a3a7
    return Response(str(random.choice(teams)), mimetype='text/plain')


