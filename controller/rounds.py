from model import rounds as round_model
from controller import player as player_controller
from tinydb import TinyDB, Query, where
import datetime
from operator import *
from controller import clear as clr

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
    elif round_name == "Round2":
        #define database, and rounds table
        db = TinyDB('maxchess_db.json')
        TinyDB.default_table_name = 'tournament'
        #get previous round data
        round_name = round_name.replace('Round', '')
        round_name = f'Round{int(round_name) - 1}'
        sorted_players = db.search(where('rounds')[0]['name'] == round_name)
        sorted_players = sorted_players[-1]['rounds'][0]['players']
        sorted_players.sort(key=itemgetter('score'), reverse=True)
    elif round_name == "Round3":
        #define database, and rounds table
        db = TinyDB('maxchess_db.json')
        TinyDB.default_table_name = 'tournament'
        #get previous round data
        round_name = round_name.replace('Round', '')
        round_name = f'Round{int(round_name) - 1}'
        sorted_players = db.search(where('rounds')[1]['name'] == round_name)
        sorted_players = sorted_players[-1]['rounds'][1]['players']
        sorted_players.sort(key=itemgetter('score'), reverse=True)
    elif round_name == "Round4":
        #define database, and rounds table
        db = TinyDB('maxchess_db.json')
        TinyDB.default_table_name = 'tournament'
        #get previous round data
        round_name = round_name.replace('Round', '')
        round_name = f'Round{int(round_name) - 1}'
        sorted_players = db.search(where('rounds')[2]['name'] == round_name)
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

    start_secs = input("\nEnter Number Of Seconds Before Start : ")
    print('\nTiming Method : BLITZ\n')
    now = datetime.datetime.now()
    start = now + datetime.timedelta(seconds = int(start_secs))
    datetime_start = start.strftime("%m/%d/%Y %H:%M:%S")
    end = now + datetime.timedelta(seconds = 300+int(start_secs))
    datetime_end = end.strftime("%m/%d/%Y %H:%M:%S")
    print(f'\nRound Will Start at {datetime_start}')
    print(f'\nRound will finish at {datetime_end}')

    return (datetime_start, datetime_end)

    
def set_matches(round_name, list_name):
    '''
    creates the matches list
    '''
    # global sorted_players
    sorted_players = sort_players(round_name, list_name)
    # # retrieve all surnames from players list
    players_list = []

    for i in sorted_players:
        surname = i['surname']
        name = i['name']
        birthday = i['birthday']
        gender = i['gender']
        if round_name == "Round1":
            score = 0
        else:
            score = i['score']
        players_list.append([name, surname, birthday, gender, i["rank"], score])
        
    if round_name == 'Round1':
        matches = [
        (players_list[0],players_list[4]),
        (players_list[1],players_list[5]),
        (players_list[2],players_list[6]),
        (players_list[3],players_list[7]),
        ]
    else:
        matches = [
        (players_list[0],players_list[1]),
        (players_list[2],players_list[3]),
        (players_list[4],players_list[5]),
        (players_list[6],players_list[7]),
        ]
    print(f'''
    \n\nThe Next Matches are:\n\n
    {matches[0][0][0]} {matches[0][0][1]} VS {matches[0][1][0]} {matches[0][1][1]}\n
    {matches[1][0][0]} {matches[1][0][1]} VS {matches[1][1][0]} {matches[1][1][1]}\n
    {matches[2][0][0]} {matches[2][0][1]} VS {matches[2][1][0]} {matches[2][1][1]}\n
    {matches[3][0][0]} {matches[3][0][1]} VS {matches[3][1][0]} {matches[3][1][1]}\n
    ''')
    enter_score = input("\nPress 'ENTER' To Set the Scores\n")
    return matches


def set_scores(matches):

    for (player1, player2) in matches:
        # get players names
        player1_name = player1[1]
        player2_name = player2[1]
        print(f'\nScore of match:\n {player1_name} vs {player2_name} ?\n')
        winner = input(f"\nWho won the match:\n\n[1] for {player1_name}\n[2] for {player2_name}\n[0] for Even \n\n Option Number : ")
        if winner == '1':
            player1[5] += 1.0
        # if 2 : player2 += 1
        elif winner == '2':
            player2[5] += 1.0
        # if 0 : 0.5 each (even)
        elif winner == '0':
            player1[5] += 0.5
            player2[5] += 0.5 
        else:
            print("Wrong option number !")
            quit

    scoreboard = matches
    return scoreboard

def get_players():

    print('''
    [1] Use Existing Players
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
                get_players()
        elif players_option_nb == 2:
            list_name = player_controller.add(8)
            break
        else:
            print('Invalid Number')
            add_round()
            break
    print("this is list name !!!!!!!!!")
    return list_name

def add_round(round_name):

    # Fetch the round_name
    round_name = round_name
    if round_name == "Round1":
        list_name = get_players()
        clr.screen()
    else:
        list_name = ""

    (datetime_start, datetime_end) = set_time()
    (matches) = set_matches(round_name, list_name)
    (scoreboard) = set_scores(matches)

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
        matches_list.append([match[0][1], match[0][5]])
        matches_list.append([match[1][1], match[1][5]])
 
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
        players= updated_players
    ).save()


def remove_all(): 
    db = TinyDB('maxchess_db.json')
    q = Query()
    TinyDB.default_table_name = 'Rounds'
    db.drop_table('Rounds')
    print('Table Rounds Deleted !')
