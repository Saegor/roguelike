#!/usr/bin/env python3

from random import randint


class World:

    terr_map = {}
    char_list = []
    char_map = {}

    def __init__(self, map_size):
        sx, sy = map_size
        for y in range(sy):
            for x in range(sx):
                tile = "ground"
                if not randint(0, 1 << 2) : tile = "tree"
                if not randint(0, 1 << 4) : tile = "wall"
                self.terr_map[(x, y)] = tile

    def create_character(self, attr):
        char = Character(*attr)
        self.char_list.append(char)
        return char


class Character:

    def __init__(self, name, position, aspect):
        self.name = name
        self.position = position
        self.aspect = aspect

    def move(self, world, direction):
        px, py = self.position
        dx, dy = direction
        destination = px + dx, py + dy
        if world.terr_map.get(destination) in ("ground",):
            if not world.char_map.get(destination):
                self.position = destination

if __name__ == "__main__":
    p = Character("Erolcha", (4, 4), "human")
    print(vars(p))
