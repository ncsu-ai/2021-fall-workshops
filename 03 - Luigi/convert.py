import os

import luigi
import chess.pgn
import pandas as pd

from download import DownloadGames


def convert_single_game(file):
    pgn = open(f'{DownloadGames.OUTPUT_DIR}{file}')
    game = chess.pgn.read_game(pgn)
    pgn.close()

    if not game:
        return

    df = pd.DataFrame(columns=['game_id', 'board', 'move', 'match_result'])
    game_id = file[:file.find('.')]
    result = game.headers['Result']

    board = chess.Board()
    for move in game.mainline_moves():
        if board.turn == chess.BLACK:
            board.push(move)
            continue

        state = board.board_fen()
        board.push(move)
        df = df.append({
            'game_id': game_id,
            'board': state,
            'move': board.board_fen(),
            'match_result': result
        }, ignore_index=True)

    return df


class ConvertGames(luigi.Task):
    """
    TODO
    """
    OUTPUT_FILE = 'data/processed/moves.csv'

    def requires(self):
        """
        TODO
        :return:
        """
        return DownloadGames()

    def output(self):
        """
        TODO
        :return:
        """
        return luigi.LocalTarget(self.OUTPUT_FILE)

    def run(self):
        """
        TODO
        :return:
        """
        df = pd.DataFrame(columns=['game_id', 'board', 'move', 'match_result'])

        with os.scandir(DownloadGames.OUTPUT_DIR) as it:
            for entry in it:
                data = convert_single_game(entry.name)
                if data is not None:
                    df = df.append(data)

        df.to_csv(self.OUTPUT_FILE, index=False)
