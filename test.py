from model import rounds as round_model
from model import player_tournament as player_model
from controller import tournament as tournament_controller
from controller import player as player_controller
from tinydb import TinyDB, Query, where
import datetime
from datetime import timedelta
from operator import *
import itertools
from controller import menu, tournament


def main():
   
   main = tournament.check_tournament()
   main()


main()
    