import random
import sys
from typing import Dict, Union, Optional

from ..models import CatanBoard

def create_board(seed: Optional[Union[str, int]] = None):
    """Creates a fully random board"""

    if seed is None:
        seed = random.randrange(sys.maxsize)
    rng = random.Random(seed)

    tiles = ["ore", "ore", "ore", "brick", "brick", "brick", "sheep", "sheep", "sheep", "sheep", "wood", "wood", "wood", "wood", "wheat", "wheat", "wheat", "wheat"]
    numbers = ["2", "3", "3", "4", "4", "5", "5", "6", "6", "8", "8", "9", "9", "10", "10", "11", "11", "12"]
    
    # Shuffle tiles
    rng.shuffle(tiles)
    rng.shuffle(numbers)

    # Create pips array
    pips = []
    for number in numbers:
        if number == "6" or number == "8":
            pips.append(".....")
        elif number == "5" or number == "9":
            pips.append("....")
        elif number == "4" or number == "10":
            pips.append("...")
        elif number == "3" or number == "11":
            pips.append("..")
        elif number == "2" or number == "12":
            pips.append(".")

    # Calculate and insert desert tile location
    desert_loc = rng.randint(0, len(numbers) - 1)
    tiles.insert(desert_loc, "desert")
    numbers.insert(desert_loc, "")
    pips.insert(desert_loc, "")

    # Create a new row in db for the new board
    # new_board = CatanBoard(
    #     seed=seed,
    #     resource_tiles_order=tiles,
    #     probabilities_order=numbers,
    #     pips_order=pips
    #     )
    
    # new_board.save()

    # return {
    #     "seed": seed,
    #     "resource_tiles_order": tiles,
    #     "probabilities_order": numbers,
    #     "pips_order": pips
    # }

    return_array = []
    for i in range(len(tiles)):
        return_array.append([tiles[i], numbers[i], pips[i]])

