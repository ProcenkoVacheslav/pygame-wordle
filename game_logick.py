from draw import Draw

from pg_settings import *
from settings import *


class GameLogic(Draw):
    def __init__(self):
        super().__init__()

    def end_game(self) -> None:
        self.continue_game = False

    def is_win(self) -> int:
        if (self.word[-1]).lower() == self.total_word:
            return 1
        elif len(self.word) == 7:
            return 2
        return 0

    def change_color(self):
        mouse_pos = pg.mouse.get_pos()

        if self.restart_button.collidepoint(mouse_pos) and not self.continue_game:
            self.restart_button_color = BUTTON_ACTIVE_COLOR
        else:
            self.restart_button_color = BUTTON_DIS_ACTIVE_COLOR

    def restart_all_game(self):
        self.total_word = self.restart_game()
        self.word = ['']
        self.draw_word = [[]]
        self.continue_game = True
        self.datas.clear()
        self.lines = [[[SIMPLE_BLOCK_COLOR, (START_POS_X + SIZE * sqr + sqr * STEP, self.START_POS_Y,
                                             SIZE, SIZE)] for sqr in range(QUANTITY)]]

    def events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False

            if event.type == pg.KEYDOWN and event.key not in LOG_KEYS and self.continue_game:
                if event.key == pg.K_RETURN and len(self.word) <= QUANTITY:
                    if self.word[-1].capitalize() + '\n' in self.all_words:
                        for number, letter in enumerate(self.word[-1]):
                            if letter.lower() in self.total_word:
                                self.lines[-1][number][0] = (0, 255, 255)
                                if letter.lower() == self.total_word[number]:
                                    self.lines[-1][number][0] = (0, 255, 0)

                        if total := self.is_win() > 0:
                            self.win_games += 1
                            self.save_win_games()

                            self.datas = [
                                f'Итог: {"Победа" if total == 1 else "Поражение"} ',
                                f'Попыток: {len(self.lines)}',
                                f'Слово: {self.total_word}',
                                f'Выйграных игр: {self.win_games}',
                            ]

                            self.end_game()

                        if len(self.word) < QUANTITY:
                            self.lines.append([[SIMPLE_BLOCK_COLOR, (START_POS_X + SIZE * sqr + sqr * STEP,
                                                                     self.START_POS_Y + len(self.lines) * (STEP + SIZE),
                                                                     SIZE, SIZE)] for sqr in range(QUANTITY)])
                            self.word.append('')
                            self.draw_word.append([])

                if event.key == pg.K_BACKSPACE:
                    self.word[-1] = self.word[-1][:-1]
                    self.draw_word[-1] = self.draw_word[-1][:-1]

                if event.key != pg.K_RETURN and event.key != pg.K_BACKSPACE:
                    if len(self.word[-1]) < 7:
                        letter = event.unicode
                        self.word[-1] += letter
                        self.draw_word[-1].append(letter_font.render(letter, True, LETTER_COLOR))

            if event.type == pg.MOUSEBUTTONDOWN:
                if not self.continue_game:
                    if self.restart_button.collidepoint(event.pos):
                        self.restart_all_game()
