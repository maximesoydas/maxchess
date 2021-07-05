from view import players as player_view
from view import last_players as last_player_view
from view import tournament as tournament_view
from view import last_tournament as last_tournament_view
import os
import platform

class ReportsController():
        
    def players_latest_report():
        """ 
        Returns the latest players list in console and web view
        """
        os_name = platform.system()
        last_player_view.LastPlayers.view_text()
        if os_name == "Linux":
            last_player_view.LastPlayers.view_html() 
        elif os_name == "Darwin":
            last_player_view.LastPlayers.view_html() 
        else:
            pass



    def players_all_reports():
        """ 
        Returns the all players list in console and web view
        """

        player_view.AllPlayers.view_text()
        os_name = platform.system()
        if os_name == "Linux":
            player_view.AllPlayers.view_html()
        elif os_name == "Darwin":
            player_view.AllPlayers.view_html()
        else:
            pass


    def tournament_latest_report():
        """ 
        Returns the last round(4) of latest tournament list in console and web view
        """

        os_name = platform.system()
        last_tournament_view.LastTournament.view_text()
        if os_name == "Linux":
            last_tournament_view.LastTournament.view_html()
        elif os_name == "Darwin":
            last_tournament_view.LastTournament.view_html()
        else:
            pass


    def tournament_all_reports():
        """ 
        Returns the last round(4) of all tournaments list in console and web view
        """
        os_name = platform.system()
        tournament_view.AllTournaments.view_text()
        if os_name == "Linux":
            tournament_view.AllTournaments.view_html()
        elif os_name == "Darwin":
            tournament_view.AllTournaments.view_html()
        else:
            pass