
def main():
    print("""
    
      ♞ Chess Tournament Scoreboard ♖
      
    [1] Players    ♙
    [2] Tournaments ♕
    [3] Reports     ♗
    [4] Exit ↵

    """)

# CREATE TOURNAMENT
def tournament():
    print("""
    
    ♙ Welcome to the tournaments' Menu ♙

    [1] Start New Tournament
    [2] Exit to Main Menu ↵

    """)

def tournament_players():
    print("""
        
    ♙ Create New Tournament ♙

    [1] Create New Players List
    [2] Use Existing Players List
    [3] Exit to Main Menu ↵

    
    
    """)

# CREATE PLAYERS
def player():
    print("""
    
    ♙ Welcome to the players' Menu ♙

    [1] Add Players List (8 Players)
    [2] Delete Players List
    [3] Exit to Main Menu ↵

    """)

# Remove Players
def remove_players():
    print("""
    
    Remove Players List by:
    
    [1] Players List ID
    [2] Players List Name
    [3] All Players List
    [4] Exit ↵
    
    """)


# CREATE REPORTS

def reports():
    print("""
    
    ♙ Welcome to the reports' Menu ♙

    [1] View Players Reports
    [2] View Tournament Reports
    [3] Exit to Main Menu ↵

    """)

def players_reports():
    print("""
    ♙ Players reports' Menu ♙
    [1] View Latest Players report
    [2] View All Players Reports
    [3] Exit to Main Menu ↵

    """)


def tournament_reports():
    print("""
    ♙ Tournament reports' Menu ♙
    [1] View Latest Tournament report
    [2] View All Tournament Reports
    [3] Exit to Main Menu ↵

    """)