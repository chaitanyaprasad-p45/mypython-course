'''
import sys

print(sys.version)

print("Hello World !!")

if 5 < 7:
    print("Number Seven is Greaterthan the Number Five")
else:
    print("Number Five is Lesserthan the Numner Seven")

if 5 > 7:
    print("Number Five is Lesserthan the Number Seven")
else:
    print("Number Seven is Graterthan the nUmber Five")
'''

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random

print(random.randrange(1, 10))