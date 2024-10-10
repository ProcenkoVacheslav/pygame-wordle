import pygame as pg

from game_logick import GameLogic

pg.init()


class Main:
    def __init__(self) -> None:
        self.app = GameLogic()

    def run(self) -> None:
        while self.app.run:
            self.app.update()
            self.app.events()

            self.app.title_text()
            self.app.draw_lines()

            self.app.draw_letters()

            self.app.break_game()
            self.app.change_color()


if __name__ == "__main__":
    app = Main()

    app.run()
