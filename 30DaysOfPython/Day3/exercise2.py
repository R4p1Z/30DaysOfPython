import math
# Area and Perimeter of Triangle

'''length = int(input('Enter the length: '))
width = int(input('Enter the width: '))
print('Area of triangle is ', length * width)
'''
# Perimeter of Triangle

'''print('Perimeter of triangle is ', 2*(length+width))'''

# Radius of Circle

'''radius = int(input('Enter a radius of a circle: '))
pi = 3.14
print('The area of the circle is ', pi * radius**2)
print('The circumference of the circle is ', 2 * pi * radius)'''

# Slope and distance

#Find slope of y = 2x - 2

'''m1 = 2 # Since y = mx + b for slope intercept form

x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))
m2 = (y2-y1)/(x2-x1)
u_dist = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
print('The slope of these 2 points are: ', m2)
print('The Euclidean Distance of these 2 points are: ', u_dist)

# Slope comparison
print('Does slope 1 equal to slop 2? : ', m1 == m2)'''

# Find the value of y when y = x^2 + 6x + 9
# Let's see what increment or diminishment of y value will affect y value.

x = 0

while (x != 10):
    y = x**2 + 6*(x) + 9 
    print('This is x towards', x, 'when y =', y)
    x += 1

while (x != -10):
    y = x**2 + 6*(x) + 9 
    print(y)
    print('This is x towards', x, 'when y =', y)
    x -= 1

'''After running x towards 10 and -10 to find a value of x that makes y = 0
The result can be concluded that x = -3 making y = 10.'''
