from view import players as player_view
from view import last_players as last_player_view
from view import tournament as tournament_view
from view import last_tournament as last_tournament_view




def players_latest_report():
    """ 
    Returns the latest players list in console and web view
    """
    last_player_view.view_text()
    last_player_view.view_html() 


def players_all_reports():
    """ 
    Returns the all players list in console and web view
    """
    print('all players view')
    player_view.view_text()
    player_view.view_html()

def tournament_latest_report():
    """ 
    Returns the last round(4) of latest tournament list in console and web view
    """
    print("this is the latest tournament")
    last_tournament_view.view_text()
    last_tournament_view.view_html()

def tournament_all_reports():
    """ 
    Returns the last round(4) of all tournaments list in console and web view
    """
    tournament_view.view_text()
    tournament_view.view_html()