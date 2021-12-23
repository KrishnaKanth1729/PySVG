from shapes import Rectangle, Circle
from link import Link
from canvas import Canvas
from server import svg_server

canvas = Canvas(500, 500)
link = Link("https://google.com", canvas)
circle = Circle(cx=15, cy=20, r=50, parent=link)
svg_server(canvas)
