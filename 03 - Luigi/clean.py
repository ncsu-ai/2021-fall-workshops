import os
import shutil
from os import getcwd
from pathlib import Path

from get_urls import GetGameUrls
from download import DownloadGames
from convert import ConvertGames


try:
    os.remove(GetGameUrls.OUTPUT_FILE)
except FileNotFoundError:
    pass

try:
    shutil.rmtree(getcwd() / Path(f'./{DownloadGames.OUTPUT_DIR}'))
except FileNotFoundError:
    pass

try:
    os.remove(ConvertGames.OUTPUT_FILE)
except FileNotFoundError:
    pass
