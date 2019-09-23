## Module to import FPL data

# Import packages
import numpy as np
import json


def get_fpl_data_all(session):
    response = session.get("https://fantasy.premierleague.com/api/bootstrap-static/")
    return json.loads(response.text)


def get_team_history(session, team_id):
    response = session.get("https://fantasy.premierleague.com/api/entry/"+team_id+"/history/")
    return json.loads(response.text)


## Does not work
def get_team_latest_transfers(session, team_id):
    response = session.get("https://fantasy.premierleague.com/api/entry/"+team_id+"/transfers-latest/")
    return json.loads(response.text)


def get_league_data(session, league_id):
    response = session.get("https://fantasy.premierleague.com/api/leagues-classic/"+league_id+"/standings/")
    return json.loads(response.text)


def get_team_data(session, team_id):
    response = session.get("https://fantasy.premierleague.com/api/entry/"+team_id+"/")
    return json.loads(response.text)

def get_team_name(session, team_id):
    team_data = get_team_data(session, team_id)
    first_name = team_data["player_first_name"]
    last_name = team_data["player_last_name"]
    return first_name + " " + last_name

def get_team_ids(league_data):
    IDs = []
    teams = league_data['standings']['results']
    for team in teams:
        team_id = team['entry']
        IDs.append(team_id)
    return IDs

def get_team_names(league_data):
    names = {}
    teams = league_data['standings']['results']
    for i in range(0, len(teams)):
        name = teams[i]['player_name']
        names[str(i+1)] = name
    return names


def get_podium_teams(league_data):
    names = {}
    teams = league_data['standings']['results']
    for i in range(0, 3):
        name = teams[i]['player_name']
        names[str(i+1)] = name
    return names


def get_highest_score_gw(league_data):
    names = []
    score = 0

    teams = league_data['standings']['results']
    for team in teams:

        score_new = int(team['event_total'])
        if score_new > score:
            score = score_new
            names = []
            names.append(team["player_name"])
        elif score_new == score:
            names.append(team["player_name"])

    return names, score


def get_lowest_score_gw(league_data):
    names = []
    score = np.inf

    teams = league_data['standings']['results']
    for team in teams:

        score_new = int(team['event_total'])
        if score_new < score:
            score = score_new
            names = []
            names.append(team["player_name"])
        elif score_new == score:
            names.append(team["player_name"])

    return names, score


def get_highest_gw_score_overall(session, league_data):
    ids = get_team_ids(league_data)
    names = []
    events = []
    score = 0
    gw = ""
    for id in ids:
        team_hist = get_team_history(session, str(id))
        for event in team_hist['current']:
            score_new = event["points"]
            if score_new >= score:
                gw = event["event"]
                name = get_team_name(session, str(id))
                if score_new > score:
                    names = []
                    events = []
                    score = score_new
                    names.append(name)
                    events.append(gw)
                elif score_new == score:
                    names.append(name)
                    events.append(gw)

    return names, events, score


def get_lowest_gw_score_overall(session, league_data):
    ids = get_team_ids(league_data)
    names = []
    events = []
    score = np.inf
    gw = ""
    for id in ids:
        team_hist = get_team_history(session, str(id))
        for event in team_hist['current']:
            score_new = event["points"]
            if score_new <= score:
                gw = event["event"]
                name = get_team_name(session, str(id))
                if score_new < score:
                    names = []
                    events = []
                    score = score_new
                    names.append(name)
                    events.append(gw)
                elif score_new == score:
                    names.append(name)
                    events.append(gw)

    return names, events, score


def get_highest_climb_gw(league_data):
    names = []
    rank_diff = -np.inf

    teams = league_data['standings']['results']
    for team in teams:

        rank = team["rank"]
        rank_last = team["last_rank"]
        rank_diff_new = int(rank_last) - int(rank)

        if rank_diff_new > rank_diff:
            rank_diff = rank_diff_new
            names = []
            names.append(team["player_name"])
        elif rank_diff_new == rank_diff:
            names.append(team["player_name"])

    if rank_diff == 0:
        names = ["None"]

    return names, rank_diff


def get_highest_score_on_bench_gw(session, league_data):
    ids = get_team_ids(league_data)
    names = []
    score = 0
    for id in ids:
        team_hist = get_team_history(session, str(id))
        event = team_hist["current"][len(team_hist["current"]) - 1]
        score_new = event["points_on_bench"]
        
        if score_new >= score:
            name = get_team_name(session, str(id))
            if score_new > score:
                names = []
                score = score_new
                names.append(name)
            elif score_new == score:
                names.append(name)

    return names, score


def get_highest_acc_score_on_bench(session, league_data):
    ids = get_team_ids(league_data)
    names = []
    score = 0
    for id in ids:
        team_hist = get_team_history(session, str(id))
        events = team_hist["current"]
        score_new = 0
        for event in events:
            score_new += event["points_on_bench"]
            
        if score_new >= score:
            name = get_team_name(session, str(id))
            if score_new > score:
                names = []
                score = score_new
                names.append(name)
            elif score_new == score:
                names.append(name)

    return names, score


def get_most_transfers_gw(session, league_data):
    ids = get_team_ids(league_data)
    names = []
    transfers = 0
    for id in ids:
        team_hist = get_team_history(session, str(id))
        event = team_hist["current"][len(team_hist["current"]) - 1]
        transfers_new = event["event_transfers"]
        
        if transfers_new >= transfers:
            name = get_team_name(session, str(id))
            if transfers_new > transfers:
                names = []
                transfers = transfers_new
                names.append(name)
            elif transfers_new == transfers:
                names.append(name)

    return names, transfers


def get_most_transfers(session, league_data):
    ids = get_team_ids(league_data)
    names = []
    transfers = 0
    for id in ids:
        team_hist = get_team_history(session, str(id))
        events = team_hist["current"]
        transfers_new = 0
        for event in events:
            transfers_new += event["event_transfers"]
            
        if transfers_new >= transfers:
            name = get_team_name(session, str(id))
            if transfers_new > transfers:
                names = []
                transfers = transfers_new
                names.append(name)
            elif transfers_new == transfers:
                names.append(name)

    return names, transfers


def get_highest_asset_value_team(session, league_data):
    ids = get_team_ids(league_data)
    names = []
    value = 0
    for id in ids:
        team_hist = get_team_history(session, str(id))
        event = team_hist["current"][len(team_hist["current"]) - 1]
        bank = int(event["bank"])
        team_value = int(event["value"])
        value_new = bank + team_value
        
        if value_new >= value:
            name = get_team_name(session, str(id))
            if value_new > value:
                names = []
                value = value_new
                names.append(name)
            elif value_new == value:
                names.append(name)

    return names, value/10


def get_highest_bank_value_team(session, league_data):
    ids = get_team_ids(league_data)
    names = []
    value = 0
    for id in ids:
        team_hist = get_team_history(session, str(id))
        event = team_hist["current"][len(team_hist["current"]) - 1]
        value_new = int(event["bank"])
        
        if value_new >= value:
            name = get_team_name(session, str(id))
            if value_new > value:
                names = []
                value = value_new
                names.append(name)
            elif value_new == value:
                names.append(name)

    return names, value/10


def get_current_gw_number(session):
    fpl_data = get_fpl_data_all(session)
    for gw in fpl_data["events"]:
        if gw["is_current"]:
            return gw["name"]

