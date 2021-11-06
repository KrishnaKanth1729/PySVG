from .style import Style
from typing import List
from .canvas import Canvas


class Shape:
    def __init__(self, canvas):
        self.canvas = canvas

    def svg_content(self) -> str:
        pass

class Rectangle(Shape):
    def __init__(self, width: int, height: int, canvas: Canvas, x: int = 0, y: int = 0, style: Style = Style({"fill": "black"})):
        super().__init__(canvas)
        canvas.add_shape(self)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.style = style

    def svg_content(self) -> str:
        content = f'<rect width="{self.width}" height="{self.height}" x={self.x} y={self.y} style={self.style.svg()} />'
        return content


class Circle(Shape):
    def __init__(self, cx: int, cy: int, r: int, style: Style, canvas: Canvas, stroke: str = "", stroke_width: int = None, fill: str = None):
        super().__init__(canvas)
        canvas.add_shape(self)
        self.cx = cx
        self.cy = cy
        self.r = r
        self.style = style
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.fill = fill

    def svg_content(self):
        return f'<circle cx="{self.cx}" cy="{self.cy}" r="{self.r}" stroke="{self.stroke}" stroke-width="{self.stroke_width}" fill="{self.fill}" style={self.style.svg} />'


class Point(Shape):
    def __init__(self, x: int, y: int, canvas: Canvas):
        super().__init__(canvas)
        self.x = x
        self.y = y

    def string(self):
        return f"{self.x},{self.y}"


class Polygon(Shape):
    def __init__(self, points: List[Point], canvas: Canvas, style: Style = Style({'fill': 'black'})):
        super().__init__(canvas)
        canvas.add_shape(self)
        self.points = points
        self.style = style

    def svg_content(self):
        return f'<polygon points="{" ".join([point.string() for point in self.points])}" style={self.style.svg()} />'


class Ellipse(Shape):
    def __init__(self, cx: int, cy: int, rx: int, ry: int, canvas: Canvas, style: Style = Style({'fill': 'black'})):
        super().__init__(canvas)
        canvas.add_shape(self)
        self.cx = cx
        self.cy = cy
        self.rx = rx
        self.ry = ry
        self.canvas = canvas
        self.style = style

    def svg_content(self) -> str:
        return f'<ellipse cx="{self.cx}" cy="{self.cy}" rx="{self.rx}" ry="{self.ry}" style="{self.style.svg()}" />'


class Line(Shape):
    def __init__(self, x1: int, y1: int, x2: int, y2: int, canvas: Canvas, style: Style = Style({'stroke': 'black'})):
        super().__init__(canvas)
        canvas.add_shape(self)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.canvas = canvas
        self.style = style

    def svg_content(self) -> str:
        return f'<line x1="{self.x1}" y1="{self.y1}" x2="{self.x2}" y2="{self.y2}" style="{self.style.svg()}" />'


class Text(Shape):
    def __init__(self, x: int, y: int, canvas: Canvas, fill: str = "black", transform: str = ""):
        super().__init__(canvas)
        canvas.add_shape(self)
        self.x = x
        self.y = y
        self.canvas = canvas
        self.fill = fill
        self.transform = transform


    def svg_content(self) -> str:
        return f'<text x="{self.x}" y="{self.y}" fill="{self.fill}" transform="{self.transform}">I love SVG</text>'

