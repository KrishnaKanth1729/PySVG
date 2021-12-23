from typing import Optional, List
from svg.canvas import Canvas


class Link:
    def __init__(self, href: Optional[str], canvas: Canvas):
        """
        Link class for HTML <a> tags

        :param href:
        """

        canvas.add_shape(self)
        self.href = href
        self.shapes = []

    def svg_content(self) -> str:
        content = f'<a href="{self.href}">'
        for shape in self.shapes:
            content += shape.svg_content()
        content += '</a>'
        return content

    def add_shape(self, shape) -> None:
        self.shapes.append(shape)

