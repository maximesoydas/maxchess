'''

 -- /home/phec/Documents/max2.py 
coucou
score of match Zoé vs Charly ?
Who won the match (1 for Zoé, 2 for Charly, 0 for even) ?1
winner="1"
score of match Clara vs Bob ?
Who won the match (1 for Clara, 2 for Bob, 0 for even) ?0
winner="0"
score of match Richard vs Alice ?
Who won the match (1 for Richard, 2 for Alice, 0 for even) ?0
winner="0"
score of match Marc vs Edouard ?
Who won the match (1 for Marc, 2 for Edouard, 0 for even) ?0
winner="0"
Scores :
----------------------
Zoé : 1.0 points
Charly : 0.0 points
Clara : 0.5 points
Bob : 0.5 points
Richard : 0.5 points
Alice : 0.5 points
Marc : 0.5 points
Edouard : 0.5 points
----------------------
phec@nuc-reunion:~/Documents$ python

La commande « python » n'a pas été trouvée, voulez-vous dire :

  commande « python3 » du deb python3
  commande « python » du deb python-is-python3

phec@nuc-reunion:~/Documents$ python3
Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> s1 = {10:0.0, 30:0.0, 20:0.0}
>>> s2 = [(10, 0.0), (30, 0.0), (20, 0.0)]
>>> s1
{10: 0.0, 30: 0.0, 20: 0.0}
>>> s2
[(10, 0.0), (30, 0.0), (20, 0.0)]
>>> s1[30] += 0.5
>>> s2[1] = (30, 0.5)
>>> s2
[(10, 0.0), (30, 0.5), (20, 0.0)]
>>> s1[30] += 0.5
>>> s1
{10: 0.0, 30: 1.0, 20: 0.0}
>>> s1
{10: 0.0, 30: 1.0, 20: 0.0}
>>> s1.
s1.clear(       s1.items(       s1.setdefault(
s1.copy(        s1.keys(        s1.update(
s1.fromkeys(    s1.pop(         s1.values(
s1.get(         s1.popitem(     
>>> s1.values()
dict_values([0.0, 1.0, 0.0])
>>> s1.items()
dict_items([(10, 0.0), (30, 1.0), (20, 0.0)])
>>> s2
[(10, 0.0), (30, 0.5), (20, 0.0)]
>>> dict(s2)
{10: 0.0, 30: 0.5, 20: 0.0}
>>> p = (30, 10, 20)
>>> s = (1.5, 0.0, 1.0)
>>> zip(p, s)
<zip object at 0x7f2b2f2a5f00>
>>> list(zip(p, s))
[(30, 1.5), (10, 0.0), (20, 1.0)]
>>> p
(30, 10, 20)
>>> s
(1.5, 0.0, 1.0)
>>> list(zip(p, s))
[(30, 1.5), (10, 0.0), (20, 1.0)]
>>> dict(zip(p, s))
{30: 1.5, 10: 0.0, 20: 1.0}
>>> s2
[(10, 0.0), (30, 0.5), (20, 0.0)]
>>> for (a, b) in s2:
...   print(f'a = {a}, b = {b}')
... 
a = 10, b = 0.0
a = 30, b = 0.5
a = 20, b = 0.0
>>> s1
{10: 0.0, 30: 1.0, 20: 0.0}
>>> for (a, b) in s1:
...    print(f'a = {a}, b = {b}')
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot unpack non-iterable int object
>>> 
>>> for x in s1:
... print(x)
  File "<stdin>", line 2
    print(x)
    ^
IndentationError: expected an indented block
>>> 
>>> for x in s1:
...   print(x)
... 
10
30
20
>>> s1.
s1.clear(       s1.items(       s1.setdefault(
s1.copy(        s1.keys(        s1.update(
s1.fromkeys(    s1.pop(         s1.values(
s1.get(         s1.popitem(     
>>> list(s1.items())
[(10, 0.0), (30, 1.0), (20, 0.0)]
>>> for x in s1.items():
... 
KeyboardInterrupt
>>> 
>>> 
>>> for (a, b) in s1.items():
...    print(f'a = {a}, b = {b}')
... 
a = 10, b = 0.0
a = 30, b = 1.0
a = 20, b = 0.0
>>> a = ['bleu', 'blanc', 'rouge']
>>> 
>>> couleurs = ['bleu', 'blanc', 'rouge']
>>> for couleur in couleurs:
...   print(couleur)
... 
bleu
blanc
rouge
>>> enumerate(couleurs)
<enumerate object at 0x7f2b2df0bd80>
>>> list(enumerate(couleurs))
[(0, 'bleu'), (1, 'blanc'), (2, 'rouge')]
>>> for (i, couleur) in enumerate(couleurs):
...   print(f'i={i}  {couleur}')
... 
i=0  bleu
i=1  blanc
i=2  rouge
>>> couleurs
['bleu', 'blanc', 'rouge']
>>> matches = [(1, 2), (3, 4), (5, 3), (4, 5)]
>>> for (p1, p2) in matches:
...   print(f'player1 {p1} vs player2 {p2}')
... 
player1 1 vs player2 2
player1 3 vs player2 4
player1 5 vs player2 3
player1 4 vs player2 5
>>> for (p1, p2) in matches:
...   print(f'match n°X : player1 {p1} vs player2 {p2}')
... 
match n°X : player1 1 vs player2 2
match n°X : player1 3 vs player2 4
match n°X : player1 5 vs player2 3
match n°X : player1 4 vs player2 5
>>> for (n, (p1, p2)) in enumerate(matches):
...   print(f'match n°{n} : player1 {p1} vs player2 {p2}')
... 
match n°0 : player1 1 vs player2 2
match n°1 : player1 3 vs player2 4
match n°2 : player1 5 vs player2 3
match n°3 : player1 4 vs player2 5
>>> 

'''

print('coucou')

def get_players():
    '''
    Get the players list
    returns a list of :
    [
        },{
            'id': 1,
            'name': 'Alice',
            'rank': 100,
            'score': 0.0,
        },{
            'id': 2,
            'name': 'Bob',
            'rank': 230,
            'score': 0.0,
        },{
            'id': 3,
            'name': 'Richard',
            'rank': 250,
            'score': 0.0,
        },{
            'id': 4,
            'name': 'Clara',
            'rank': 250) 
            'score': 0.0,
        },{
            'id': 5,
            'name': 'Marc',
            'rank': 444,
            'score': 0.0,
        },{
            'id': 3,
            'name': 'Edouard',
            'rank': 250,
            'score': 0.0,
        },{
            'id': 4,
            'name': 'Zoé',
            'rank': 250,
            'score': 0.0,
        },{
            'id': 5,
            'name': 'Charly',
            'rank': 444,
            'score': 0.0,
    ]
    rank is the rank or the previous round score
    '''
    return [{
            'id': 1,
            'name': 'Alice',
            'rank': 100,
            'score': 0.0,
        },{
            'id': 2,
            'name': 'Bob',
            'rank': 230,
            'score': 0.0,
        },{
            'id': 3,
            'name': 'Richard',
            'rank': 250,
            'score': 0.0,
        },{
            'id': 4,
            'name': 'Clara',
            'rank': 250,
            'score': 0.0,
        },{
            'id': 5,
            'name': 'Marc',
            'rank': 444,
            'score': 0.0,
        },{
            'id': 6,
            'name': 'Edouard',
            'rank': 250,
            'score': 0.0,
        },{
            'id': 7,
            'name': 'Zoé',
            'rank': 250,
            'score': 0.0,
        },{
            'id': 8,
            'name': 'Charly',
            'rank': 444,
            'score': 0.0,
        }]

def make_matches(players):
    '''
    Make the matches
    returns a list of macthes:
    [(1, 2), (3, 4), (5, 3), (4, 5)]
    '''
    return [(7, 8), (4, 2), (3, 1), (5, 6)]


def get_scores(matches, players):
    '''
    Ask for the scores of given matches

    returns : {
        1: 1.0,
        2: 0.0,
        8: 0.5,
        7: 0.5,
        6: 0.0,
        3: 1.0,
        4: 0.5,
        5: 0.5,
    }
    '''
    # init the scores of all players to 0.0
    scores = {}
    for (p1, p2) in matches:
        scores[p1] = 0.0
        scores[p2] = 0.0
    # loop over matches
    # ex : match = (5, 3)
    #for match in matches:
    for (player1, player2) in matches:
        # get players names
        player1_name = get_player_name(player1, players)
        player2_name = get_player_name(player2, players)
        # ask who won the match (1, 2 or 0)
        print(f'score of match {player1_name} vs {player2_name} ?')
        winner = input(f"Who won the match (1 for {player1_name}, 2 for {player2_name}, 0 for even) ?")
        # distribute the points :
        # if 1 : player1 += 1
        print(f'winner="{winner}"')
        if winner == '1':
            scores[player1] += 1.0
        # if 2 : player2 += 1
        elif winner == '2':
            scores[player2] += 1.0
        # else : player1 += 0.5; player2 += 0.5
        else:
            scores[player1] += 0.5
            scores[player2] += 0.5            
    return scores


def get_player_name(id_player, players):
    '''
    Get player name from its id
    '''
    for player in players:
        # if the player is the one we're looking at
        if player['id'] == id_player:
            # keep his name
            return player['name']


def affiche_score(scores, players):
    '''
    Affiche les scores :

    Scores :
    ----------------------
    Alice : 2.5 points
    Bob : 0.5 point
    Laura : 3.5 points
    ----------------------

    The scores args is like :
    {
        1: 1.0,
        3: 1.0,
        4: 0.5,
        2: 0.0,
        8: 0.5,
        7: 0.5,
        6: 0.0,
        5: 0.5,
    }
    '''
    print('Scores :')
    print('----------------------')

    # loop over scores
    for id_player in scores:
        # get player name
        name = get_player_name(id_player, players)

        score = scores[id_player]
        print(f'{name} : {score} points')

    print('----------------------')


def main():
    # get players
    players = get_players()

    # make matches
    matches = make_matches(players)

    # get scores
    scores = get_scores(matches, players)

    # print scores
    affiche_score(scores, players)

main()