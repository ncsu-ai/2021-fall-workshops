import re

import luigi
from bs4 import BeautifulSoup


class GetGameUrls(luigi.Task):
    """
    Scrapes an HTML file to build full download URLs for Magnus Carlsen chess games.
    """
    _base_url = 'https://old.chesstempo.com'
    OUTPUT_FILE = 'data/external/game_urls.txt'

    def output(self):
        return luigi.LocalTarget(self.OUTPUT_FILE)

    def run(self):
        with open('./data/external/game_table.html') as fp:
            soup = BeautifulSoup(fp, 'html.parser')

        # Find all game download links
        hyperlinks = soup.find_all('a', href=re.compile('download_game_pgn'))

        # Extract relative urls and build a list of full download urls
        urls = [f'{self._base_url}{tag["href"]}\n' for tag in hyperlinks]

        # Save the urls to the output target
        with open(self.OUTPUT_FILE, 'w') as fp:
            fp.writelines(urls)
