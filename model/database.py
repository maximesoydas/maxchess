from tinydb import TinyDB, Query
from icecream import ic


class Table:

    def __init__(self, name):
        '''
        Charge le nom de table joueurs/matchs/tournois depuis la base de donnée
        '''
        self.name = name
        self.items = []
        self.load()


    def save(self):
        '''
        Save all table items to the persistant db
        '''
        #self.db.insert_multiple(self.items)
        db = TinyDB(f'maxchess_db.json')   
        table = db.table(self.name)
        table.truncate()
        #ic(self.items)
        #ic(self.items[0].doc_id)
        table.insert_multiple(self.items)


    def load(self):
        '''
        Load all items from the persistant db
        '''
        db = TinyDB(f'maxchess_db.json')   
        table = db.table(self.name)
        self.items = table.all()
