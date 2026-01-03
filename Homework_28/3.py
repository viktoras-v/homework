class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
rectanlge_1=Rectangle(5,5)
rectanlge_2=Rectangle(5,6)
print(rectanlge_1.area())
print(rectanlge_2.area())
