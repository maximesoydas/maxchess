from controller.menu import tournament
from re import M
from model import tournament as tournament_model
from model import temp_tournament as temp_tournament_model
from controller import rounds as round_controller
from tinydb import TinyDB, Query, where
from view import menu
from controller import menu
from operator import *
import json


def new_tournament():
    '''
    Add Tournament
    '''
    # Fetch basic tournament info from inputs
    name=input("\nEnter Tournament Name: ")
    place=input("\nEnter Tournament Place: ")
    date=input("Enter Tournament Date (dd/mm/yyyy): ")
    rounds_number=4
    timing_method="Blitz"
    description=input("Enter Description:")
    # first set the round_table empty then append round by round in the for loop
    rounds_table = []
    status = True
    # delete previous tournaments Rounds table
    db = TinyDB('maxchess_db.json')
    TinyDB.default_table_name = 'Rounds'
    db.drop_table('Rounds')
    # Save the previous inputs and create tournament table in db
    tournament_model.Tournament(
        name= name,
        place= place,
        date= date,
        rounds_number= rounds_number,
        timing_method= timing_method,
        description= description,
        rounds= rounds_table,
        status= status,
    ).save()
    round_num = 0
    for rounds in range(4):
        # reset the rounds_table to an empty list (avoiding duplicates)
        rounds_table = []
        round_num = round_num + 1
        round_name = f"Round{round_num}"
        # after fecthing the correct round_name
        # call the add_round() function
        round_controller.add_round(round_name)
        db = TinyDB('maxchess_db.json')
        TinyDB.default_table_name = 'Rounds'
        rounds = db.all()
        # append current round to the rounds_table list
        rounds_table.append(rounds)
        db.drop_table('Rounds')
        db = TinyDB('maxchess_db.json')
        TinyDB.default_table_name = 'tournament'
        this_tournament= db.get(Query().name == name)
        this_tournament.doc_id
        document_id= this_tournament.doc_id
        # update the tournament table's rounds to the rounds_table list
        db.update({'rounds': rounds_table}, Query().rounds.exists(), doc_ids=[document_id])
    tournament_data = db.get(doc_id=document_id)
    best_player_name = tournament_data['rounds'][0][-1]['players'][0]['name']
    best_player_surname = tournament_data['rounds'][0][-1]['players'][0]['surname']
    print('Round Added Successfully !')
    print('Tournament Updated Successfully')
    print(f"Winner of this Tournament is {best_player_name} {best_player_surname}")
    quit()




def existing_tournament(tournament_id, round_num):
    # else fetch tournament data
    db = TinyDB('maxchess_db.json')
    TinyDB.default_table_name = 'tournament'
    tournament_data = db.get(doc_id=tournament_id)
    # re-update the rounds_table variable with the latest table data
    rounds_table = tournament_data['rounds'][0]
    for round in range(4-int(round_num)):
        round_num = int(round_num) + 1
        round_name = f"Round{round_num}"
        # after fecthing the correct round_name
        # call the add_round() function
        round_controller.add_round(round_name)
        db = TinyDB('maxchess_db.json')
        TinyDB.default_table_name = 'Rounds'
        rounds = db.all()
        # append current round to the rounds_table list
        rounds_table.append(rounds)
        db.drop_table('Rounds')
        db = TinyDB('maxchess_db.json')
        TinyDB.default_table_name = 'tournament'
        # update the tournament table's rounds to the rounds_table list
        db.update({'rounds': rounds_table}, Query().rounds.exists(), doc_ids=[tournament_id])
        rounds_table = []
    tournament_data = db.get(doc_id=tournament_id)
    best_player_name = tournament_data['rounds'][0][-1]['players'][0]['name']
    best_player_surname = tournament_data['rounds'][0][-1]['players'][0]['surname']
    print('Round Added Successfully !')
    print('Tournament Updated Successfully')
    print(f"Winner of this Tournament is {best_player_name} {best_player_surname}")
    return menu.main()


def tournament_exists():

    pass

def check_tournament():
    db = TinyDB('maxchess_db.json')
    # check if tournament table exists
    TinyDB.default_table_name = 'tournament'
    all_tournaments = db.all()
    if all_tournaments:
        tournament_id = all_tournaments[-1].doc_id
        rounds = all_tournaments[-1]['rounds'][0]
        if len(rounds) < 4:            
            while len(rounds) < 4:
                round_num = len(rounds) 
                print(f'Previous Tournament Found ! \nPlease Enter Round {round_num + 1} Before starting a new tournament')
                existing_tournament(tournament_id, round_num)
        else:
            menu.main()
    else:
        menu.main()

