from math import sqrt

class Coords:
    def __init__(self, w: int, p: int) -> None:
        self.w = w
        self.p = p

    def __str__(self) -> str:
        return f"({self.w}, {self.p})"
    
    @property
    def axis_coordinates(self) -> tuple:
        x = sqrt(3) / 2 * self.p
        y = self.w + 0.5 * self.p
        return (x, y)
    
    @property
    def hex_coordinates(self) -> tuple:
        return (self.w, self.p)
    