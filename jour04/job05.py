from math import pi

class Shape:

    def area(self):
        return 0

class Rectangle(Shape):

    def __init__(self, length: float, width: float):
        if ( isinstance(length, float) and 
             isinstance(width, float) and
             length > 0 and width >0 ):
            self.__length = length
            self.__width = width
        else:
            raise Exception("Rectangle.__init__(): length and width should be float > 0.")
        
    def perimeter(self):
        return (self.__length + self.__width)*2
    
    def area(self):
        return self.__length * self.__width
    
    def get_length(self):
        return self.__length
    
    def set_length(self, length: float):
        if isinstance(length, float) and length > 0:
            self.__length = length
        else:
            raise Exception("Rectangle.set_length(): length should be float > 0")

    def get_width(self):
        return self.__width

    def set_width(self, width: float):
        if isinstance(width, float) and width > 0:
            self.__width = width
        else:
            raise Exception("Rectangle.set_width(): width should be float > 0")

class Circle(Shape):

    def __init__(self, radius: float):
        if ( isinstance(radius, float) and radius > 0 ):
            self.__radius = radius
        else:
            raise Exception("Circle.__init__(): Radius should be float > 0.")

    def area(self):
        return pi * self.__radius ** 2

rectangle = Rectangle(60.0,60.0)
circle = Circle(30.0)

print(f"Aire rectangle: {rectangle.area()} m^2")
print(f"Aire cercle: {circle.area()} m^2")