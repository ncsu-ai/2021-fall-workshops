import os

import luigi
import requests

from get_urls import GetGameUrls


class DownloadGames(luigi.Task):
    """
    Downloads chess games from a list of download URLs as .pgn files.
    """
    OUTPUT_DIR = './data/external/games/'
    HEADERS = {
        'Host': 'old.chesstempo.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://old.chesstempo.com/game-database.html',
        'Cookie': 'napp2.sid=ag6uvkCbTc_osgn9JJRy5L1zu9N5ycAl; PHPSESSID=of2bmu1k1jkbrbn4jsgvsdaou6; rm_scroll_pos=648',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1'
    }

    count = luigi.IntParameter(default=-1)

    def requires(self):
        """
        Defines the task's dependencies.
        :return: the GetGameUrls task which must be run before this task
        """
        return GetGameUrls()

    def output(self):
        """
        Defines the task's outputs.
        :return: a local target representing the directory where downloaded games will be saved
        """
        return luigi.LocalTarget(self.OUTPUT_DIR, format=None)

    def run(self):
        """
        TODO
        :return:
        """
        with open(GetGameUrls.OUTPUT_FILE, 'r') as fp:
            urls = fp.readlines()

        if self.count < 0:
            c = len(urls)
        else:
            c = self.count

        os.mkdir(self.OUTPUT_DIR)

        for i in range(c):
            url = urls[i][:-1]
            game_id = url[url.rfind('=') + 1:]

            # Reference: https://stackoverflow.com/a/16696317
            with requests.get(url, headers=self.HEADERS, stream=True, allow_redirects=True) as r:
                r.raise_for_status()
                with open(f'{self.OUTPUT_DIR}{game_id}.pgn', 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        # If you have chunk encoded response uncomment if
                        # and set chunk_size parameter to None.
                        # if chunk:
                        f.write(chunk)

            self.set_progress_percentage(i / c)
