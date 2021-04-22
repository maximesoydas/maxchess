from model import database
from tinydb import TinyDB, Query


class Player:
    def __init__(self, name, surname, birthday, gender, rank):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.gender = gender
        self.rank = rank


    def serialize(self):
        '''
        Renvoie la réprésentation sérialisée du joueur
        '''
        return {
            'name' : self.name,
            'surname' : self.surname,
            'birthday' : self.birthday,
            'gender' : self.gender,
            'rank' : self.rank,
        }

    def save(self):
        '''
        appends objects from the player class
        calls the save method from database.py
        '''
        all.items.append(self.serialize())
        all.save()


all = database.Table('players')