import numpy as np
import pandas as pd

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

df = deliveries.merge(matches, left_on = 'match_id', right_on = "id")

all_teams = sorted(set((list(df['team1'].unique()) + list(df["team2"].unique()))))


def teams():
    return {"allTeams": all_teams}


def teamVsTeam(t1, t2):
    if t1 in all_teams and t2 in all_teams:
        teams_df = df[((df["team1"] == t1) & (df["team2"] == t2)) | ((df["team1"] == t2) & (df["team2"] == t1))]

        totalMatches = teams_df.shape[0]
        matchesWonTeam1 = teams_df["winner"].value_counts().get(t1, 0)
        matchesWonTeam2 = teams_df["winner"].value_counts().get(t2, 0)
        draws = totalMatches - (matchesWonTeam1 + matchesWonTeam2)

        return {
            "totalMatches": str(totalMatches),
            "matchesWonTeam1": str(matchesWonTeam1),
            "matchesWonTeam2": str(matchesWonTeam2),
            "draws": str(draws)
        }
    else:
        return {
            "error": "Invalid team name/s",
            "validTeams": all_teams
        }


def teamRecord(t):
    if t in all_teams:
        totalMatches = df[(df["team1"] == t) | (df["team2"] == t)].shape[0]
        matchesWon = df[((df["team1"] == t) | (df["team2"] == t)) & (df["winner"] == t)].shape[0]
        matchesLost = df[((df["team1"] == t) | (df["team2"] == t)) & (df["winner"] != t)].shape[0]
        draws = totalMatches - (matchesWon + matchesLost)

        return {
            "overall": {
                "totalMatches": totalMatches,
                "matchesWon": matchesWon,
                "matchesLost": matchesLost,
                "draws": draws
            },
            "against": {team2: teamVsTeam(t, team2) for team2 in [i for i in all_teams if i != t]}
        }
    else:
        return {
            "error": "Invalid team name/s",
            "validTeams": all_teams
        }
