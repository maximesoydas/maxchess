from model import database
from tinydb import TinyDB, Query


class temp_tournament:
    def __init__(self, name, place, date, rounds_number, timing_method, description):
        self.name = name
        self.place = place
        self.date = date
        self.rounds_number = rounds_number
        self.timing_method = timing_method
        self.description = description


    def serialize(self):
        '''
        Renvoie la réprésentation sérialisée du joueur
        '''
        return {
            'name' : self.name,
            'place' : self.place,
            'date' : self.date,
            'rounds_number' : self.rounds_number,
            'timing_method' : self.timing_method,
            'description' : self.description,
        }

    def save(self):
        '''
        appends objects from the player class
        calls the save method from database.py
        '''
        all.items.append(self.serialize())
        all.save()

