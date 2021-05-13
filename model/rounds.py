from model import database
from tinydb import TinyDB, Query

class Rounds:
    def __init__(self, name, datetime_start, datetime_end, matches, players):
        self.name = name
        self.datetime_start = datetime_start
        self.datetime_end = datetime_end
        self.matches = matches
        self.players = players


    def serialize(self):
        '''
        Renvoie la réprésentation sérialisée du joueur
        '''
        return {
            'name' : self.name,
            'datetime_start' : self.datetime_start,
            'datetime_end' : self.datetime_end,
            'matches' : self.matches,
            'players' : self.players,
        }

    def save(self):
        '''
        appends objects from the player class
        calls the save method from database.py
        '''
        all.items.append(self.serialize())
        all.save()

    


all = database.Table('Rounds')


