from typing import List
from ..style import Style


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def string(self):
        return f"{self.x},{self.y}"


class Polygon:
    def __init__(self, points: List[Point], style: Style = None):
        self.points = points
        self.style = style

    def svg_content(self):
        return f'<polygon points="{" ".join([point.string() for point in self.points])}" style={self.style.svg()} />'
