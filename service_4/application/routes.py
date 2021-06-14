from application import app 
from flask import request, Response

@app.route("/result", methods=["POST"])
def result():
    player = request.json["player"]
    team = request.json["team"]
    
    if player == "Fabregas":
        message="Fabregas will score 2 goals"
    elif player == "Henry":
        if team == "Liverpool":
            message="Henry will not score"
        else:
            message="Henry will score a hat-trick"
    elif player == "Ozil":
        if team == "Chelsea" or team == "ManchesterUnited":
            message="Ozil will score a freekick"
        else:
            message="Ozil will not score"
    elif player == "Bergkamp":
        if team == "ManchesterUnited":
            message="Bergkamp will score a tap in"
        else:
            message="Bergkamp will not score"
    elif player == "Wright":
        if team == "West-Ham":
            message="Wright will score a tap in"
        else:
            message="Wright will not score"       
    return Response(message, mimetype='text/plain')
