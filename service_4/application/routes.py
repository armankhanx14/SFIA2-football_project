from application import app 
from flask import request, Response

@app.route("/result", methods=["POST"])
def result():
    player = request.json["player"]
    team = request.json["team"]
    
    if player == "Rashford":
        message="Rashford will score 4 goals"
    elif player == "Rooney":
        if team == "Liverpool":
            message="Rooney will not score"
        else:
            message="Rooney will score a hat-trick"
    elif player == "Beckham":
        if team == "Arsenal" or team == "Fulham":
            message="Beckham will score a freekick"
        else:
            message="Beckham will not score"
    elif player == "Cole":
        if team == "Fulham":
            message="Cole will score a tap in"
        else:
            message="Cole will not score"       
    return Response(message, mimetype='text/plain')
    

