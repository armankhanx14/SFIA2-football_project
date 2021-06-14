from application import app
from flask import request, Response
import random

@app.route("/player", methods=["GET"])
def get_player():

    players = ["Henry", "Ozil", "Bergkamp", "Fabregas","Wright"]

    return Response(str(random.choice(players)), mimetype='text/plain')

