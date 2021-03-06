from pathlib import Path
from icecream import ic 
from model import players_list as player
import webbrowser
import os
from jinja2 import Environment, FileSystemLoader

templateLoader = FileSystemLoader(searchpath=Path(__file__).parent / 'template')
templateEnv = Environment(loader=templateLoader)

class LastPlayers:

    def view_text():
        tmpl = Path(__file__).parent / 'template' / 'last_players.txt'
        # ic(tmpl)
        assert tmpl.exists(), "Template not found !!"
        #output = tmpl.open().read()
        # ic(player.all.items)
        player_table = templateEnv.get_template('last_players.txt').render(players = player.all.items)
        print(player_table)

        with open(f"./view/tables/players.txt", "w") as f:
            f.write(player_table)
        # jinja !!!

    def view_html():
        tmpl = Path(__file__).parent / 'template' / 'last_players.html'
        # ic(tmpl)
        assert tmpl.exists(), "Template not found !!"
        #output = tmpl.open().read()
        # ic(player.all.items)
        player_table = templateEnv.get_template('last_players.html').render(players = player.all.items)

        with open(f"./view/tables/last_players.html", "w") as f:
            f.write(player_table)
        # jinja !!!
        url_path = os.path.abspath("./view/tables/last_players.html")
        print("The Players table has been created and can be viewed in your browser (players.html)")
        url = f'file://{url_path}'
        webbrowser.open(url, new=2)  # open in new tab
