from random import choice

from settings import *

from pg_settings import *


class Configurations:
    def __init__(self) -> None:
        self.run = True
        self.root = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.all_words = self.get_words()
        self.total_word = self.restart_game()
        self.word = ['']
        self.draw_word = [[]]
        self.continue_game = True
        self.datas = []
        self.win_games = self.get_win_games()
        self.restart_button = pg.Rect(START_POS_X + (END_GAME_WIDTH - BUTTON_SIZE[0]) / 2, 400, *BUTTON_SIZE)
        self.restart_button_color = BUTTON_DIS_ACTIVE_COLOR
        self.START_POS_Y = 2 * STEP + title_text.get_height()
        self.lines = [[[SIMPLE_BLOCK_COLOR, (START_POS_X + SIZE * sqr + sqr * STEP, self.START_POS_Y,
                                             SIZE, SIZE)] for sqr in range(QUANTITY)]]

    @staticmethod
    def get_words() -> list:
        with open('files/words.txt', 'r', encoding='utf-8') as file:
            return file.readlines()

    @staticmethod
    def get_win_games() -> int:
        with open('files/attempts.txt', 'r') as file:
            return int(file.read()[:-1])

    def save_win_games(self) -> None:
        with open('files/attempts.txt', 'w') as file:
            file.write(f'{self.win_games}\n')

    def update(self) -> None:
        img = pg.image.load('img/ico.jpg')

        pg.display.flip()
        pg.display.set_caption('WORDLE')
        pg.display.set_icon(img)
        self.clock.tick(FPS)
        self.root.fill(BG_COLOR)

    def restart_game(self) -> str:
        return choice(self.all_words)[:-1].lower()
