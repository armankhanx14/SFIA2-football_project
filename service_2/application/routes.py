from application import app
from flask import request, Response
import random

@app.route("/player", methods=["GET"])
def get_player():
<<<<<<< HEAD
    players = ["Henry", "Ozil", "Bergkamp", "Fabregas","Wright","Adams","Carzola"]
=======

    players = ["Henry", "Ozil", "Bergkamp", "Fabregas","Wright"]

>>>>>>> ade1b6e52f5b539d3b1528532612d594bce9a3a7
    return Response(str(random.choice(players)), mimetype='text/plain')

