class Style:
    def __init__(self, style: dict):
        self.style = style

    def svg(self):
        return f'"{";".join([f"{key}:{value}" for key, value in self.style.items()])}"'