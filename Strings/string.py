print("Hello")
print('hello')

# Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")

# Assign String to a Variable
a = "Hello"
print(a)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Strings are Arrays
a = "Hello, World!"
print(a[1])

#Looping Through a String - Loop through the letters in the word "banana":
for x in "banana":
  print(x)

# String Length - The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[4])

# Check String - Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)
# Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Check if NOT - Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)
# Use it in an if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")