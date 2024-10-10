from config import Configurations
from settings import *
from pg_settings import *

pg.init()


class Draw(Configurations):
    def __init__(self) -> None:
        super().__init__()

    def title_text(self) -> None:
        self.root.blit(title_text, ((WIDTH - title_text.get_width()) // 2, STEP))

    def draw_lines(self) -> None:
        for rects in self.lines:
            for rect in rects:
                pg.draw.rect(self.root, *rect)

    def draw_letters(self) -> None:
        for cord_y, word in enumerate(self.draw_word):
            for cord_x, letter in enumerate(word):
                self.root.blit(letter, (START_POS_X + (SIZE - letter.get_width()) // 2 + (SIZE + STEP) * cord_x,
                                        self.START_POS_Y + (SIZE - letter.get_height()) // 2 + (SIZE + STEP) * cord_y))

    def break_game(self) -> None:
        if not self.continue_game:
            pg.draw.rect(self.root, END_GAME_COLOR,
                         (END_GAME_POS, self.START_POS_Y, END_GAME_WIDTH, HEIGHT - 2 * self.START_POS_Y))

            pg.draw.rect(self.root, SECOND_END_GAME_COLOR,
                         (END_GAME_POS, self.START_POS_Y, END_GAME_WIDTH, HEIGHT - 2 * self.START_POS_Y), 20)

            end_game_texts = [
                end_game_font.render(self.datas[RESULT], True, TEXT_COLOR),
                end_game_font.render(self.datas[ATTEMPT], True, TEXT_COLOR),
                end_game_font.render(self.datas[WORD], True, TEXT_COLOR),
                end_game_font.render(self.datas[WIN_GAMES], True, TEXT_COLOR),
            ]

            for number, fraze in enumerate(end_game_texts):
                self.root.blit(fraze, (START_POS_X + STEP,
                                       self.START_POS_Y + 2 * STEP + (fraze.get_height() + STEP) * number))

            self.restart_button.y = self.START_POS_Y + 2 * STEP + (end_game_texts[0].get_height() + STEP) * 4.5

            pg.draw.rect(self.root, self.restart_button_color, self.restart_button, 5)

            escape_text = escape_font.render('Заново', True, self.restart_button_color)
            self.root.blit(escape_text, (self.restart_button.x + (BUTTON_SIZE[0] - escape_text.get_width()) // 2,
                                         self.restart_button.y + (BUTTON_SIZE[1] - escape_text.get_height()) // 2))
