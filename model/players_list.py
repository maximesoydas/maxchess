from model import database
from tinydb import TinyDB, Query


class Players_list:
    def __init__(self, list_name, players):
        self.list_name = list_name
        self.players = players

    def serialize(self):
        '''
        Renvoie la réprésentation sérialisée du joueur
        '''
        return {
            'list_name' : self.list_name,
            'players' : self.players,
        }

    def save(self):
        '''
        appends objects from the player class
        calls the save method from database.py
        '''
        all.items.append(self.serialize())
        all.save()


all = database.Table('players_lists')