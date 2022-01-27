# 2021-fall-w03-luigi

A starter repository for AI Club at NC State's third workshop of 2021 which covers Luigi.

-----

References:
- [Luigi](https://luigi.readthedocs.io/en/stable/index.html)
- [Chess Tempo](https://old.chesstempo.com/game-database.html)
- [python-chess](https://python-chess.readthedocs.io/en/latest/index.html)

### Workshop Steps
1. Install prerequisites
   1. Python
   2. Git/GitHub Desktop
   3. IDE/Text Editor
2. Click "Use this template" to create a personal copy of the workshop repository
3. Clone your personal workshop repository onto your local machine
   1. Open terminal/command prompt in the directory where you want to clone the repository
   2. `git clone [repository url]`
4. Activate virtual environment from terminal/command prompt
   ```
   # Move into repository directory
   cd [repository directory]
   
   # Create a new virtual environment
   python3 -m venv .venv
   ```
   1. Windows: `.venv\Scripts\activate.bat`
   2. Unix/MacOS: `source .venv/bin/activate`
5. Install required Python packages
   ```
   pip install -r requirements.txt
   ```
6. Start the Luigi daemon
   ```
   luigid
   ```
7. The Luigi dashboard can then be accessed [here](http://localhost:8082).
8. Open a new terminal/command prompt window and activate your virtual environment in it
   ```
   # Move into repository directory
   cd [repository directory]
   ```
   1. Windows: `.venv\Scripts\activate.bat`
   2. Unix/MacOS: `source .venv/bin/activate`
9. Once you've activated your second virtual environment, make sure to run one of the following commands corresponding to your operating system
   1. Windows: `set PYTHONPATH=.;%PYTHONPATH%`
   2. MacOS: `PYTHONPATH=".;$PYTHONPATH"`
   3. Unix: `export PYTHONPATH=".;$PYTHONPATH"`
10. Familiarize yourself with the `get_urls.py` module, then run the Luigi task
    ```
    luigi --module get_urls GetGameUrls
    ```
11. Inspect the output(s) from the task, `data/external/game_urls.txt`
12. Clean up output(s) from running the task
    ```
    python -m clean
    ```
13. Familiarize yourself with the `download.py` module, then run the Luigi task
    ```
    luigi --module download DownloadGames --count 20
    ```
    1. Notice the use of the `--count` parameter, which we can use to specify how many games to download from the list of download URLs (`game_urls.txt`). If a value isn't specified for the parameter, all the games in the list of download URLs will be downloaded which may take a while.
14. Inspect the output(s) from the task, `data/external/games/[game_id].pgn`
15. Clean up output(s) from running the task
   ```
   python -m clean
   ```
16. Familiarize yourself with the `convert.py` module, then run the Luigi task
   ```
   luigi --module convert ConvertGames --DownloadGames-count 150
   ```
17. While the game files are being downloaded, check out the status of the DownloadGames task in the Luigi dashboard!
18. Inspect the output(s) from the task, `data/processed/moves.csv`
