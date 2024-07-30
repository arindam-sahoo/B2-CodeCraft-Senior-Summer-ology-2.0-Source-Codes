# POLYMORPHISM: The ability of a method to behave differently under different situations. We use the same method name for different classes.


class Shape:

  def area(self):
    pass


class Square(Shape):

  def __init__(self, side):
    self.side = side

  def area(self):
    return self.side * self.side

  def __str__(self):
    return "Square"


class Rectangle(Shape):

  def __init__(self, length, breadth):
    self.length = length
    self.breadth = breadth

  def area(self):
    return self.length * self.breadth

  def __str__(self):
    return "Rectangle"


class Triangle(Shape):

  def __init__(self, base, height):
    self.base = base
    self.height = height

  def area(self):
    return 0.5 * self.base * self.height

  def __str__(self):
    return "Triangle"


class Circle(Shape):

  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return 3.14 * self.radius * self.radius

  def __str__(self):
    return "Circle"

class Hexagon(Shape):
  def __init__(self, side):
    self.side = side

  def area(self):
    return (3 * 3**0.5 * self.side * self.side) / 2

  def perimeter(self):
    return self.side * 6

  def __str__(self):
    return "Hexagon"

side = 6
h = Hexagon(side)
print(f"The area of the {h} of side {side} is {h.area()}.")

s = [Square(5), Rectangle(5, 6), Circle(5), Hexagon(6)]
for i in s:
  print("The perimeter of the", i, "is", i.perimeter())


base = 6
height = 4
t = Triangle(base, height)
print("The perimeter of the", t, "is", t.perimeter())


side = 6
s = Square(side)
print(f"The area of the Square of side {side} is {s.area()}.")

length = 6
breadth = 7
r = Rectangle(length, breadth)
print(
    f"The area of the Rectangle of length {length} and breadth {breadth} is {r.area()}."
)

base = 6
height = 5
t = Triangle(base, height)
print(
    f"The area of the Triangle of base {base} and height {height} is {t.area()}."
)

radius = 5
c = Circle(radius)
print(f"The area of the Circle of radius {radius} is {c.area()}.")

# Driver Code using List
s = [Square(5), Rectangle(5, 6), Triangle(6, 7), Circle(5)]
for i in s:
  print("The area of the", i, "is", i.area())
