class Rectangle:

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
    
    def surface(self):
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

class Parallelepiped(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        if isinstance(height, float) and length > 0:
            self.__height = height
        else:
            raise Exception("Parallelepiped.__init__(): height should be float > 0")

    def volume(self):
        return self.surface() * self.__height
    
rectangle = Rectangle(10.0,35.0)
print(f"Longueur: {rectangle.get_length()} m")
print(f"Largeur: {rectangle.get_width()} m")
print(f"Périmètre: {rectangle.perimeter()} m")
print(f"Aire: {rectangle.surface()} m^2")
rectangle.set_length(34.0)
rectangle.set_width(9.0)
print(f"Longueur: {rectangle.get_length()} m")
print(f"Largeur: {rectangle.get_width()} m")

parallelepiped = Parallelepiped(10.0,10.0,10.0)
print(f"Volume: {parallelepiped.volume()} m^3")