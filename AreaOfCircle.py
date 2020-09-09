#Area of Circle with radius provided by user
global a

def Area(r):
    a = 3.141592653589793238 * r ** 2
    return a

r = int(input("Input the radius of circle"))
print("The area of the circle with radius ",r," is", Area(r))
