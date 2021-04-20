from view import menu
from view import players as Players
from controller import player as Player

def main():
    menu.main()
    option = int(input("\n\nOption : "))
    while option != 0:
        if option == 1:
            player()
            break
        elif option == 2:
            tournament()
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
            Player.add(int(input("\n\nNumber of players: ")))
            break
        elif option == 2:
            Players.view_text()
            Players.view_html()
            break
        elif option == 3:
            print("\n\n Remove by:\n\n   [1] ID\n   [2] Name\n   [3] All Players\n   [4] Exit ↵")
            delete_option = int(input("\n\nOption Number: "))
            while delete_option != 0:
                if delete_option == 1:
                    Player.remove_id()
                    break
                elif delete_option == 2:
                    Player.remove_name()
                    break
                elif delete_option == 3:
                    Player.remove_all()
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
    
def tournament():
    menu.tournament()
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

