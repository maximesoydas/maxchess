from model import rounds as model
from tinydb import TinyDB, Query, where
import datetime
from datetime import timedelta
from operator import itemgetter



def add_first_round():
    '''
    Sort your players list by rank
    '''
    db = TinyDB('maxchess_db.json')
    TinyDB.default_table_name = 'players'
    players = db.search(where('rank') > '1000000')
    players.sort(key=itemgetter('rank'), reverse=True)
    n = 0
    '''
    Create players matchup list of first round
    '''
    players_list = []
    matches = []
    n = 0
    for i in players:
        n = n+1
        rank = i["rank"]
        player_id = n
        tmp_list = []
        tmp_list.append(player_id)
        tmp_list.append(rank)
        player_tuple = (tmp_list[0:1], tmp_list[1:2])
        players_list.append(player_tuple)

    matches.append(players_list[0])
    matches.append(players_list[4])

    matches.append(players_list[1])
    matches.append(players_list[5])

    matches.append(players_list[2])
    matches.append(players_list[6])

    matches.append(players_list[3])
    matches.append(players_list[7])

    '''
    Add first Round to Rounds table
    '''

    surname = [r['surname'] for r in db]
    print(surname[0])
    now = datetime.datetime.now()
    date_time = now.strftime("%m/%d/%Y %H:%M:%S")
    now = datetime.datetime.now()
    date_time_end = now + datetime.timedelta(minutes = 5.20)
    date_time_end = date_time_end.strftime("%m/%d/%Y %H:%M:%S")
    model.Rounds(
        name= (f'Round1'),
        surname = (surname),
        datetime_start= (date_time),
        datetime_end= (date_time_end),
        matches= (matches),
    ).save()
    print('First Round Started Successfully !') 



def remove_all(): 
    db = TinyDB('maxchess_db.json')
    q = Query()
    TinyDB.default_table_name = 'Rounds'
    db.drop_table('Rounds')
    print('Table Rounds Deleted !')
