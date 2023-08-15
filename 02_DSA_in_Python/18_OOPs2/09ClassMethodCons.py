class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    
    @classmethod
    def create_square(cls, side_length):
        return cls(side_length, side_length)
    

obj = Rectangle(3, 5)
print(obj.height, obj.width)

sqr = Rectangle.create_square(12)
print(sqr.height, sqr.width)