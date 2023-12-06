import lib_20_Tile as mason
import lib_20_Grid as grid
from copy import deepcopy

# Parse input and create tiles
Tiles = mason.make_tiles("20_eg.txt")

# Initiatlize possibilities with an empty grid
Possibilities = [grid.Grid(Tiles)]


def eval_possiblities():
    init_num_poss = len(Possibilities)

    new_possibilities = []
    for possibility in Possibilities:
        # Evaluation is always destructive. If we find a new possibility then it'll get added to the list.
        # If not then it means that the possibility is not viable and needs to be dropped anyway
        Possibilities.remove(possibility)

        cell = possibility.get_next_empty_cell()
        if not cell:
            continue

        for t in possibility.get_free_tiles():
            if possibility.can_fit(cell, t):
                new_possibility = deepcopy(possibility)
                new_possibility.set(cell, t)
                new_possibilities.append(new_possibility)

    Possibilities.extend(new_possibilities)
    print(
        "Num Possibilities. Initial=",
        init_num_poss,
        ", Final=",
        len(Possibilities),
        sep="",
    )


eval_possiblities()
