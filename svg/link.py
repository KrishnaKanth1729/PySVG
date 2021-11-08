from typing import Optional, List
from .shapes import Shape


class Link:
    def __init__(self, text_arg: str, href: Optional[str]):
        """
        Link class for HTML <a> tags

        :param text_arg:
        :param href:
        """
        self.text_arg = text_arg
        self.href = href
        self.shapes: List[Shape] = []

    def svg_content(self) -> str:
        content = f'<a href="{self.href}">'
        for shape in self.shapes:
            content += shape.svg_content()
        content += '</a>'
        return content

    def add_shape(self, shape) -> None:
        self.shapes.append(shape)

