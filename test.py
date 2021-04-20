from tinydb import TinyDB, Query
from tinydb.operations import delete
from view import menu
from view import players as Players
from controller import player as Player

db = TinyDB('maxchess_db.json')
q = Query()
TinyDB.default_table_name = 'players'
print(db.tables())
db.drop_table('my_table_name')



def remove_name():
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
                break
            elif option == 2:
                remove_name()
                break
            elif option == 3:
                menu.player()
                break
            
def remove_id():

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
                break
            elif option == 2:
                remove_id()
                break
            elif option == 3:
                menu.player()
                break


def remove_all():
    db.drop_table('players')

print("\n\nRemove by ID or Name ?\n\n[1] ID\n[2] Name\n[3] Exit ↵")
delete_option = int(input("\n\nOption Number: "))
while delete_option != 0:
    if delete_option == 1:
        remove_id()
        break
    elif delete_option == 2:
        remove_name()
        break
    elif delete_option == 3:
        menu.player()
        break
    