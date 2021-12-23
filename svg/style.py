class Style:
    def __init__(self, style: dict):
        self.style = style

    def filter(self):
        # TODO: to add more known attributes
        known_attributes = ['fill', 'stroke', 'stroke-width', 'fill-rule']
        for key in self.style.keys():
            if key not in known_attributes:
                raise Warning("Attribute {key} is not a known style property")

    def svg(self):
        return f'"{";".join([f"{key}:{value}" for key, value in self.style.items()])}"'
