class Circle():
    X = 0
    Y = 0
    R = 1
    S = 3.14
    P = 6.28
    def __init__(self, X, Y, R):
        self.X = X
        self.Y = Y
        self.R = R

    def area(self):
        self.S = self.R * 3.14

    def perimeter(self):
        self.P = 2 * 3.14 * self.R

    def scale(self, K):
        self.R *= K

    def is_intersect(self, other):
        if isinstance(other, Circle):
            return (self.X - other.X) ** 2 + (self.Y - other.Y) ** 2 <= (self.R + other.R) ** 2

    def info(self):
        print('Coordinates: X, Y = {}\nSemidiameter: {}\nArea: {} m^2\nPerimeter: {}'.format(
            (self.X, self.Y), self.R, self.S, self.P
        ))

circle_1 = Circle(15, 15, 2)
circle_2 = Circle(1, 1, 1)

circle_1.area()
circle_1.perimeter()
circle_1.info()
if circle_1.is_intersect(circle_2):
    print('Окружности пересекаются')