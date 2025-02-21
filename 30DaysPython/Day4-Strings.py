# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string
a = "Thirty"
b = "Days"
c = "Of"
d = "Python"
space = " "
result = a + space + b + space + c + space + d
print(result)  
# Output: Thirty Days Of Python

# 2. Concatenate 'Coding', 'For', 'All' to 'Coding For All'
x = "Coding"
y = "For"
z = "All"
result2 = x + space + y + space + z
print(result2)  
# Output: Coding For All

# 3. Declare a variable company and assign it to "Coding For All"
company = "Coding For All"

# 4. Print the variable company
print(company)  
# Output: Coding For All

# 5. Print the length of the company string
print(len(company))  
# Output: 14

# 6. Convert all characters to uppercase
print(company.upper())  
# Output: CODING FOR ALL

# 7. Convert all characters to lowercase
print(company.lower())  
# Output: coding for all

# 8. Use capitalize(), title(), and swapcase()
print(company.capitalize())  # Output: Coding for all
print(company.title())       # Output: Coding For All
print(company.swapcase())    # Output: cODING fOR aLL

# 9. Slice out the first word "Coding"
sliced_text = company[company.find(" ") + 1:]
print(sliced_text)  
# Output: For All

# 10. Check if "Coding For All" contains "Coding"
print(company.find('Coding'))   # Output: 0
print(company.index("Coding"))  # Output: 0
print("Coding" in company)      # Output: True

# 11. Replace "Coding" with "Python"
new_company = company.replace("Coding", "Python")
print(new_company)  
# Output: Python For All

# 12. Change "Python For All" to "Python For Everyone"
new_company_1 = new_company.replace("All", "Everyone")
print(new_company_1)  
# Output: Python For Everyone

# 13. Split "Coding For All"
print(company.split())  
# Output: ['Coding', 'For', 'All']

# 14. Split a string with commas
x = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(x.split(","))  
# Output: ['Facebook', ' Google', ' Microsoft', ' Apple', ' IBM', ' Oracle', ' Amazon']

# 15. Character at index 0
print(company[0])  
# Output: C

# 16. Last character in "Coding For All"
print(company[-1])  
# Output: l

# 17. Character at index 10
print(company[10])  
# Output: A

# 18. Acronym for "Python For Everyone"
pfa = ''.join([word[0] for word in "Python For Everyone".split()])
print(pfa)  
# Output: PFE

# 19. Acronym for "Coding For All"
cfa = ''.join([word[0] for word in "Coding For All".split()])
print(cfa)  
# Output: CFA

# 20. Position of first occurrence of "C"
print(company.index('C'))  
# Output: 0

# 21. Position of first occurrence of "F"
print(company.index('F'))  
# Output: 7

# 22. Position of last occurrence of 'l' in "Coding For All People"
sentence = "Coding For All People"
print(sentence.rfind('l'))  
# Output: 19

# 23. First occurrence of "because"
sen1 = "You cannot end a sentence with because because because is a conjunction"
print(sen1.index('because'))  
# Output: 31

# 24. Last occurrence of "because"
print(sen1.rindex('because'))  
# Output: 47

# 25. Slice out "because because because"
sliced_sentence = sen1.replace("because because because", "").strip()
print(sliced_sentence)  
# Output: You cannot end a sentence with is a conjunction

# 26. First occurrence of "because"
print(sen1.index("because"))  
# Output: 31

# 27. Slice out "because because because" again
print(sliced_sentence)  
# Output: You cannot end a sentence with is a conjunction

# 28. Does "Coding For All" start with "Coding"?
print(company.startswith("Coding"))  
# Output: True

# 29. Does "Coding For All" end with "coding"?
print(company.endswith("Coding"))  
# Output: False

# 30. Remove left and right trailing spaces
space = "   Coding For All      "
print(space.strip())  
# Output: Coding For All

# 31. Check valid Python identifiers
var1 = "30DaysOfPython"
var2 = "thirty_days_of_python"
print(var1.isidentifier())  # Output: False
print(var2.isidentifier())  # Output: True

# 32. Join list with " # "
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" # ".join(python_libraries))  
# Output: Django # Flask # Bottle # Pyramid # Falcon

# 33. Newline escape sequence
print("I am enjoying this challenge.\nI just wonder what is next.")  
# Output:
# I am enjoying this challenge.
# I just wonder what is next.

# 34. Tab escape sequence
text = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(text)  
# Output:
# Name    Age    Country    City
# Asabeneh    250    Finland    Helsinki

# 35. String formatting for area of a circle
radius = 10
area = 3.14 * radius ** 2
output = f"The area of a circle with radius {radius} is {area} meters square."
print(output)  
# Output: The area of a circle with radius 10 is 314.0 meters square.

# 36. String formatting for calculations
a, b = 8, 6
print(f"{a} + {b} = {a + b}")  # Output: 8 + 6 = 14
print(f"{a} - {b} = {a - b}")  # Output: 8 - 6 = 2
print(f"{a} * {b} = {a * b}")  # Output: 8 * 6 = 48
print(f"{a} / {b} = {a / b:.2f}")  # Output: 8 / 6 = 1.33
print(f"{a} % {b} = {a % b}")  # Output: 8 % 6 = 2
print(f"{a} // {b} = {a // b}")  # Output: 8 // 6 = 1
print(f"{a} ** {b} = {a ** b}")  # Output: 8 ** 6 = 262144
