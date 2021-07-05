from pathlib import Path
from icecream import ic 
from model import tournament
import webbrowser
import os
from jinja2 import Environment, FileSystemLoader

templateLoader = FileSystemLoader(searchpath=Path(__file__).parent / 'template')
templateEnv = Environment(loader=templateLoader)

class LastTournament:
    def view_text():
        tmpl = Path(__file__).parent / 'template' / 'last_tournament.txt'
        # ic(tmpl)
        assert tmpl.exists(), "Template not found !!"
        #output = tmpl.open().read()
        # ic(rounds.all.items)
        tournaments = templateEnv.get_template('last_tournament.txt').render(tournament = tournament.all.items)
        print(tournaments)

        with open(f"./view/tables/last_tournament.txt", "w") as f:
            f.write(tournaments)
        # jinja !!!

    def view_html():
        tmpl = Path(__file__).parent / 'template' / 'last_tournament.html'
        # ic(tmpl)
        assert tmpl.exists(), "Template not found !!"
        #output = tmpl.open().read()
        # ic(rounds.all.items)
        tournaments = templateEnv.get_template('last_tournament.html').render(tournament = tournament.all.items)

        with open(f"./view/tables/last_tournament.html", "w") as f:
            f.write(tournaments)
        # jinja !!!
        url_path = os.path.abspath("./view/tables/last_tournament.html")
        print("The Last Tournament table has been created and can be viewed in your browser (view/tables/rounds.html)")
        url = f'file://{url_path}'
        webbrowser.open(url, new=2)  # open in new tab
