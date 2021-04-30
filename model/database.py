from tinydb import TinyDB, Query
from icecream import ic

#db = TinyDB(f'maxchess_db_{self.name}.json')
db = TinyDB(f'maxchess_db.json')




def read_table(table):
    '''
    Lit une table depuis la base de donnée
    '''
    pass



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
        table = db.table(self.name)
        table.truncate()
        #ic(self.items)
        #ic(self.items[0].doc_id)
        table.insert_multiple(self.items)


    def load(self):
        '''
        Load all items from the persistant db
        '''
        table = db.table(self.name)
        self.items = table.all()
