#1.  Declare your age as integer variable
age = int(200)

#2.  Declare your height as a float variable
height = float (182.6)

#3.  Declare a variable that store a complex number
z = 4+6j
print(z.real)  # Output: 3.0
print(z.imag)  # Output: 4.0

#4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
"""
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
"""
b = int(input("Enter the Base of the Triangle: "))
h = int(input("Enter the Height of the Triangle: "))
results = 0.5 * b * h
print("The Area of the Triangle is: ", results)

#5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
"""
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
"""
a = float(input("Enter the Side A Perimeter of a triangle: "))
b = float(input("Enter the Side B Perimeter of a triangle: "))
c = float(input("Enter the Side C Perimeter of a triangle: "))
results = a + b + c
print("The Permiter of the triangle is", results)

#6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter the length of the Rectangle: "))
width = float(input("Enter the Width of the Rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print("The Area of the Rectagle is: ", area)
print("The Perimeter of the Rectagle is: ", perimeter)

#7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
#pi = 3.14
import math
r = float(input("Entet the Radius of the circle: "))
area = math.pi * r ** r
circumference = 2 * math.pi * r
print("The Area of the Circle is:", area)
print("The Circumference of the Circle is:", circumference)

#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
#9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
#10.    Compare the slopes in tasks 8 and 9.
#11.    Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

#12.    Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("python"))
print(len("dragon"))