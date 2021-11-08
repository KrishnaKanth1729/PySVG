# PySVG
## The Python library for generating dynamic SVGs using Python3

Version: 0.0.5

## Installation
```
pip install python-svg
```

Note:
    This library is still under development

Example:
```python
import svg
from svg.canvas import Canvas
from svg.shapes import Rectangle
from svg.server import svg_server

canvas = Canvas(500, 500)
rect1 = Rectangle(200, 100, canvas)
svg_server(canvas=canvas, port=8000)
```

To Access the raw SVG in a form of a string
```python
from svg.canvas import Canvas
from svg.shapes import Rectangle
from svg.server import svg_server

canvas = Canvas(500, 500)
rect1 = Rectangle(200, 100, canvas)

svg_code = canvas.svg_content()
print(svg_code)
```

#### The browser will redirect you to localhost:port and you can see the SVG ouput!

### There will be a RestAPI Version for the same library soon ;)

### By KrishnaKanth1729