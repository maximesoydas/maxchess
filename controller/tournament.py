from controller import clear as clr
from re import M
from model import tournament as tournament_model
from controller import rounds as round_controller
from tinydb import TinyDB, Query, where
from view import menu
from controller import menu
from controller import tools
from operator import *
from pprint import *
from time import sleep


class TournamentController():

    '''
    Controls the Tournament Model
    Retrieves general data inputs from user and calls the model to save the tournament into the database
    Calls the RoundsController, and saves each round into the tournament table
    '''

    def new_tournament():
        '''
        Add Tournament
        '''
        # Fetch basic tournament info from inputs
        name=tools.str_input('name')
        place=tools.str_input('place')
        date=tools.date_input('date')
        rounds_number=4
        timing_method="Blitz"
        description=tools.str_input('description')
        # first set the round_table empty then append round by round in the for loop
        rounds_table = []
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
        ).save()
        round_num = 0
        for rounds in range(4):
            # rounds_table = []
            round_num = round_num + 1
            round_name = f"Round{round_num}"
            # after fecthing the correct round_name
            # call the add_round() function
            round_controller.RoundsController.add_round(round_name)
            db = TinyDB('maxchess_db.json')
            TinyDB.default_table_name = 'Rounds'
            rounds = db.all()
            # append current round to the rounds_table list
            # rounds_table.append(rounds)
            db.drop_table('Rounds')
            db = TinyDB('maxchess_db.json')
            TinyDB.default_table_name = 'tournament'
            table = db.table('tournament')
            document_id = len(table)
            # update the tournament table's rounds to the rounds_table list
            # db.update({'rounds': rounds_table}, Query().rounds.exists(), doc_ids=[document_id])
            db.update({'rounds': rounds}, Query().rounds.exists(), doc_ids=[document_id])
        tournament_data = db.get(doc_id=document_id)
        best_player_name = tournament_data['rounds'][-1]['players'][0]['name']
        best_player_surname = tournament_data['rounds'][-1]['players'][0]['surname']
        print('Tournament Updated Successfully')
        print(f"Winner of this Tournament is {best_player_name} {best_player_surname}")
        quit()




    def existing_tournament(tournament_id, round_num):
        # else fetch tournament data
        db = TinyDB('maxchess_db.json')
        TinyDB.default_table_name = 'tournament'
        tournament_data = db.get(doc_id=tournament_id)
        # re-update the rounds_table variable with the latest table data
        rounds_table = tournament_data['rounds']
        for round in range(4-int(round_num)):
            round_num = int(round_num) + 1
            round_name = f"Round{round_num}"
            # after fecthing the correct round_name
            # call the add_round() function
            round_controller.RoundsController.add_round(round_name)
            db = TinyDB('maxchess_db.json')
            TinyDB.default_table_name = 'Rounds'
            rounds = db.all()
            db.drop_table('Rounds')
            # append current round to the rounds_table list
            rounds_table.append(rounds[-1])
            db = TinyDB('maxchess_db.json')
            TinyDB.default_table_name = 'tournament'
            # update the tournament table's rounds to the rounds_table list
            db.update({'rounds': rounds_table}, Query().rounds.exists(), doc_ids=[tournament_id])
        tournament_data = db.get(doc_id=tournament_id)
        best_player_name = tournament_data['rounds'][-1]['players'][0]['name']
        best_player_surname = tournament_data['rounds'][-1]['players'][0]['surname']
        print('Tournament Updated Successfully')
        print(f"Winner of this Tournament is {best_player_name} {best_player_surname}")
        quit()


    def check_tournament():
        db = TinyDB('maxchess_db.json')
        # check if tournament table exists
        TinyDB.default_table_name = 'tournament'
        all_tournaments = db.all()
        if all_tournaments:
            tournament_id = all_tournaments[-1].doc_id
            rounds = all_tournaments[-1]['rounds']
            if len(rounds) < 4:            
                while len(rounds) < 4:
                    round_num = len(rounds)
                    print(f'Previous Tournament Found ! \nPlease Enter Round {round_num + 1} Before starting a new tournament')
                    TournamentController.existing_tournament(tournament_id, round_num)
            else:
                menu.MenuController.main()
        else:
            menu.MenuController.main()


    def remove_name():
        """
        Remove players list by players list name
        """
        db = TinyDB('maxchess_db.json')
        q = Query()
        TinyDB.default_table_name = 'tournament'
        tournament_name = (input("Enter Tournament Name : "))
        tournament = db.get((q.name == tournament_name))
        if tournament == None:
            clr.screen()
            print('\nTournament Not Found\nTry Again !\n')
            TournamentController.remove_name()
        else:
            clr.screen()
            print(f"\nRemove Tournament '{tournament_name}':")
            print("[1] Yes\n[2] No (other Tournament)\n[3] Exit\n")
            option = tools.int_input('option')
            while option != 0:
                if option == 1:
                    clr.screen()
                    # Remove by Name & Surname
                    db.remove((q.name == tournament_name))
                    print(f'\nTournament Name {tournament_name}\nSuccesfully Deleted !')
                    menu.MenuController.main()
                    break
                elif option == 2:
                    clr.screen()
                    TournamentController.remove_name()
                    break
                elif option == 3:
                    clr.screen()
                    menu.MenuController.tournament()
                    break
                else:
                    clr.screen()
                    print("Wrong option number, back to Delete Tournament By Name\n")
                    TournamentController.remove_name()
                    break
                


    def remove_id():
        """
        Remove players list by players list id
        """
        db = TinyDB('maxchess_db.json')
        q = Query()
        TinyDB.default_table_name = 'tournament'
        clr.screen()
        id_num = tools.id_input("id_num")
        # Seach by id
        tournament_id = db.get(doc_id=id_num)
        if tournament_id is None:
            print('\nPlayer Not Found, Try Again !\n')
            TournamentController.remove_id()
        else:
            print(f"\nRemove Tournament Number {id_num}:")
            print("[1] Yes\n[2] No (other Tournament)\n[3] Exit\n")
            option = tools.int_input('option')
            while option != 0:
                if option == 1:
                    # Remove by id
                    clr.screen()
                    db.remove(doc_ids=[int(id_num)])
                    print(f'\Tournament:\n\nTournament {id_num}\nSuccesfully Deleted !')
                    menu.MenuController.player()
                    break
                elif option == 2:
                    TournamentController.remove_id()
                    break
                elif option == 3:
                    clr.screen()
                    menu.MenuController.tournament()
                    break
                else:
                    tools.check_range(option, 1-3)
                    clr.screen()
                    print("Wrong option number, back to Delete Tournament By ID\n")
                    TournamentController.remove_id()
                    break


    def remove_all():
        db = TinyDB('maxchess_db.json')
        q = Query()
        TinyDB.default_table_name = 'tournament'
        if db.drop_table('tournament') == False:
            print('No Tournament Found')
            quit()
        else:
            print('All Tournaments Removed Successfully!')
            quit()


