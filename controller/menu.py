from os import remove
from view import menu
from view import players as player_view
from view import rounds as round_view
from controller import player as player_controller
from controller import rounds as round_controller
from controller import tournament as tournament_controller
from controller import reports as report
from controller import clear as clr
from controller import tools


class MenuController():

    def main():
        menu.ViewMenu.main()
        option = tools.int_input('option')
        while option != 0:
            if option == 1:
                clr.screen()
                MenuController.player()
                break
            elif option == 2:
                clr.screen()
                MenuController.tournament()
                break
            elif option == 3:
                clr.screen()
                MenuController.reports()
                break
            elif option == 4:
                clr.screen()
                print("""
                Thank you, Have a GREAT day!
                """)
                quit()
            else:
                tools.check_range(option, 1-4)
                MenuController.main()

                break


    def player():
        menu.ViewMenu.player()
        option = tools.int_input('option')
        while option != 0:
            if option == 1:
                clr.screen()
                player_controller.PlayerController.add(8)
                break
            elif option == 2:
                clr.screen()
                menu.ViewMenu.remove_players()
                delete_option = tools.int_input('delete_option')
                while delete_option != 0:
                    if delete_option == 1:
                        clr.screen()
                        player_controller.PlayerController.remove_id()
                        break
                    elif delete_option == 2:
                        clr.screen()
                        player_controller.PlayerController.remove_name()
                        break
                    elif delete_option == 3:
                        clr.screen()
                        player_controller.PlayerController.remove_all()
                        break
                    elif delete_option == 4:
                        clr.screen()
                        quit()
                        break
                    else:
                        tools.check_range(option, 1-4)
                        menu.ViewMenu.player()
                        break
<<<<<<< HEAD
            elif option == 3:
=======
<<<<<<< HEAD
            elif option == 3:
=======
            elif option == 4:
>>>>>>> eee33165c0f3dd4fd90481e4588bb874ad45d935
>>>>>>> d84b8a5125f2695ca4f98c5b32b1434d012ce24b
                clr.screen()
                print("""
                Thank you, Have a GREAT day!
                """)
                MenuController.main()
                break
            else:
                tools.check_range(option, 1-3)
                MenuController.player()
                break
        

    def tournament():
        menu.ViewMenu.tournament()
        option = tools.int_input('option')
        while option != 0:
            if option == 1:
                # Start New Tournament
                clr.screen()
                tournament_controller.TournamentController.new_tournament()
                break
            elif option == 2:
                clr.screen()
                menu.ViewMenu.remove_tournament()
                delete_option = tools.int_input('delete_option')
                while delete_option != 0:
                    if delete_option == 1:
                        clr.screen()
                        tournament_controller.TournamentController.remove_id()
                        break
                    elif delete_option == 2:
                        clr.screen()
                        tournament_controller.TournamentController.remove_name()
                        break
                    elif delete_option == 3:
                        clr.screen()
                        tournament_controller.TournamentController.remove_all()
                        break
                    elif delete_option == 4:
                        clr.screen()
                        quit()
                        break
                    else:
                        clr.screen()
                        print('Invalid Number')
                        menu.player()
                        break
                break
            elif option == 3:
                # return to main menu
                clr.screen()
                MenuController.main() 
                break
            else:
                clr.screen()
                print('Invalid Number')
                MenuController.main()
                break
        
    def reports():
        menu.ViewMenu.reports()
        option = tools.int_input('option')
        while option != 0:
            if option == 1:
                menu.ViewMenu.players_reports()
                players_reports_option = tools.int_input('players_reports_option')
                if players_reports_option == 1:
                    report.ReportsController.players_latest_report()
                    print("\nOn Windows You can view the html version by typing: \nstart view/tables/last_players.html")
                    quit()
                elif players_reports_option == 2:
                    report.ReportsController.players_all_reports()
                    print("\nOn Windows You can view the html version by typing: \nstart view/tables/players.html")
                    quit()
                else:
                    clr.screen()
                    MenuController.main()
            elif option == 2:
                menu.ViewMenu.tournament_reports()
                tournaments_reports_option = tools.int_input('tournaments_reports_option')
                if tournaments_reports_option == 1:
                    report.ReportsController.tournament_latest_report()
                    print("On Windows You can view the html version by typing: \nstart view/tables/last_tournament.html")
                    quit()
                elif tournaments_reports_option == 2:
                    report.ReportsController.tournament_all_reports()
                    print("On Windows You can view the html version by typing: \nstart view/tables/tournaments.html")
                    quit()
                else:
                    clr.screen()
                    MenuController.main()
            elif option == 3:
                clr.screen()
                MenuController.main()
            elif option == 4:
                clr.screen()
                print("""
                Thank you, Have a GREAT day!
                """)
                quit()
            else:
                tools.check_range(option, 1-4)
                print('Invalid Number')
                break

