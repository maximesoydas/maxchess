from controller import tournament
from controller import player

def main():
   player.PlayerController.remove_unfinished()
   tournament.TournamentController.check_tournament()

if __name__ == "__main__":
    main()
