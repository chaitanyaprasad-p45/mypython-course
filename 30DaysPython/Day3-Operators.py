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

#13.    Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "python" and "on" in "dragon") # use the in operator along with and to check if "on" is present in both "python" and "dragon"

#14.    I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
print("jargon" in sentence)

#15.    There is no 'on' in both dragon and python
print("on" not in "dragon" and "on" not in "python")

#16.    Find the length of the text python and convert the value to float and convert it to string
text = "python"
print(len(text))
print(float(len(text)))
print(str(len(text)))

"""
text = "python"

# Finding the length
length = len(text)
print(length)  # Output: 6

# Converting to float
length_float = float(length)
print(length_float)  # Output: 6.0

# Converting to string
length_str = str(length)
print(length_str)  # Output: "6"
"""

#17.    Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
x = int(input("Enter the Value: "))
if x % 2 == 0:
    print("This is a EVEN Number")
else:
    print("This is a ODD Number")

#18.    Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
x = 7
y = 3
results = x // y
converted_value = int(2.7)          # Convert 2.7 to an integer
print(results == converted_value)    # Check if they are equal

#19.    Check if type of '10' is equal to type of 10
print(type('10') == type(10))

#20.    Check if int('9.8') is equal to 10
print(type(float('9.8')) == type(10))

#21.    Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
x = int(input("Enter Hours: "))
y = int(input("Enter Rate per Hour: "))
z = x * y
print("Your weekly earning is", z)

#22.    Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
max_years = 100
#(75×365)+(25×366)/100=365.25 days per year
sec_in_year = 365.25 * 24 * 60 * 60
x = int(input("Enter the Years you have lived: "))
results = x * sec_in_year
print("You have lived for", int(results), "seconds")

#23.     Write a Python script that displays the following table
"""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
print("Number1", "1", "Number2", "Number3")
for i in range (1, 6):
    print(i, 1, i**2, i**3)

"""
print(f"{'Number':<8} {'1':<8} {'Number²':<8} {'Number³':<8}")

for i in range(1, 6):
    print(f"{i:<8} {1:<8} {i**1:<8} {i**2:<8} {i**3:<8}")
#   <8 means left-align text in a column 8 spaces wide for a structured look.
"""
