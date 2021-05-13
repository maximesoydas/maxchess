from view import menu
from view import players as player_view
from view import rounds as round_view
from controller import player as player_controller
from controller import rounds as round_controller


#class Menu:
def main():
    menu.main()
    option = int(input("\n\nOption : "))
    while option != 0:
        if option == 1:
            player()
            break
        elif option == 2:
            rounds()
            break
        elif option == 3:
            reports()
            break
        elif option == 4:
            print("""
            Thank you, Have a GREAT day!
            """)
            quit()
        else:
            print('Invalid Number')
            menu.main()
            break


def player():
    menu.player()
    option = int(input("\n\nOption : "))
    while option != 0:
        if option == 1:
            player_controller.add(int(input("\n\nNumber of players: ")))
            break
        elif option == 2:
            player_view.view_text()
            player_view.view_html()
            break
        elif option == 3:
            print("\n\n Remove by:\n\n   [1] ID\n   [2] Name\n   [3] All Players\n   [4] Exit ↵")
            delete_option = int(input("\n\nOption Number: "))
            while delete_option != 0:
                if delete_option == 1:
                    player_controller.remove_id()
                    break
                elif delete_option == 2:
                    player_controller.remove_name()
                    break
                elif delete_option == 3:
                    player_controller.remove_all()
                    break
                elif delete_option == 4:
                    quit()
                    break
                else:
                    print('Invalid Number')
                    menu.player()
                    break
        elif option == 4:
            print("""
            Thank you, Have a GREAT day!
            """)
            main()
            break
        else:
            print('Invalid Number')
            menu.player()
            break
    
def rounds():
    menu.round()
    round_option = int(input("\n\nOption : "))
    while round_option != 0:
        if round_option == 1:
            # Start First Round
            round_controller.add_first_round()
            # round_view.view_text()
            break
        elif round_option == 2:
            #View Rounds
            round_view.view_text()
            round_view.view_html()
            break
        elif round_option == 3:
            #Delete Rounds Table
            round_controller.remove_all()  
            break
            
        elif round_option == 4:
            main.menu()
            quit()
            break
        else:
            print('Invalid Number')
            break

    
def reports():
    menu.reports()
    option = int(input("\n\nOption : "))
    while option != 0:
        if option == 1:
            player_menu()
        elif option == 2:
            tournament_menu()
        elif option == 3:
            main()
        elif option == 4:
            print("""
            Thank you, Have a GREAT day!
            """)
            quit()
        else:
            print('Invalid Number')
            break

