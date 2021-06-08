from pathlib import Path
from icecream import ic 
from model import tournament
import webbrowser
import os
from jinja2 import Environment, FileSystemLoader

templateLoader = FileSystemLoader(searchpath=Path(__file__).parent / 'template')
templateEnv = Environment(loader=templateLoader)


def view_text():
    tmpl = Path(__file__).parent / 'template' / 'tournaments.txt'
    # ic(tmpl)
    assert tmpl.exists(), "Template not found !!"
    #output = tmpl.open().read()
    # ic(rounds.all.items)
    tournaments = templateEnv.get_template('tournaments.txt').render(tournament = tournament.all.items)
    print(tournaments)

    with open(f"./view/tables/rounds.txt", "w") as f:
        f.write(tournaments)
    # jinja !!!

def view_html():
    tmpl = Path(__file__).parent / 'template' / 'tournaments.html'
    # ic(tmpl)
    assert tmpl.exists(), "Template not found !!"
    #output = tmpl.open().read()
    # ic(rounds.all.items)
    tournaments = templateEnv.get_template('tournaments.html').render(tournament = tournament.all.items)

    with open(f"./view/tables/tournaments.html", "w") as f:
        f.write(tournaments)
    # jinja !!!
    url_path = os.path.abspath("./view/tables/tournaments.html")
    print("The Rounds table has been created and can be viewed in your browser (view/tables/rounds.html)")
    url = f'file://{url_path}'
    webbrowser.open(url, new=2)  # open in new tab
