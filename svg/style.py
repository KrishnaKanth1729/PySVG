class Style:
    def __init__(self, style: dict):
        self.style = style
        self.filter()

    def filter(self):
        for key in self.style.keys():
            pass
            #if key not in self.shape_type.keys:
                #raise ValueError(f"Unexpected Style attribute {key} for Shape {self.shape_type}")

    def svg(self):
        return f'"{";".join([f"{key}:{value}" for key, value in self.style.items()])}"'