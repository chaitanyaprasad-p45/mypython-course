#String variables can be declared either by using single or double quotes:
#
x = "John"
# is the same as
x = 'John'

# Variable names are case-sensitive.
# This will create two variables:
a = 4
A = "Sally"
#A will not overwrite a
print(A)
print(a)

# A variable is created the moment you first assign a value to it.
x = 8
y = "john"
print(x)
print(y)

# In the code, when x is first assigned 4, it becomes an integer. Later, when it is reassigned "Sally", it becomes a string. 
# Python handles this type change automatically without requiring explicit type declarations.
x = 5
x = "john"
print(x)

# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

#You can get the data type of a variable with the type() function.
x = 5
y = "John"
z = 3.14
print(type(x))
print(type(y))
print(type(z))