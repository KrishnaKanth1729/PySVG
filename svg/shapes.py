from style import Style
from typing import List


class Circle:
    def __init__(self, cx: int, cy: int, r: int, style: Style, stroke_width: int = None, fill: str = None):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.style = style
        self.stroke_width = stroke_width
        self.fill = fill


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


class Rectangle:
    def __init__(self, width: int, height: int, x: int = 0, y: int = 0, style: Style = Style({"fill": "black"})):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.style = style

    def svg_content(self) -> str:
        content = f'<rect width="{self.width}" height="{self.height}" x={self.x} y={self.y} style={self.style.svg()} />'
        return content
