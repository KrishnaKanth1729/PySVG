from ..style import Style


class Circle:
    def __init__(self, cx: int, cy: int, r: int, style: Style, stroke_width:int =None, fill:str =None):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.style = style
        self.stroke_width = stroke_width
        self.fill = fill
