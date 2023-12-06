import numpy as np
import math
import lib_20_Tile as mason


class Grid:
    def __init__(self, tiles):
        self.__free_tiles = {}
        for t in tiles:
            self.__free_tiles[t.Name] = t

        self.__size = len(tiles)
        self.__side_len = int(math.sqrt(self.__size))
        self.__cells = np.full((self.__side_len, self.__side_len), None)

    def get(self, loc):  # -> Tile
        if not loc:
            return None
        (x, y) = loc
        return self.__cells[x][y]

    def get_free_tiles(self):
        return [t.Name for t in list(self.__free_tiles.values())]

    def get_next_empty_cell(self):  # -> (int, int)
        loc = (0, 0)
        for _ in range(self.__size):
            if self.get(loc) == None:
                return loc

            loc = self.__get_next_diagonal_loc(loc)
            if not loc:
                return None
        return None

    # Get next location when traversing the grid diagonally (up and right)
    def __get_next_diagonal_loc(self, loc):  # -> (int, int)
        if not loc:
            return None
        (x, y) = loc

        lim = self.__side_len - 1
        if (x == lim) and (y == lim):
            return None
        elif (x > 0) and (y < lim):
            return (x - 1, y + 1)
        else:
            return (min(x + y + 1, lim), max((x + y + 1 - lim), 0))

    # Test if Tile 't' can fit in the grid given the following constraints:
    # * 't' shouldn't already be used elsewhere
    # * (x, y) should have at least one occupied neighbor.
    #   This is meant to constrain where tiles can be placed to prevent the possibilities from exploding
    # * The only exception to the above is if the grid is entirely empty so that we can place the first tile
    def can_fit(self, loc, id: int):
        if not loc:
            return False
        elif not id in self.__free_tiles:
            return False
        elif len(self.__free_tiles) == self.__size:  # Grid is empty
            return True

        orientations = mason.get_all_orientations(self.__free_tiles[id])
        # Each tile has 8 orientations
        return True

    def set(self, loc, id: int):
        if loc:
            (x, y) = loc
            self.__cells[x][y] = self.__free_tiles.pop(id)

    def __get_left_neighbor(self, loc):  # -> Tile
        if loc:
            (x, y) = loc
            if x > 0:
                return self.get((x - 1, y))
        return None

    def __get_bot_neighbor(self, loc):  # -> Tile
        if loc:
            (x, y) = loc
            if y > 0:
                return self.get((x, y - 1))
        return None

    def __get_top_neighbor(self, loc):  # -> Tile
        if loc:
            (x, y) = loc
            if y < self.__side_len - 1:
                return self.get((x, y + 1))
        return None

    def __get_right_neighbor(self, loc):  # -> Tile
        if loc:
            (x, y) = loc
            if x < self.__side_len - 1:
                return self.get((x + 1, y))
        return None
