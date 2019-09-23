## Import modules
import src.stats as stats

## Import packages
from pprint import pprint

def gen_report(session, league_id):

    ## Get league data as JSON
    league_data = stats.get_league_data(session, league_id)
    current_gw = stats.get_current_gw_number(session)
    
    ## Get podium teams as dict
    podium_teams = stats.get_podium_teams(league_data)

    ## Get teams with highest score in gw
    highest_score_gw_names, highest_score_gw = stats.get_highest_score_gw(league_data)

    ## Get teams with lowest score in gw
    lowest_score_gw_names, lowest_score_gw = stats.get_lowest_score_gw(league_data)

    ## Get teams with highest gw score overall
    highest_score_gw_overall_names, highest_score_gw_overall_events, highest_score_gw_overall = stats.get_highest_gw_score_overall(session, league_data)
    
    ## Get teams with lowest gw score overall
    lowest_score_gw_overall_names, lowest_score_gw_overall_events, lowest_score_gw_overall = stats.get_lowest_gw_score_overall(session, league_data)
    
    ## Get teams with highest climb in gw
    climb_names, rank_diff = stats.get_highest_climb_gw(league_data)

    ## Get teams with highest score on bench in gw
    bench_score_names, bench_score = stats.get_highest_score_on_bench_gw(session, league_data)

    ## Get teams with highest accumulated score in bench
    bench_score_acc_names, bench_acc_score = stats.get_highest_acc_score_on_bench(session, league_data)

    ## Get teams with most transfers in gw
    transfers_gw_names, tranfers_gw = stats.get_most_transfers_gw(session, league_data)

    ## Get teams with most transfers
    transfers_names, tranfers = stats.get_most_transfers(session, league_data)

    ## Get teams with highest asset value
    asset_value_names, asset_value = stats.get_highest_asset_value_team(session, league_data)

    ## Get teams with highest bank account value
    bank_value_names, bank_value = stats.get_highest_bank_value_team(session, league_data)

    #### Generate report #####

    report = ''' 
            FPL report after {0}

            Podium teams:
            1) {1}
            2) {2}
            3) {3}

            Team[s] with highest score:
            {4} with {5} points

            Team[s] with lowest score:
            {6} with {7} points

            Team[s] with highest GW score overall:
            {8} with {9} points in GW {10}

            Team[s] with lowest GW score overall:
            {11} with {12} points in GW {13}

            Team[s] with highest climb in current GW:
            {14} with {15} place[s]

            Team[s] with most points on the bench:
            {16} with {17} points

            Team[s] with the most accumulated points on the bench:
            {18} with {19} points

            Team[s] with most transfers in GW:
            {20} with {21} transfers

            Team[s] with most transfers overall:
            {22} with {23} transfers

            Team[s] with the highest asset value:
            {24} with £{25}

            Team[s] with the most value in bank:
            {26} with £{27}

    '''.format(current_gw, podium_teams.get("1"), podium_teams.get("2"), podium_teams.get("3"), \
                    highest_score_gw_names, highest_score_gw, \
                    lowest_score_gw_names, lowest_score_gw, \
                    highest_score_gw_overall_names, highest_score_gw_overall, highest_score_gw_overall_events, \
                    lowest_score_gw_overall_names, lowest_score_gw_overall, lowest_score_gw_overall_events, \
                    climb_names, rank_diff, \
                    bench_score_names, bench_score, \
                    bench_score_acc_names, bench_acc_score, \
                    transfers_gw_names, tranfers_gw, \
                    transfers_names, tranfers, \
                    asset_value_names, asset_value, \
                    bank_value_names, bank_value
                    )

    print(report)
    return None