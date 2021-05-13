from model import rounds as round_model
from model import player_tournament as player_model
from tinydb import TinyDB, Query, where
import datetime
from datetime import timedelta
from operator import *
import operator


def sort_players(round_name):
    '''
    Sort players by Rank if it is First Round, otherwise,
    Sort by Score and/or by Rank if the Score is even
    [
        {
        'name': 'Bethy',
        'surname': 'Daniels',
        'birthday': '07/08/1984',
        'gender': 'Female',
        'rank': '900'
        }
    ]
    '''
    if round_name == "Round1" :
        #define database, and players table
        db = TinyDB('maxchess_db.json')
        TinyDB.default_table_name = 'players'
        # search by rank
        sorted_players = db.search(where('rank') > '0')
        
        # sort by rank
        sorted_players.sort(key=itemgetter('rank'), reverse=True)
    else:
        #define database, and rounds table
        db = TinyDB('maxchess_db.json')
        TinyDB.default_table_name = 'Rounds'
        #get previous round data
        round_name = round_name.replace('Round', '')
        round_name = f'Round{int(round_name) - 1}'
        sorted_players = db.search(where('name') == round_name)
        # sort by rank & score
        sorted_players = sorted_players[0]['players']
        sorted_players.sort(key=itemgetter('rank'), reverse=True)
        sorted_players.sort(key=itemgetter('score'), reverse=True)

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

    
def set_matches(round_name):
    '''
    creates the matches list
    '''
    # global sorted_players
    sorted_players = sort_players(round_name)
    # # retrieve all surnames from players list
    n = 0
    players_list = []

    for i in sorted_players:
        surname = i['surname']
        name = i['name']
        birthday = i['birthday']
        gender = i['gender']
        n = n + 1
        if round_name == "Round1":
            score = 0
        else:
            score = i['score']
        # ASK MATCH 1v5 : L / W / E
        players_list.append([str(n), name, surname, birthday, gender, i["rank"], score])

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
    {matches[0][0][2]} VS {matches[0][1][2]}\n
    {matches[1][0][2]} VS {matches[1][1][2]}\n
    {matches[2][0][2]} VS {matches[2][1][2]}\n
    {matches[3][0][2]} VS {matches[3][1][2]}\n
    ''')
    enter_score = input("\nPress 'ENTER' To Set the Scores\n")
    return matches


def set_scores(matches):

    for (player1, player2) in matches:
        # get players names
        player1_name = player1[2]
        player2_name = player2[2]
        print(f'\nScore of match:\n {player1_name} vs {player2_name} ?\n')
        winner = input(f"\nWho won the match:\n\n[1] for {player1_name}\n[2] for {player2_name}\n[0] for Even \n\n Option Number : ")
        if winner == '1':
            player1[6] += 1.0
        # if 2 : player2 += 1
        elif winner == '2':
            player2[6] += 1.0
        # if 0 : 0.5 each (even)
        elif winner == '0':
            player1[6] += 0.5
            player2[6] += 0.5 
        else:
            print("Wrong option number !")
            quit

    scoreboard = matches
    return scoreboard


def add_first_round():

    # Fetch the round_name
    round_name = f"Round{input('Enter Round Number : ')}"
    (datetime_start, datetime_end) = set_time()
    (matches) = set_matches(round_name)
    (scoreboard) = set_scores(matches)

    # Update players_list for this tournament's round
    for i in range(4):
        for player in scoreboard[i]:
            player_model.Player_tournament(
                position = player[0],
                name= player[1],
                surname= player[2],
                birthday= player[3],
                gender=player[4],
                rank=player[5],
                score = player[6]
            ).save()



    '''
    Create Round
    '''

    db = TinyDB('maxchess_db.json')
    TinyDB.default_table_name = 'players_list'
    round_players = db.search(where('score') > -1)
    # sort by rank & score
    round_players.sort(key=itemgetter('rank'), reverse=True)
    round_players.sort(key=itemgetter('score'), reverse=True)
    print(round_players)
    db.drop_table('players_list')
    print("Score Added Successfully !")

    matches_list = []
    for match in (scoreboard):
        matches_list.append([match[0][2], match[0][6]])
        matches_list.append([match[1][2], match[1][6]])
 
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
        players= round_players
    ).save()


def remove_all(): 
    db = TinyDB('maxchess_db.json')
    q = Query()
    TinyDB.default_table_name = 'Rounds'
    db.drop_table('Rounds')
    print('Table Rounds Deleted !')
