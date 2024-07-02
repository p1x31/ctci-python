class Point:

    #class atributes
    color = "red"
    radius = 2

    #constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

Point.color = "blue"
print(Point.color)
print(Point.__dict__)
a = Point(1, 2)
print(isinstance(a, Point))
print(type(a))