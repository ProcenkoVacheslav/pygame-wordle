import pygame as pg

from colors import *

pg.init()

title_font = pg.font.SysFont('corbel', 60, bold=True)
title_text = title_font.render('WORDLE', True, TITLE_COLOR)

letter_font = pg.font.SysFont('corbel', 55, bold=True)

end_game_font = pg.font.SysFont('corbel', 60, bold=True)

escape_font = pg.font.SysFont('corbel', 50, bold=True)

LOG_KEYS = [
    pg.K_ESCAPE,
    pg.K_TAB,
    pg.K_CAPSLOCK,
    pg.K_RSHIFT,
    pg.K_LSHIFT,
    pg.K_RALT,
    pg.K_LALT,
    pg.K_LCTRL,
    pg.K_RCTRL,
    pg.K_LSUPER,
    pg.K_RSUPER,
]
