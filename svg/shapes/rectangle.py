from ..style import Style


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
