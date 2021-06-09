from application import app
from flask import request, Response
import random

@app.route("/player", methods=["GET"])
def get_player():
    players = ["Rooney", "Beckham", "Cole", "Rashford"]
    return Response(str(random.choice(players)), mimetype='text/plain')

