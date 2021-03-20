from abc import ABC, abstractmethod
import math
from itertools import accumulate
import random

class Shape(ABC):
    
    
    @abstractmethod
    def perimeter ():
        pass
    
    @abstractmethod
    def area():
        pass
        
    def __str__(self):
        return "This is a shape"
    
class Triangle (Shape):
    
    def __init__ (self,sides):
        self.sides = sides
        ac = accumulate(sides)
        for i in range(len(sides)):
            if i == len(sides) -1:
                self.s = next(ac)
            else:
                next(ac)
        
    def area(self):
        s = self.s / 2
        sid = self.sides
        print(sid)
        
        return math.sqrt(s * (s - sid[0]) * (s - sid[1]) *(s - sid[2]))
    
    def perimeter (self):
        return self.s
    
    def __str__(self):
        return super().__str__() + f" And also a triangle with sides : {self.sides}"
    
class Rectangle(Shape):
    
    def __init__(self,side):
        self.side = side
        
    def area (self):
        return self.side * self.side
    
    def perimeter (self):
        return 4 * self.side
    
    def __str__(self):
        return super().__str__() + f" And also a rectangle with side: {self.side}"
    

class Shape_Factory ():
    
    def __init__(self):
        self.shapes = []
        while True:
            
            name = input("Please type desired shape name:")
            if name == "Rectangle":
                self.shapes.append(Rectangle(random.randint(1, 10)))
            elif name == "Triangle":
                self.shapes.append(Triangle([random.randint(20,30) for i in range(3)]))
            else:
                break
            
            
    def __str__(self):
        return str([str(i) for i in self.shapes])
    
Triangle
tr = Triangle([5,12,13])
rec = Rectangle(3)

sf = Shape_Factory()
print(sf)



