'''
Classses fundamental tools
Classes is a template : for creating object with related data and functions that interact with that data
'''

class User:
    pass

# User1 is an instance of the user class or an object
user1 = User()
# first_name and last_name are fields: data attached to an object
user1.first_name = "Dave"
user1.last_name = "Bowman"
#Check if the data is in the user1 object, print them
print(user1.first_name)

print(user1.last_name)


# stand alone variables, this values are not attached to an object
# values are kept seperate
first_name = "Arthur"
last_name = "Clark"

user2 = User()
user2.first_name = "Frank"
user2.last_name = "Poole"

# Classes are used to make object and each objects can have different values with the same variable  name

user1.age = 37
user2.favorite_book = "2001: A space odyssey"

#Objects of the same class can have different field names 

from dataclasses import dataclass

@dataclass
class Player():
    name: str
    age: int
    rank: int

def go():
    player1 = Player(name="Maxime", age=25)