from typing import Optional

from coords import Coords
from hex_type import HexType


class Hex:
    def __init__(self, coords: Coords, resource: Optional[HexType] = None, probability: Optional[int] = None) -> None:
        self.coords = coords

