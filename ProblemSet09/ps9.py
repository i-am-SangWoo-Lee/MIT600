# 6.00 Problem Set 9
#
# Name: SangWoo Lee
# Collaborators: None
# Time: 2022.08.27

from string import *
# from turtle import shape

class Shape(object):
    def area(self):
        # raise AttributeException("Subclasses should override this method.")
        raise AttributeError("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return f"area is {self.base} * {self.height} * 0.5 = {self.base * self.height * 0.5}"
    def __str__(self):
        return f"Triangle with base {self.base} and height {self.height}"
    def __eq__(self, other):
        """
        Two triangles are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Triangle and self.base*self.height == other.base * other.height


#
# Problem 2: Create the ShapeSet class
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet(Shape):
    def __init__(self):
        """
        Initialize any needed variables
        """
        # self.Square = Square
        # self.Circle = Circle
        # self.Triangle = Triangle
        # self.sh = {}
        ## TO DO
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        self.sh = set(list(self.sh).append(sh))
        ## TO DO
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """

        ## TO DO
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        if self == Circle:
            term = 'radius'
        elif self == Square:
            term = 'side'
        elif self == Triangle:
            term = 'side'
        else:
            return -1
        return f"{self} with {term} {self.area}"
        ## TO DO
        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    ## TO DO

#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    ## TO DO


if __name__ == '__main__':
    # a = Triangle(3.0, 4.0)
    # b = Triangle(3.1, 4.1)
    # c = Triangle(3.0, 4.0)
    # print(a.area())
    # print(type(a))
    # print(type(a) == Triangle)
    # print(a.__eq__(b))
    # print(a.__eq__(c))
    d = ShapeSet()
    print(d)