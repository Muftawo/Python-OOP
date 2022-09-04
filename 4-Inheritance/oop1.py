class Rectangle:
    def __init__(self, length, width=10,car="car"):
        self.length = length
        self.width = width
        self.car = car
        

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length,car):
        super().__init__(length,car)
        
        
small_square = Square(3,[3])
print(small_square.width )
print(small_square.car )
