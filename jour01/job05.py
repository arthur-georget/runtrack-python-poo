class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"x: {self.x} y:{self.y}")
    
    def afficherX(self):
        print(f"x: {self.x}")

    def afficherY(self):
        print(f"y: {self.y}")

    def changerX(self, new_x_value):
        self.x = new_x_value
    
    def changerY(self, new_y_value):
        self.y = new_y_value

point1 = Point(20,10)
point1.afficherLesPoints()
point1.afficherX()
point1.afficherY()
point1.changerX(536)
point1.changerY(234)
point1.afficherLesPoints()