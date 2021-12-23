from .link import Link
from .canvas import Canvas
from typing import Union, List, Optional
from .style import Style


class Shape:
    def __init__(self, parent):
        self.parent: Union[Canvas, Link] = parent
        self.area: int = 0

    def svg_content(self) -> str:
        pass


class Rectangle(Shape):
    def __init__(self, width: int, height: int, parent:
                 Union[Canvas, Link], x: int = 0, y: int = 0,
                 style: Optional[Style] = Style({"fill": "black"}),
                 rx: Optional[int] = 0, ry: Optional[int] = 0):
        """
        Rectangle class

        :param width
        :param height: int
        :param parent
        :param x:
        :param y:
        :param style:
        :param rx:
        :param ry:
        """
        super().__init__(parent)
        parent.add_shape(self)
        self.width = width
        self.height = height
        self.area = self.width * self.height
        self.x = x
        self.y = y
        self.style = style
        self.rx = rx
        self.ry = ry

    def svg_content(self) -> str:
        content = f'<rect width="{self.width}" height="{self.height}" x={self.x} y={self.y} style={self.style.svg()} rx={self.rx} ry={self.ry} />'
        return content


class Circle(Shape):
    def __init__(self, cx: int, cy: int, r: int, parent: Union[Canvas, Link],
                 stroke: str = "", stroke_width: int = None, fill: str = 'black',
                 style: Style = Style({})):

        if not isinstance(parent, Canvas) and not isinstance(parent, Link):
            raise ValueError(f"Expected a class of Canvas or Link found type "
                             f"{type(parent)}")

        super().__init__(parent)
        self.parent.add_shape(self)

        self.cx = cx
        self.cy = cy
        self.r = r
        self.style = style
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.fill = fill

    def svg_content(self):
        return f'<circle cx="{self.cx}" cy="{self.cy}" r="{self.r}" ' \
               f'stroke="{self.stroke}" stroke-width="{self.stroke_width}" ' \
               f'fill="{self.fill}" style={self.style.svg()} />'


class Point(Shape):
    """
        Class to represent
    """
    def __init__(self, x: int, y: int, canvas: Canvas):
        super().__init__(canvas)

        self.x = x
        self.y = y
        self.canvas = canvas
        self.check_outline()

    def check_outline(self):
        if self.x > self.canvas.width:
            raise Warning(f"X {self.x} value of point {self} lies outside canvas "
                          f"of width {self.canvas.width}")
        elif self.y > self.canvas.height:
            raise Warning(f"x {self.x} value of point {self} lies outside canvas "
                          f"of width {self.canvas.width}")

    def __str__(self):
        return f"{self.x},{self.y}"


class Polygon(Shape):
    """
        Class for the polygon class
        <polygon points="">
    """
    def __init__(self, points: List[Union[Point, tuple]], parent: Union[Canvas, Link], style: Style = Style({'fill': 'black'})):
        if not isinstance(parent, Canvas) and not isinstance(parent, Link):
            raise ValueError(f"Expected a class of Canvas or Link found type {type(parent)}")

        super().__init__(parent)
        parent.add_shape(self)
        self.points = points
        self.style = style

    def svg_content(self):
        return f'<polygon points="{" ".join([str(point) for point in self.points])}" style={self.style.svg()} />'


class Ellipse(Shape):
    """
        A Class for the SVG Ellipse
    """
    def __init__(self, cx: int, cy: int, rx: int, ry: int,
                 parent: Union[Canvas, Link], style: Style = Style({'fill': 'black'})):

        if not isinstance(parent, Canvas) and not isinstance(parent, Link):
            raise ValueError(f"Expected a class of Canvas or Link found type "
                             f"{type(parent)}")

        super().__init__(parent)
        parent.add_shape(self)

        self.cx = cx
        self.cy = cy
        self.rx = rx
        self.ry = ry
        self.canvas = parent
        self.style = style

    def svg_content(self) -> str:
        return f'<ellipse cx="{self.cx}" cy="{self.cy}" rx="{self.rx}" ' \
               f'ry="{self.ry}" style="{self.style.svg()}" />'


class Line(Shape):
    def __init__(self, x1: int, y1: int, x2: int, y2: int, parent: Union[Canvas, Link], style: Style = Style({'stroke': 'black'})):
        if not isinstance(parent, Canvas) and not isinstance(parent, Link):
            raise ValueError(f"Expected a class of Canvas or Link found type {type(parent)}")

        super().__init__(parent)
        parent.add_shape(self)

        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.canvas = parent
        self.style = style

    def svg_content(self) -> str:
        return f'<line x1="{self.x1}" y1="{self.y1}" x2="{self.x2}" y2="{self.y2}" style="{self.style.svg()}" />'


class Text(Shape):
    def __init__(self, x: int, y: int, text: str, parent: Union[Canvas, Link], fill: str = "black", transform: Optional[str] = ""):
        if not isinstance(parent, Canvas) and not isinstance(parent, Link):
            raise ValueError(f"Expected a class of Canvas or Link found type {type(parent)}")

        super().__init__(parent)
        parent.add_shape(self)
        self.x = x
        self.y = y
        self.canvas = parent
        self.fill = fill
        self.transform = transform
        self.text = text

    def svg_content(self) -> str:
        return f'<text x="{self.x}" y="{self.y}" fill="{self.fill}" transform="{self.transform}">{self.text}</text>'
