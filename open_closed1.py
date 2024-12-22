class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        self.kwargs = kwargs

    def area(self):
        if self.shape_type == "rectangle":
            return self.kwargs['width'] * self.kwargs['height']
        elif self.shape_type == "circle":
            return 3.14 * self.kwargs['radius'] ** 2
        else:
            raise ValueError("Unknown shape type")


rectangle = Shape("rectangle", width=10, height=5)
circle = Shape("circle", radius=7)
print(rectangle.area())  
print(circle.area())     
