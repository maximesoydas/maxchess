from os import remove
from view import menu
from view import players as player_view
from view import rounds as round_view
from controller import player as player_controller
from controller import rounds as round_controller
from controller import tournament as tournament_controller
from controller import reports as report
from controller import clear as clr


class Menu:
        
    def main():
        clr.screen()
        menu.main()
        option = int(input("\n\nOption : "))
        while option != 0:
            if option == 1:
                clr.screen()
                player()
                break
            elif option == 2:
                clr.screen()
                tournament()
                break
            elif option == 3:
                clr.screen()
                reports()
                break
            elif option == 4:
                clr.screen()
                print("""
                Thank you, Have a GREAT day!
                """)
                quit()
            else:
                clr.screen()
                print('Invalid Number')
                menu.main()
                break


    def player():
        menu.player()
        option = int(input("\n\nOption : "))
        while option != 0:
            if option == 1:
                clr.screen()
                player_controller.add(8)
                break
            elif option == 2:
                clr.screen()
                menu.remove_players()
                delete_option = int(input("\n\nOption Number: "))
                while delete_option != 0:
                    if delete_option == 1:
                        clr.screen()
                        player_controller.remove_id()
                        break
                    elif delete_option == 2:
                        clr.screen()
                        player_controller.remove_name()
                        break
                    elif delete_option == 3:
                        clr.screen()
                        player_controller.remove_all()
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
            elif option == 3:
                clr.screen()
                print("""
                Thank you, Have a GREAT day!
                """)
                main()
                break
            else:
                clr.screen()
                print('Invalid Number')
                menu.player()
                break
        

    def tournament():
        menu.tournament()
        tournament_option = int(input("\n\nOption : "))
        while tournament_option != 0:
            if tournament_option == 1:
                # Start New Tournament
                clr.screen()
                tournament_controller.new_tournament()
                break
            elif tournament_option == 2:
                clr.screen()
                menu.remove_tournament()
                delete_option = int(input("\n\nOption Number: "))
                while delete_option != 0:
                    if delete_option == 1:
                        clr.screen()
                        tournament_controller.remove_id()
                        break
                    elif delete_option == 2:
                        clr.screen()
                        tournament_controller.remove_name()
                        break
                    elif delete_option == 3:
                        clr.screen()
                        tournament_controller.remove_all()
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
            elif tournament_option == 3:
                # return to main menu
                clr.screen()
                main() 
                break
            else:
                clr.screen()
                print('Invalid Number')
                main()
                break
        
    def reports():
        menu.reports()
        option = int(input("\n\nOption : "))
        while option != 0:
            if option == 1:
                menu.players_reports()
                players_reports_option = int(input("\n\nOption : "))
                if players_reports_option == 1:
                    report.players_latest_report()
                    print("\nOn Windows You can view the html version by typing: \nstart view/tables/last_players.html")
                    quit()
                elif players_reports_option == 2:
                    report.players_all_reports()
                    print("\nOn Windows You can view the html version by typing: \nstart view/tables/players.html")
                    quit()
                else:
                    clr.screen()
                    main()
            elif option == 2:
                menu.tournament_reports()
                tournaments_reports_option = int(input("\n\nOption : "))
                if tournaments_reports_option == 1:
                    report.tournament_latest_report()
                    print("On Windows You can view the html version by typing: \nstart view/tables/last_tournament.html")
                    quit()
                elif tournaments_reports_option == 2:
                    report.tournament_all_reports()
                    print("On Windows You can view the html version by typing: \nstart view/tables/tournaments.html")
                    quit()
                else:
                    clr.screen()
                    main()
            elif option == 3:
                clr.screen()
                main()
            elif option == 4:
                clr.screen()
                print("""
                Thank you, Have a GREAT day!
                """)
                quit()
            else:
                print('Invalid Number')
                break

