import math


class Circle:

    def __init__(self, area):
        self.area = area

    @classmethod
    def create_by_radius(cls, radius):
        return cls(math.pi * (radius**2))

    @classmethod
    def create_by_diameter(cls, diameter):
        return cls(math.pi / 4 * (diameter**2))

    def __repr__(self):
        return f"I'm circle with area equal {self.area}"

    def __add__(self, other):
        if isinstance(other, Circle):
            self.area += other.area
        else:
            raise Exception('You can added only circles!')

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.area == other.area
        else:
            raise Exception('You can compare only circles!')

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.area < other.area
        else:
            raise Exception('You can compare only circles!')

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.area > other.area
        else:
            raise Exception('You can compare only circles!')


circle_1 = Circle.create_by_radius(5)
circle_2 = Circle.create_by_diameter(15)
circle_3 = Circle.create_by_diameter(15)
print(circle_1)
print(circle_2)

circle_1 + circle_2
print(circle_1)

if circle_1 > circle_2:
    print('Circle 1 bigger than cirle 2')

if circle_1 < circle_2:
    print('Circle 2 bigger than cirle 1')

if circle_3 == circle_2:
    print('Circle 2 and cirle 3 are equal')

circle_2 + circle_3
list_circles = [circle_1, circle_2, circle_3]
list_circles.sort()
print(list_circles)
