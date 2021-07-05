from model import player as model
from model import players_list as player_model
from tinydb import TinyDB, Query, where
from controller import clear as clr
from view import menu
from operator import *
from controller import tools

# input int  while ok int

class PlayerController():
        
    def add(n=1):
        '''
        Add Player
        '''
        for i in range (n):
            print(f"\nPlease Add Player {i+1}")
            model.Player(
                name= tools.str_input('name'),
                surname=tools.str_input('surname'),
                birthday=tools.date_input('birthday'),
                gender=input("\nEnter Player Gender: "),
                rank=int(input("\nEnter Player Rank: ")),
            ).save()
            clr.screen()
            print(f'Player {i+1} Added Successfully !')
        db = TinyDB('maxchess_db.json')
        TinyDB.default_table_name = 'players'
        players_list = db.search(where('rank') > -1)
        players_list.sort(key=itemgetter('rank'), reverse=True)
        list_name=input("\nEnter Player_List Name: ")
        player_model.Players_list(
            list_name=list_name,
            players=players_list,
        ).save()
        db = TinyDB('maxchess_db.json')
        TinyDB.default_table_name = 'players'
        db.drop_table('players')
        return list_name

    def remove_name():
        """
        Remove players list by players list name
        """
        db = TinyDB('maxchess_db.json')
        q = Query()
        TinyDB.default_table_name = 'players_lists'
        list_name = (input("Enter Players List Name : "))
        player_name = db.get((q.list_name == list_name))
        print(player_name)
        if player_name == None:
            print('\nPlayer Not Found\nTry Again !\n')
            PlayerController.remove_name()
        else:
            print(f"\nRemove the following player ?\n\n{player_name}\n\n[1] Yes\n[2] No (other player)\n[3] Exit\n")
            option = int(input("\n\nOption Number: "))
            while option != 0:
                if option == 1:
                    # Remove by Name & Surname
                    db.remove((q.list_name == list_name))
                    print(f'\nPlayer:\n\n{player_name}\nSuccesfully Deleted !')
                    quit()
                    break
                elif option == 2:
                    PlayerController.remove_name()
                    break
                elif option == 3:
                    menu.player()
                    break
                elif option == '':
                    print('Invalid Number')
                    menu.player()
                    break
                else:
                    print('Invalid Number')
                    PlayerController.remove_name()
                    break
                


    def remove_id():
        """
        Remove players list by players list id
        """
        db = TinyDB('maxchess_db.json')
        q = Query()
        TinyDB.default_table_name = 'players_lists'
        id_num = int(input("\nEnter Player List ID : "))
        # Seach by id
        player_id = db.get(doc_id=id_num)
        if player_id is None:
            print('\nPlayer Not Found, Try Again !\n')
            PlayerController.remove_id()
        else:
            print(f"\nRemove the following player ?\n\n{player_id}\n\n[1] Yes\n[2] No (other player)\n[3] Exit\n")
            option = int(input("\n\nOption Number: "))
            while option != 0:
                if option == 1:
                    # Remove by id
                    db.remove(doc_ids=[int(id_num)])
                    print(f'\nPlayer:\n\n{player_id}\nSuccesfully Deleted !')
                    quit()
                    break
                elif option == 2:
                    PlayerController.remove_id()
                    break
                elif option == 3:
                    menu.player()
                    break
                else:
                    print('Invalid Number')
                    PlayerController.remove_id()
                    break


    def remove_all():
        db = TinyDB('maxchess_db.json')
        q = Query()
        TinyDB.default_table_name = 'players'
        if db.drop_table('players_lists'):
            print('No Players List found')
            quit()
        else:
            print('All Players Lists successfully removed !')
            quit()
