from typing import Optional

from coords import Coords
from hex_type import HexType
from hex_probability import HexProb


class Hex:
    def __init__(self, coords: Coords, resource: Optional[HexType] = None, probability: Optional[HexProb] = None) -> None:
        self.coords = coords

