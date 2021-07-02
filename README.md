# Fetch Packages

First you have to install modules and packages used

```cmd
pip3 install -r requirements.txt
```


# Launch App

Open a terminal and cd yourself to the project's folder
then you can run the menu.py file with 

```shell
# enter the repo directory
cd maxchess
# Linux, MacOD
./maxchess
# Windows
maxchess.bat
```

# TODO

-Finalize the TUI with curses module

- [x] Configure Tournament Class in model/tournament.py
- [ ] add ticket for curse console view
- [x] add to print matches ( "sorted by rank")
- [x] before starting a round clear screen round and add print(' Round 2 ')
- [x] Round 2 + remove print or write the error into a json file could also add boolean debug if debug print x
- [x] add bash script for Linux ( launch app by the app name)
- [x] add batch script for Windows ( launch app by the app name)
- [x] Check if the if loop exists for checking which os 
- [x] fix jinja readability (see this [SO question](https://stackoverflow.com/questions/36870953/jinja2-how-to-remove-trailing-newline))
- [ ] Elements have to be tailored for the user (dates have to be dates, ints have to be ints, strings have to be strings, option for gender ) -> Forcer les formats
- [ ] rank/date/variables try except assert if not int -> verfier les types
- [ ] add class to all files (mvc) -> 
- [ ] elaborate a prettier print of reports -> optional
- [ ] when tournament/reports/players ends (program ends) return to main menu for reports -> main.menu() instead of quit()