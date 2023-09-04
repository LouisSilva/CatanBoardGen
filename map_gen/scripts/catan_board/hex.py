from typing import Optional, Set, Union

from coords import Coords
from hex_type import HexType
from hex_probability import HexProb


class Hex:
    """A hex on a catan board"""

    CONNECTED_CORNER_OFFSETS: Set[Coords] = {
            Coords(1, 0),
            Coords(0, 1),
            Coords(-1, 1),
            Coords(-1, 0),
            Coords(0, -1),
            Coords(1, -1),
        }

    def __init__(self, coords: Coords, hex_type: Optional[HexType] = None, hex_prob: Optional[HexProb] = None) -> None:
        self.__coords = coords
        self.__hex_type = hex_type
        self.__hex_prob = hex_prob

    @property
    def coords(self) -> Coords:
        return self.__coords
    
    @property
    def hex_type(self) -> Union[HexType, None]:
        return self.__hex_type
    
    @property
    def hex_prob(self) -> Union[HexProb, None]:
        return self.__hex_prob

    def __str__(self) -> str:
        return f"{self.__hex_type.resource.capitalize()} hex with the number {self.__hex_prob.num}"
    