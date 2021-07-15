from model import player as model
from model import players_list as player_model
from tinydb import TinyDB, Query, where
from controller import clear as clr
from operator import *
from controller import tools
from controller import menu
from pprint import *
import re
# input int  while ok int

class PlayerController():
        
    def add(n=1):
        '''
        Add Player
        '''
        list_name=input("\nEnter The Player's List Name: ")
        for i in range (n):
            print(f"\nPlease Add Player {i+1}")
            model.Player(
                name= tools.str_input('name'),
                surname=tools.str_input('surname'),
                birthday=tools.birthday_input('birthday'),
                gender=tools.gender_input('gender'),
                rank=tools.rank_input('rank'),
            ).save()
            clr.screen()
            print(f'Player {i+1} Added Successfully !')
        db = TinyDB('maxchess_db.json')
        TinyDB.default_table_name = 'players'
        players_list = db.search(where('rank') > -1)
        players_list.sort(key=itemgetter('rank'), reverse=True)
        player_model.Players_list(
            list_name=list_name,
            players=players_list,
        ).save()
        db = TinyDB('maxchess_db.json')
        TinyDB.default_table_name = 'players'
        db.drop_table('players')
        #return to menu.main
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
            clr.screen()
            print('\nPlayer Not Found\nTry Again !\n')
            PlayerController.remove_name()
        else:
            clr.screen()
            print("Remove the following Players List :")
            print(str(player_name).replace('players', '').replace(',','').replace('{', "\n").replace('}', "\n").replace('"','').replace("'", "").replace('[', "").replace(']', ""))
            print("[1] Yes\n[2] No (other Players List)\n[3] Exit\n")
            option = tools.int_input('option')
            while option != 0:
                if option == 1:
                    # Remove by Player List Name
                    clr.screen()
                    db.remove((q.list_name == list_name))
                    print(f'\nPlayer List: {list_name} Succesfully Deleted !')
                    menu.MenuController.main()
                    break
                elif option == 2:
                    clr.screen()
                    PlayerController.remove_name()
                    break
                elif option == 3:
                    clr.screen()
                    menu.MenuController.player()
                    break
                else:
                    tools.check_range(option, 1-3)
                    clr.screen()
                    print("Wrong option number, back to Delete Players List By Name\n")
                    PlayerController.remove_name()
                    break
                    
                


    def remove_id():
        """
        Remove players list by players list id
        """
        db = TinyDB('maxchess_db.json')
        q = Query()
        TinyDB.default_table_name = 'players_lists'
        clr.screen()
        id_num = tools.id_input("id_num")
        # Seach by id
        player_id = db.get(doc_id=id_num)
        if player_id is None:
            clr.screen()
            print('\nPlayer Not Found, Try Again !\n')
            PlayerController.remove_id()
        else:
            clr.screen()
            print("Remove the following Players List :")
            print(str(player_id).replace('players', '').replace(',','').replace('{', "\n").replace('}', "\n").replace('"','').replace("'", "").replace('[', "").replace(']', ""))
            print("[1] Yes\n[2] No (other Players List)\n[3] Exit\n")
            option = tools.int_input('option')
            while option != 0:
                if option == 1:
                    # Remove by id
                    clr.screen()
                    db.remove(doc_ids=[int(id_num)])
                    print(f'\nPlayer:\n\n{player_id}\nSuccesfully Deleted !')
                    menu.MenuController.player()
                    break
                elif option == 2:
                    clr.screen()
                    PlayerController.remove_id()
                    break
                elif option == 3:
                    clr.screen()
                    menu.MenuController.player()
                    break
                else:
                    tools.check_range(option, 1-3)
                    clr.screen()
                    print("Wrong option number, back to Delete Players List By ID\n")
                    PlayerController.remove_id()
                    break


    def remove_all():
        db = TinyDB('maxchess_db.json')
        q = Query()
        TinyDB.default_table_name = 'players_list'
        if db.drop_table('players_list'):
            print('No Players List found')
        else:
            pass
        TinyDB.default_table_name = 'players_lists'
        if db.drop_table('players'):
            print('No Players List found')
        else:
            pass
        TinyDB.default_table_name = 'players'
        if db.drop_table('players_lists'):
            print('No Players List found')
            menu.MenuController.main()
        else:
            print('All Players Lists successfully removed !')
            menu.MenuController.main()
        
    def remove_unfinished():
        """
        remove unfinished players list
        """
        db = TinyDB('maxchess_db.json')
        q = Query()
        TinyDB.default_table_name = 'players'
        if db.drop_table('players'):
            print('No Players List found')
        else:
            pass

