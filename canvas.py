from typing import List


class Canvas:
    def __init__(self, width: int, height: int) -> None:
        self.width: int = width
        self.height: int = height
        self.shapes: List = []

    def svg_content(self) -> str:
        content = f'<svg width="{self.width}" height="{self.height}">'
        for shape in self.shapes:
            content += f"\n {shape.svg_content()}"
        content += "\n </svg>"
        return content

    def add_shape(self, shape):
        self.shapes.append(shape)
