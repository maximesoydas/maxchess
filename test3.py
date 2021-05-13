from tinydb import TinyDB, Query
from tinydb import where
from tinydb.operations import delete
from view import menu
from view import players as Players
from controller import player as Player
from collections import Counter
import pprint
from operator import itemgetter 
from datetime import datetime
from model import database
pp = pprint.PrettyPrinter(indent=4)
db = TinyDB('maxchess_db_test.json')
q = Query()
TinyDB.default_table_name = 'rounds'
from model import database
from tinydb import TinyDB, Query


class Rounds:
    def __init__(self, name, datetime_start, datetime_end, matches):
        self.name = name
        self.datetime_start = datetime_start
        self.datetime_end = datetime_end
        self.matches = matches


    def serialize(self):
        '''
        Renvoie la réprésentation sérialisée du joueur
        '''
        return {
            'name' : self.name,
            'datetime_start' : self.datetime_start,
            'datetime_end' : self.datetime_end,
            'matches' : self.matches,
        }

    def save(self):
        '''
        appends objects from the player class
        calls the save method from database.py
        '''
        all.items.append(self.serialize())
        all.save()



all = database.Table('Rounds')


def first_matches():
    '''
    Sort your players list by rank
    '''
    db = TinyDB('maxchess_db_test.json')
    db.drop_table('round')
    TinyDB.default_table_name = 'players'
    players = db.search(where('rank') > '1000000')
    players.sort(key=itemgetter('rank'), reverse=True)
    n = 0
    '''
    Create players list of first round matchup
    '''
    players_list = []
    n = 0
    for i in players:
        n = n + 1
        players_list.append([str(n), i["rank"]])

    matches = [
	(players_list[0],players_list[4]),
	(players_list[1],players_list[5]),
	(players_list[2],players_list[6]),
	(players_list[3],players_list[7]),
    ]

    return matches


def add_first_round():
    '''
    Add first Round
    '''
    matches = first_matches()
    print(matches[0])
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y | %H:%M:%S")
    Rounds(
        name= (f'Round1'),
        datetime_start= (date_time),
        datetime_end= (date_time),
        matches= (matches),
    ).save()
    print('Round Added Successfully !') 

add_first_round()
