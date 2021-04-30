from model import database
from tinydb import TinyDB, Query


class Rounds:
    def __init__(self, name, surname, datetime_start, datetime_end, matches):
        self.name = name
        self.surname = surname
        self.datetime_start = datetime_start
        self.datetime_end = datetime_end
        self.matches = matches


    def serialize(self):
        '''
        Renvoie la réprésentation sérialisée du joueur
        '''
        return {
            'name' : self.name,
            'surname' : self.surname,
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


