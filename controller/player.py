from model import player as model
from tinydb import TinyDB, Query



def add(n=1):
    '''
    Add Player
    '''
    for i in range (n):
        model.Player(
            ids= input("\nEnter Player Unique ID/Position (1-8 only): "),
            name=input("\nEnter Player Name: "),
            surname=input("\nEnter Player Surname: "),
            birthday=input("Enter Player Birthday: "),
            gender=input("\nEnter Player Gender: "),
            rank=input("\nEnter Player Rank: "),
        ).save()
        print('Players Added Successfully !')        


def remove_name():
    db = TinyDB('maxchess_db.json')
    q = Query()
    TinyDB.default_table_name = 'players'
    name = (input("Enter Player Name : "))
    surname = (input("Enter Player Surname : "))
    player_name = db.get((q.name == name and q.surname == surname))
    if player_name == None:
        print('\nPlayer Not Found\nTry Again !\n')
        remove_name()
    else:
        print(f"\nRemove the following player ?\n\n{player_name}\n\n[1] Yes\n[2] No (other player)\n[3] Exit\n")
        option = int(input("\n\nOption Number: "))
        while option != 0:
            if option == 1:
                # Remove by Name & Surname
                db.remove((q.name == name and q.surname == surname))
                print(f'\nPlayer:\n\n{player_name}\nSuccesfully Deleted !')
                quit()
                break
            elif option == 2:
                remove_name()
                break
            elif option == 3:
                menu.player()
                break
            elif option == '':
                print('Invalid Number')
                menu.player()
                break
            else:
                print('Invalid Number')
                remove_name()
                break
            
def remove_id():
    db = TinyDB('maxchess_db.json')
    q = Query()
    TinyDB.default_table_name = 'players'
    id_num = int(input("\nEnter Player ID : "))
    # Seach by id
    player_id = db.get(doc_id=id_num)
    if player_id is None:
        print('\nPlayer Not Found, Try Again !\n')
        remove_id()
    else:
        print(f"\nRemove the following player ?\n\n{player_id}\n\n[1] Yes\n[2] No (other player)\n[3] Exit\n")
        option = int(input("\n\nOption Number: "))
        while option != 0:
            if option == 1:
                # Remove by id
                db.remove(doc_ids=[int(id_num)])
                print(f'\nPlayer:\n\n{player_id}\nSuccesfully Deleted !')
                quit()
                break
            elif option == 2:
                remove_id()
                break
            elif option == 3:
                menu.player()
                break
            else:
                print('Invalid Number')
                remove_id()
                break


def remove_all():
    db = TinyDB('maxchess_db.json')
    q = Query()
    TinyDB.default_table_name = 'players'
    if db.drop_table('players'):
        print('Table Players Removed Successfully!')
        quit()
    else:
        print('no table named Players found')
        quit()
