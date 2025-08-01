"""
Q-1: Rectangle Class
Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.

Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.

Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
"""
class Rectangle:
  def __init__(self,l,b):
    self.__length = l 
    self.__width = b

  def __perimeter(self):
    return 2*(self.__length + self.__width)

  def __area(self):
    return self.__length * self.__width

  def display(self):
    print("length",self.__length)
    print("breadth",self.__width)
    print("perimeter",self.__perimeter())
    print("area",self.__area()) 

obj = Rectangle(3,5) 
obj.display()