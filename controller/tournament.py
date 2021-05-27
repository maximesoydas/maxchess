from re import M
from model import tournament as tournament_model
from model import temp_tournament as temp_tournament_model
from controller import rounds as round_controller
from tinydb import TinyDB, Query, where
from view import menu
from operator import *
import json

def new_tournament():
    '''
    Add Tournament
    '''
    name=input("\nEnter Tournament Name: ")
    place=input("\nEnter Tournament Place: ")
    date=input("Enter Tournament Date (dd/mm/yyyy): ")
    rounds_number=4
    timing_method="Blitz"
    description=input("Enter Description:")
    rounds_table = []
    print('''
    [1] Start Tournament Later
    [2] Start Tournament Now   
    [3] Exit to main menu
    ''')
    option_number= int(input("Enter Option Number: "))
    
    while option_number != 0:
        if option_number == 1:
            temp_tournament_model.temp_tournament(
                name= name,
                place= place,
                date= date,
                rounds_number= rounds_number,
                timing_method= timing_method,
                description= description,
            ).save()
            print('Temporary Tournament Added Successfully')
            menu.main()
            break
        elif option_number == 2:
            round_num = 0
            for rounds in range(4):
                round_num = round_num + 1
                round_name = f"Round{round_num}"
                round_controller.add_round(round_name)
            db = TinyDB('maxchess_db.json')
            TinyDB.default_table_name = 'Rounds'
            rounds = db.all()
            rounds_table.append(rounds)
            db = TinyDB('maxchess_db.json')
            TinyDB.default_table_name = 'Rounds'
            db.drop_table('Rounds')
            tournament_model.Tournament(
                name= name,
                place= place,
                date= date,
                rounds_number= rounds_number,
                timing_method= timing_method,
                description= description,
                rounds= rounds_table,
            ).save()
            print('Round Added Successfully !')
            print('Tournament Updated Successfully')
            menu.main()
        else:
            menu.main()
            break



def existing_tournament(tournament_name):
    # Request to check if 'rounds': [{ name: Round 4}] exists pass
    # else fetch tournament data
    tournament_name = tournament_name
    q = Query()
    db = TinyDB('maxchess_db.json')
    TinyDB.default_table_name = 'tournament'
    tournament_list = db.get((q.name == tournament_name))
    tournament_round = tournament_list['rounds'][0]['name']
    print(tournament_round)
    tournament_players = tournament_list['rounds'][0]['players']
    print(tournament_players)
    return (tournament_players)


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
        remove_name()
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
                remove_name()
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
                remove_name()
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
        remove_id()
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
                remove_id()
                break
            elif option == 3:
                menu.player()
                break
            else:
                print('Invalid Number')
                remove_id()
                break


def remove_all():
    db = TinyDB('maxchess_db.json')
    q = Query()
    TinyDB.default_table_name = 'players'
    if db.drop_table('players'):
        print('Table Players Removed Successfully!')
        quit()
    else:
        print('no table named Players found')
        quit()
