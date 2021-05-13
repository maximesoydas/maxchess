'''
TOURS/MATCHS
Chaque tour est une liste de matchs. Chaque match consiste en une paire de joueurs avec un champ de résultats pour chaque joueur. Lorsqu'un tour est terminé, le gestionnaire du tournoi saisit les résultats de chaque match avant de générer les paires suivantes. Le gagnant reçoit 1 point, le perdant 0 point. Si un match se termine par un match nul, chaque joueur reçoit 1/2 point.

Un match unique doit être stocké sous la forme d'un tuple contenant deux listes, chacune contenant deux éléments : une référence à une instance de joueur et un score. Les matchs multiples doivent être stockés sous forme de liste sur l'instance du tour. 

```python
[
    (
        [1],[900]
    ), ([5],[800])], [([2],[700],[6],[600])]

# contenant deux éléments : une référence à une instance de joueur et un score
[
    [
        [1, 900],
        [5, 800]
    ]
,
    [
        [2, 700],
        [6, 600]
    ]
]
```

En plus de la liste des correspondances, chaque instance du tour doit contenir un champ de nom. Actuellement, nous appelons nos tours "Round 1", "Round 2", etc. Elle doit également contenir un champ Date et heure de début et un champ Date et heure de fin, qui doivent tous deux être automatiquement remplis lorsque l'utilisateur crée un tour et le marque comme terminé. Les instances de round doivent être stockées dans une liste sur l'instance de tournoi à laquelle elles appartiennent.


          "matches": [
                [
                    [1],
                    ["900"]
                ],
                [
                    [5],
                    ["700"]
                ],
                
'''

                
def make_round(players):
    '''
    Create a new round from a players list
    
    players is like :
    [
	{'id': 1, 'name': 'bob', 'rank': 100},
	{'id': 2, 'name': 'alice', 'rank': 200},
	{'id': 3, 'name': 'bob', 'rank': 240},
	{'id': 4, 'name': 'bob', 'rank': 500},
	{'id': 5, 'name': 'bob', 'rank': 530},
	{'id': 6, 'name': 'bob', 'rank': 700},
	{'id': 7, 'name': 'bob', 'rank': 800},
	{'id': 8, 'name': 'bob', 'rank': 820},							
    ]
    
    returns : 
    [
        (
        	[1, 100],
        	[5, 530],
        ),(
	        [2, 200],
	        [6, 700],
        ),(
        	[3, 240],
               [7, 800],
        ),(
               [4, 500],
               [8, 820],
        )
    ]
    '''
    
  
    n = 0
    '''
    Create players matchup list of first round
    '''
    players_list = []
    n = 0
    for i in players:
        n = n + 1
        players_list.append([n, i["rank"]])

    return [
	(players_list[0],players_list[4]),
	(players_list[1],players_list[5]),
	(players_list[2],players_list[6]),
	(players_list[3],players_list[7]),
    ]
    

print('coaching Maxime chess debut')
print(make_round([
	{'id': 1, 'name': 'bob', 'rank': 100},
	{'id': 2, 'name': 'alice', 'rank': 200},
	{'id': 3, 'name': 'bob', 'rank': 240},
	{'id': 4, 'name': 'bob', 'rank': 500},
	{'id': 5, 'name': 'bob', 'rank': 530},
	{'id': 6, 'name': 'bob', 'rank': 700},
	{'id': 7, 'name': 'bob', 'rank': 800},
	{'id': 8, 'name': 'bob', 'rank': 820},							
]))
print('coaching Maxime chess fin')

def add_first_round():
    '''
    Sort your players list by rank
    '''
    # debut MODEL
    db = TinyDB('maxchess_db.json')
    TinyDB.default_table_name = 'players'
    players = db.search(where('rank') > '1000000')
    players.sort(key=itemgetter('rank'), reverse=True)
    '''
    players = [
        {'rank': },
        {}
    ]
    '''
    # fin MODEL
    
    
    
    # debut controller
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


    # debut MODEL
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
    # fin MODEL


