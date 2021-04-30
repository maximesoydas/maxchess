from pathlib import Path
from icecream import ic 
from model import rounds
import webbrowser
import os
from jinja2 import Environment, FileSystemLoader

templateLoader = FileSystemLoader(searchpath=Path(__file__).parent / 'template')
templateEnv = Environment(loader=templateLoader)


def view_text():
    tmpl = Path(__file__).parent / 'template' / 'rounds.txt'
    # ic(tmpl)
    assert tmpl.exists(), "Template not found !!"
    #output = tmpl.open().read()
    # ic(rounds.all.items)
    round_table = templateEnv.get_template('rounds.txt').render(rounds = rounds.all.items)
    ic(round_table)

    with open(f"./view/tables/rounds.txt", "w") as f:
        f.write(round_table)
    # jinja !!!

def view_html():
    tmpl = Path(__file__).parent / 'template' / 'rounds.html'
    # ic(tmpl)
    assert tmpl.exists(), "Template not found !!"
    #output = tmpl.open().read()
    # ic(rounds.all.items)
    round_table = templateEnv.get_template('rounds.html').render(rounds = rounds.all.items)

    with open(f"./view/tables/rounds.html", "w") as f:
        f.write(round_table)
    # jinja !!!
    url_path = os.path.abspath("./view/tables/rounds.html")
    print("The Rounds table has been created and can be viewed in your browser (view/tables/rounds.html)")
    url = f'file://{url_path}'
    webbrowser.open(url, new=2)  # open in new tab
