'''
TODO 

DONE - change the round class to tournament class and add key 'tournoi_name' and check doc for other keys
- enable reports menu to redirect toward the tournaments, the scoreboard and the players menu
- make sure you can call different past tournaments in the reports menu
DONE - launch app create players when tournament start 
DONE - create new players or use db existing players
DONE - apres la fin dun round relancer les fonctions de round jusqua round4
- demander a l'utilisateur de revenir au menu ou de quitter ou de voir les rapports

creer un tournoi je quite et je reviens = 

2 choix :
    -> tournoi en cours (il peuvent quitter le tournoi en cours et devoir le rapeller -> variable tournament_in_progress if true for 123 round if round4 false -> list all tournaments_in_progress)
    -> nouveau tournoi

'''
'''
def main_old():
    print('menu principal')
    choix = input()
    if choix = 'nouveau_tournoi':
        for i range(8):
            input(f'joueur {i}')
            ...
    elif choix = 'score_tournoi':
        for i range(4):
            input(f'gagnant match {i}')


maxcheess_status:
    # status = init : saisie des infos joueurs
    # status = match : match en cours
    # status = score    
    status: score
    rounds:
        - nom: Round 1
          joueurs:
              - id: j1
                rang: 230
                genre: M
                anniversaire: 12/08/1980
                nom: DUPOND
                prenom: Paul
              - id: j2
                rang: 230
                genre: M
                anniversaire: 12/08/1980
                nom: DUPOND
                prenom: Paul              
          matchs:
              - blanc:
                  joueur: j1
                  score: 0
              - noir:
                  joueur: j2
                  score: 1
                           

def message_debut(status):
    print('Bienvenu ....')
    if status == 'init':
        if dernier_joueur_saisi(status) == 0:
            print('Tapez [saisie_info_joueurs] pour sasir les joueurs')
        else:
            print('Tapez [saisie_info_joueurs] pour sasir les 4 joueurs restants')
    elif status == 'match':
        #... attendre la fin des match et taper [fin_match]
    elif status == 'score':
        # ... saisir/continuer score joueur
    else:
        print(f'Status inconnu : {status}'')
        
              
def dernier_joueur_saisi(status, round=0):
    
    Retourne 2 si 2 joueurus ont déjà été saisi
    
    return len(status['rounds'][round]['joueurs'])
    
def main_new():
    status = lire_status_bd()
    fin = False
    while not fin:
        # Afficher la situation actuelle (cf status)
        message_debut(status)
        # lire le choix de l'utilisateur
        choix = input()
        if choix = 'saisie_info_joueurs':
            # quel est le dernier joueur saisi
            pos_dernier_joueur_saisi = dernier_joueur_saisi(status)
            for i range(pos_dernier_joueur_saisi, 8):
                input(f'joueur {i}')
                ...
             # si tous les joueurs sont saisis, passer à l'étape match
            status['status'] = 'match'
              print('Vous pouvez lancer les match')
        elif choix = "fin_match":
              pass
        elif choix = 'saisie_score_tournoi':
            pos_dernier_score_saisi = dernier_score_saisi(status)
            for i range(pos_dernier_score_saisi, 4):
                input(f'gagnant match {i}')
                ...
'''

'''
TODO :

- Add id to Players_list

- Add status to tournament

- Check status of all tournaments when app.py is launched

- if tournament_status == player_init change range of players in the for loop, and start the app.py from there

- if tournament_status == score_init change range of matches_score in the for loop and start the app.py from there

- if tournament_status == round_init change range of rounds for the for loop and start the app.py from there


'''