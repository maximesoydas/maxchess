from tinydb import TinyDB, Query
from tinydb import where
from tinydb.operations import delete
from view import menu
from view import players as Players
from controller import player as Player
from collections import Counter
import pprint
from operator import itemgetter



pp = pprint.PrettyPrinter(indent=4)
db = TinyDB('maxchess_db.json')
q = Query()
TinyDB.default_table_name = 'players'
# print(db.tables())
db.drop_table('my_table_name')



# od = sorted(db.tables(), key=lambda rank: 700)
# print(od)


# players_rank = db.get(rank=900)
# players_rank


# print(db.table('players').all()[0].keys())

first_round = db.search(where('rank') > '1000000')
first_round = first_round
pp.pprint(first_round)
# max_rank = max(first_round, key='rank', value=first_round.get)
# print(max_rank)

new_list = [i["rank"] for i in first_round]
# print(new_list)
# new_dict = dict(zip(new_list, initial_list)) 

# a = [r['rank'] for r in db]
# print(a)
# # a = db.get(doc_id=0-3)
# # print(a)
# dict(sorted(first_round.items(), key=lambda item: item[1]))

# k=[[i[0],str(i[1])] for i in sorted([[elem[0],int(elem[1])] for elem in a],key=itemgetter(1), reverse=True)]
# print(k)