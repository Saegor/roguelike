#!/usr/bin/env python3

from mechanics import World, Character
from interface import Curses

SCREEN_SIZE = (24, 24)
MAP_SIZE = (48, 48)

c = Curses()

world = World(MAP_SIZE)
player = world.create_character(("Sigmund", (24, 24), "human"))
julia = world.create_character(("Xom", (24, 28), "demon"))

run = True
while run:

    # autocenter
    ppomx, ppomy = player.position
    msx, msy = MAP_SIZE
    ssx, ssy = SCREEN_SIZE
    offset_x = sorted([0, ppomx - ssx//2, msx - ssx])[1]
    offset_y = sorted([0, ppomy - ssy//2, msy - ssy])[1]

    # refresh character map
    world.char_map = {}
    for char in world.char_list:
        world.char_map[char.position] = char.aspect

    # OUTPUT
    c.scr.erase()

    ssx, ssy = SCREEN_SIZE
    for screen_y in range(ssy):
        for screen_x in range(ssx):

            scr_pos = screen_x + offset_x, screen_y + offset_y

            # draw terrains
            c.draw_cell((screen_x, screen_y), world.terr_map.get(scr_pos))

            # draw characters
            char_tile = world.char_map.get(scr_pos)
            if char_tile:
                c.draw_cell((screen_x, screen_y), char_tile)

    c.scr.refresh()

    # INPUT
    command, argument = c.get_command()

    # PROCESS
    if command == "quit":
        run = False
    if command == "move":
        player.move(world, argument)
