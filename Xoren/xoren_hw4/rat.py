class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = list()
        
    def input_sides(self):
        self.sides = [float(input('Enter side ' + str(i + 1) + ' : ')) for i in range(self.n)]
        
    def disp_sides(self):
        for i in range(self.n):
            print('Side', i+1, 'is', self.sides[i])
            

class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)
        
    def find_area(self):
        a, b, c = self.sides
        #calculate the semi-perimeter
        p = (a + b + c) / 2
        #Heron's formula
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print('The area of the triangle is %s' % area)
        
import math
        
class RightAngledTriangle(Triangle):
    def __init__(self):
        super().__init__()
        
    def input_sides(self):
        self.sides = [float(input('Enter leg ' + str(i + 1) + ': ')) for i in range(self.n - 1)]
        self.sides.append(math.sqrt(self.sides[0] ** 2 + self.sides[1] ** 2))
    
    def find_area(self):
        a, b, c = self.sides
        area = a * b * 0.5
        print('The area of right-angled triangle is %s.' % area)
        
        
rat = RightAngledTriangle()
rat.input_sides()
rat.disp_sides()
rat.find_area()