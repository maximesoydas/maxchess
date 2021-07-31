from model import rounds as round_model
from controller import player as player_controller
from tinydb import TinyDB, Query, where
import datetime
from operator import *
from controller import clear as clr
from controller import tools
from time import sleep
import pprint
from itertools import islice
import random


class RoundsController():

    '''
    Controls the Rounds' model
    Checks Round number, Sorts players, Gives out matchups, Calls Rounds model to save outcomes into the database
    '''

    def sort_players(round_name, list_name):
        '''
        Sort players by Rank if it is First Round, otherwise,
        Sort by Score and/or by Rank if the Score is even
        '''
        q = Query()
        if round_name == "Round1" :
            #define database, and players table
            db = TinyDB('maxchess_db.json')
            TinyDB.default_table_name = 'players_lists'
            players_list = db.get((q.list_name == list_name))
            sorted_players = players_list['players']
            # sort by rank
            sorted_players.sort(key=itemgetter('rank'), reverse=True)
            print(sorted_players)
        elif round_name == "Round2":
            #define database, and rounds table
            db = TinyDB('maxchess_db.json')
            TinyDB.default_table_name = 'tournament'
            table = db.table('tournament')
            table = db.get(doc_id=len(table))
            #get previous round data
            round_name = round_name.replace('Round', '')
            round_name = f'Round{int(round_name) - 1}'
            sorted_players = table['rounds'][-1]['players']
            sorted_players.sort(key=itemgetter('score'), reverse=True)
        elif round_name == "Round3":
            #define database, and rounds table
            db = TinyDB('maxchess_db.json')
            TinyDB.default_table_name = 'tournament'
            #get previous round data
            round_name = round_name.replace('Round', '')
            round_name = f'Round{int(round_name) - 1}'
            sorted_players = db.search(where('rounds')[-1]['name'] == round_name)
            sorted_players = sorted_players[-1]['rounds'][1]['players']
            sorted_players.sort(key=itemgetter('score'), reverse=True)
        elif round_name == "Round4":
            #define database, and rounds table
            db = TinyDB('maxchess_db.json')
            TinyDB.default_table_name = 'tournament'
            #get previous round data
            round_name = round_name.replace('Round', '')
            round_name = f'Round{int(round_name) - 1}'
            sorted_players = db.search(where('rounds')[-1]['name'] == round_name)
            sorted_players = sorted_players[-1]['rounds'][2]['players']
            sorted_players.sort(key=itemgetter('score'), reverse=True)
        else:
            print('Wrong Round name')
        
        return sorted_players

    def set_time():
        '''
        Timing method being "Blitz", each round has to be 5 min.
        Also, Asks how many seconds before the start of round
        '''
        # time start
        clr.screen()
        start_secs = 10
        print('\nTiming Method : BLITZ')
        print("10 seconds before start of Round")
        now = datetime.datetime.now()
        start = now + datetime.timedelta(seconds = int(start_secs))
        datetime_start = start.strftime("%m/%d/%Y %H:%M:%S")
        end = now + datetime.timedelta(seconds = 300+int(start_secs))
        datetime_end = end.strftime("%m/%d/%Y %H:%M:%S")
        print(f'\nRound Will Start at {datetime_start}')
        print(f'\nRound will finish at {datetime_end}')

        return (datetime_start, datetime_end)

    def check_matches(compare_matches, all_previous_matches, players_list, matches, xnum, outcome):
        
            
            for match in compare_matches:
                match.sort()
                # print(all_previous_matches)
                if match in all_previous_matches:
                    outcome.append('not unique')
                    # print(f'\n{match[0]} {match[1]} \n\n Already played before \n\n Creating unique matches...')
                    matches = [
                    sorted((players_list[xnum[0]],players_list[xnum[1]])),
                    sorted((players_list[xnum[2]],players_list[xnum[3]])),
                    sorted((players_list[xnum[4]],players_list[xnum[5]])),
                    sorted((players_list[xnum[6]],players_list[xnum[7]])),
                    ]
                    # print(matches)
                    compare_matches = []
                    for match in matches:
                        compare_matches.append([[match[:2][0][0], match[:2][0][1]], [match[:2][1][0], match[:2][1][1]]])
                    return matches, all_previous_matches, compare_matches, outcome, xnum
                else:
                    outcome.append('unique')

                
            return matches, all_previous_matches, compare_matches, outcome, xnum

            
            


    def set_matches(round_name, list_name):
        '''
        creates the matches list
        '''
        # Fetch the sorted players (by score and rank)
        sorted_players = RoundsController.sort_players(round_name, list_name)
        # used to append sorted players properly
        players_list = []
        # used to append previous_matches from db and definitive matches of current round
        all_previous_matches = []

        for i in sorted_players:
            surname = i['surname']
            name = i['name']
            birthday = i['birthday']
            gender = i['gender']
            if round_name == "Round1":
                score = 0
            else:
                score = i['score']
            players_list.append([name.title(), surname.title(), birthday, gender, i["rank"], score])

        # used to append previous_matches from db and matches of current round
        all_previous_matches = []
        
        if round_name == 'Round1':
            # for round 1 half players list sorted by rank
            matches = [
            sorted((players_list[0],players_list[4])),
            sorted((players_list[1],players_list[5])),
            sorted((players_list[2],players_list[6])),
            sorted((players_list[3],players_list[7])),
            ]
            for match in matches:
                # print(match[0], match[1])
                all_previous_matches.append([[match[:2][0][0], match[:2][0][1]], [match[:2][1][0], match[:2][1][1]]])
    
        elif round_name == "Round2":
            #Check if player has already fought another player before in Round1
            #Get ALL previous round matches -> compare to new matches -> if same matches found -> re-organise the matches
            
            # Matches organised by score and rank
            matches = [
            sorted((players_list[0],players_list[1])),
            sorted((players_list[2],players_list[3])),
            sorted((players_list[4],players_list[5])),
            sorted((players_list[6],players_list[7])),
            ]

            # fetch previous matches from db
            db = TinyDB('maxchess_db.json')
            TinyDB.default_table_name = 'tournament'
            round_num = round_name.replace('Round', '')
            round_nam = f'Round{int(round_num) - 1}'
            previous_matches = db.search(where('rounds')[-1]['name'] == round_nam)
            previous_matches = previous_matches[-1]['rounds'][-1]['matches']
            # put previous matches into a new list (to be updated with Round2's definitive matches)
            for match in previous_matches:
                all_previous_matches.append([[match[:2][0][0], match[:2][0][1]], [match[:2][1][0], match[:2][1][1]]])
            for match in matches:
                # print(match[0], match[1])
                all_previous_matches.append([[match[:2][0][0], match[:2][0][1]], [match[:2][1][0], match[:2][1][1]]])

        else:

            # Matches organised by score and rank
            matches = [
            sorted((players_list[0],players_list[1])),
            sorted((players_list[2],players_list[3])),
            sorted((players_list[4],players_list[5])),
            sorted((players_list[6],players_list[7])),
            ]

            # add matches into a comparing list
            compare_matches = []
            for match in matches:
                compare_matches.append([[match[:2][0][0], match[:2][0][1]], [match[:2][1][0], match[:2][1][1]]])

            db = TinyDB('maxchess_db.json')
            TinyDB.default_table_name = 'tournament'
            round_num = round_name.replace('Round', '')
            round_nam = f'Round{int(round_num) - 1}'
            last_matches = db.search(where('rounds')[-1]['name'] == round_nam)
            last_matches = last_matches[-1]['rounds'][-1]['previous_matches']
            all_previous_matches.append(last_matches)
            all_previous_matches = all_previous_matches[0]
            all_prevs_matches = all_previous_matches

            outcome = []
            while outcome != ['unique', 'unique', 'unique', 'unique']:
                all_previous_matches = all_prevs_matches
                outcome = []
                xnum = []
                # Set a length of the list to 10
                xnum = random.sample(range(0, 8), 8)
                (matches, all_previous_matches, compare_matches, outcome, xnum) = RoundsController.check_matches(compare_matches,all_previous_matches, players_list, matches, xnum, outcome)
            for match in matches:

                all_previous_matches.append([[match[:2][0][0], match[:2][0][1]], [match[:2][1][0], match[:2][1][1]]])

        print(f'''
        \n\nThe Next Matches are Sorted by Ranks and Score,\n\nIf Matches already played, unique matches are created:\n\n
        {matches[0][0][0]} {matches[0][0][1]} VS {matches[0][1][0]} {matches[0][1][1]}\n
        {matches[1][0][0]} {matches[1][0][1]} VS {matches[1][1][0]} {matches[1][1][1]}\n
        {matches[2][0][0]} {matches[2][0][1]} VS {matches[2][1][0]} {matches[2][1][1]}\n
        {matches[3][0][0]} {matches[3][0][1]} VS {matches[3][1][0]} {matches[3][1][1]}\n
        ''')
        enter_score = input(f"\nPress 'ENTER' To Set the Scores for {round_name}\n")
        # clr.screen()
        # print(all_previous_matches)
        return matches, all_previous_matches

    def set_scores(matches):

        for (player1, player2) in matches:
            # get players names
            player1_name = player1[0]
            player2_name = player2[0]
            # get players surnames
            player1_surname = player1[1]
            player2_surname = player2[1]
            # clr.screen()
            print(f'\nScore of match:\n\n{player1_name} {player1_surname} vs {player2_name} {player2_surname}\n')
            winner = 0
            while winner not in (1,2,3):
                winner = tools.winner_input(player1_name, player2_name, player1_surname, player2_surname)
                if winner == 1:
                    player1[5] += 1.0
                # if 2 : player2 += 1
                elif winner == 2:
                    player2[5] += 1.0
                # if 0 : 0.5 each (even)
                elif winner == 3:
                    player1[5] += 0.5
                    player2[5] += 0.5 
                else:
                   print("wrong option number")
                

        scoreboard = matches
        return scoreboard

    def get_players():

        print('''
        Please Enter Players List:

        [1] Use Existing Players List
        [2] Create 8 New Players
        ''')
        players_option_nb = int(input("\n\nOption : "))
        q= Query()
        while players_option_nb != 0:
            if players_option_nb == 1:
                list_name = input('Enter Existing Players List Name : ')
                db = TinyDB('maxchess_db.json')
                TinyDB.default_table_name = 'players_lists'
                if db.get((q.list_name == list_name)):
                    return list_name
                else:
                    clr.screen()
                    print(f"\nPlayer list {list_name} Doesn't exist please Try Again !")
                    RoundsController.get_players()
            elif players_option_nb == 2:
                list_name = player_controller.PlayerController.add(8)
                break
            else:
                print('Invalid Number')
                RoundsController.add_round()
                break
        return list_name

    def add_round(round_name):

        # Fetch the round_name
        round_name = round_name
        if round_name == "Round1":
            list_name = RoundsController.get_players()
            clr.screen()
        else:
            list_name = ""

        (datetime_start, datetime_end) = RoundsController.set_time()
        (matches, all_previous_matches) = RoundsController.set_matches(round_name, list_name)
        (scoreboard) = RoundsController.set_scores(matches)

        
        # Update players_list for this tournament's round
        updated_players = []
        for i in range(4):
            for player in scoreboard[i]:
                updated_player = {
                'name': player[0],
                'surname': player[1],
                'birthday': player[2],
                'gender': player[3],
                'rank': player[4],
                'score': player[5]
                }
                dictionary_copy = updated_player.copy()
                updated_players.append(dictionary_copy)
        updated_players.sort(key=itemgetter('rank'), reverse=True)
        updated_players.sort(key=itemgetter('score'), reverse=True)


        '''
        Create Round
        '''
        matches_list = []
        for match in (scoreboard):
            matches_list.append([match[0][0], match[0][1], match[0][5]])
            matches_list.append([match[1][0],match[1][1], match[1][5]])
    
        round_matches = [
            (matches_list[0],matches_list[1]),
            (matches_list[2],matches_list[3]),
            (matches_list[4],matches_list[5]),
            (matches_list[6],matches_list[7]),
            ]

        round_model.Rounds(
            name= round_name,
            datetime_start= datetime_start,
            datetime_end= datetime_end,
            matches= round_matches,
            previous_matches= all_previous_matches,
            players= updated_players
        ).save()


    def remove_all(): 
        db = TinyDB('maxchess_db.json')
        q = Query()
        TinyDB.default_table_name = 'Rounds'
        db.drop_table('Rounds')
        print('Table Rounds Deleted !')
