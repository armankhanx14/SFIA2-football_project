from application import app, db
from application.models import Players
import requests
from requests import get
from flask import render_template
from sqlalchemy import desc

@app.route('/', methods=['GET'])
def index():
    player_response = requests.get("http://football_player_backend:5000/player")
    team_response = requests.get("http://football_team_backend:5000/team")
    result_response = requests.post(
        "http://football_result_backend:5000/result", 
        json=dict(player=player_response.text, team=team_response.text))
    
    new_player = Players(name = player_response.text, team = team_response.text, result = result_response.text)
    db.session.add(new_player)
    db.session.commit()

    view_players = Players.query.order_by(desc("id")).limit(5).all()

    return render_template(
        "index.html", 
        player=player_response.text, team=team_response.text, goal=result_response.text, 
        view_players=view_players)
