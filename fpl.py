from src import report, api

## Params
sunday_league = "520415" # League ID
kollektivet = "623549"

def fpl(league_id):

    ## Create session
    session = api.create_session()

    report.gen_report(session, league_id)


fpl(kollektivet)