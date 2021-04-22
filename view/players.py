from pathlib import Path
from icecream import ic 
from model import player
import webbrowser
import os
from jinja2 import Environment, FileSystemLoader

templateLoader = FileSystemLoader(searchpath=Path(__file__).parent / 'template')
templateEnv = Environment(loader=templateLoader)


def view_text():
    tmpl = Path(__file__).parent / 'template' / 'players.txt'
    ic(tmpl)
    assert tmpl.exists(), "Template not found !!"
    #output = tmpl.open().read()
    ic(player.all.items)
    player_table = templateEnv.get_template('players.txt').render(players = player.all.items)
    ic(player_table)

    with open(f"./view/tables/players.txt", "w") as f:
        f.write(player_table)
    # jinja !!!

def view_html():
    tmpl = Path(__file__).parent / 'template' / 'players.html'
    ic(tmpl)
    assert tmpl.exists(), "Template not found !!"
    #output = tmpl.open().read()
    ic(player.all.items)
    player_table = templateEnv.get_template('players.html').render(players = player.all.items)

    with open(f"./view/tables/players.html", "w") as f:
        f.write(player_table)
    # jinja !!!
    url_path = os.path.abspath("./view/tables/players.html")
    print("The Players table has been created and can be viewed in your browser (players.html)")
    url = f'file://{url_path}'
    webbrowser.open(url, new=2)  # open in new tab
