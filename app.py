from flask import Flask, render_template, jsonify, request
import ipl

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api-allTeams")
def all_teams():
    return jsonify(ipl.teams())


@app.route("/api-teamVsTeam")
def teamVsTeam():
    team1 = request.args.get("team1")
    team2 = request.args.get("team2")
    return jsonify(ipl.teamVsTeam(team1, team2))


@app.route("/api-teamRecord")
def teamRecord():
    team = request.args.get("team")
    return jsonify(ipl.teamRecord(team))


app.run(debug=True)