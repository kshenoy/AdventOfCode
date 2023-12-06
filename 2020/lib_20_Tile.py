import numpy as np
import re
from copy import deepcopy


class Tile:
    def __init__(self, name: int, contents):
        self.Name = name
        self.Contents = np.array(contents)

    def get_left(self):
        return self.Contents[:, 0].tolist()

    def get_bot(self):
        return self.Contents[-1].tolist()

    def get_top(self):
        return self.Contents[0].tolist()

    def get_right(self):
        return self.Contents[:, -1].tolist()

    def rot_l(self, times=0):
        self.Contents = np.rot90(self.Contents, times)

    def flip(self):
        self.Contents = np.fliplr(self.Contents)


def get_all_orientations(t: Tile):
    tt = deepcopy(t)
    o = [tt]

    for i in range(3):
        tt = deepcopy(tt)
        tt.rot_l(i)
        o.append(tt)

    tt = deepcopy(tt)
    tt.flip()
    o.append(t)

    for i in range(3):
        tt = deepcopy(tt)
        tt.rot_l(i)
        o.append(tt)

    return o


def has_left_right_match(a: Tile, b: Tile):
    return a.get_left() == b.get_right()


def has_right_left_match(a: Tile, b: Tile):
    return has_right_left_match(b, a)


def has_top_bot_match(a: Tile, b: Tile):
    return a.get_top() == b.get_bot()


def has_bot_top_match(a: Tile, b: Tile):
    return has_top_bot_match(b, a)


def make_tiles(f):
    tiles = []

    with open(f) as file:
        tile_name_pat = re.compile(r"^Tile\s+(\d+):")
        tile_content_pat = re.compile(r"^[.#]+$")

        tile_name = 0
        tile_contents = []

        for line in file:
            line = line.strip()

            m = tile_name_pat.match(line)
            if m:
                tile_name = int(m.group(1))
            elif tile_content_pat.match(line):
                tile_contents.append(list(line))
            else:
                tiles.append(Tile(tile_name, tile_contents))
                tile_contents.clear()

        if len(tile_contents) != 0:
            tiles.append(Tile(tile_name, tile_contents))

    return tiles
