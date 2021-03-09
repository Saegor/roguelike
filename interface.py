#!/usr/bin/env python3

import curses


class Curses:

    scr = curses.initscr()
    curses.curs_set(False)
    curses.echo(False)
    curses.start_color()
    COLORS = {}
    for n in range(16):
        curses.init_pair(1 + n, n % 8, 0)
        c = curses.color_pair(1 + n)
        if n >= 8: c |= curses.A_BOLD
        COLORS[n] = c

    commands = {
        'q': ("quit",   True),
        'l': ("move",   ( 1,  0)),
        'h': ("move",   (-1,  0)),
        'j': ("move",   ( 0,  1)),
        'k': ("move",   ( 0, -1)),
        'n': ("move",   ( 1,  1)),
        'b': ("move",   (-1,  1)),
        'u': ("move",   ( 1, -1)),
        'y': ("move",   (-1, -1)),
    }

    tiles = {
        "human":        ('@',  0b1111),
        "demon":        ('&',  0b1001),
        "ground":       ('.',  0b0010),
        "wall":         ('#',  0b0111),
        "tree":         ('7',  0b1010),
    }

    def draw_cell(self, pos, type):
        x, y = pos
        tile = self.tiles.get(type)
        if tile:
            char, color = tile
            color_pair = self.COLORS[color]
            self.scr.addstr(y, x << 1, char, color_pair)

    def get_command(self):
        key = self.scr.getkey()
        return self.commands.get(key, ("none", 0))

    def __del__(self):
        curses.endwin()


if __name__ == "__main__":
    c = Curses()
    for y in range(24):
        for x in range(24):
            c.draw_cell((x, y), "ground")
    c.draw_cell((12, 12), "human")
    c.get_command()
