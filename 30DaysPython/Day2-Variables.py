first_name = "Chaitanya"
last_name = "Prasad"
full_name = "Chaitanya Prasad"
country = "India"
city = "Bangalore"
age = 30
year = 2024
is_married = "No"
is_true = "Yes"
is_light = "Yes"
job, seat_no, colour = "devops", 98, "green"
print(colour)

print(type(last_name))
print(len(full_name))

print(len(first_name) > len(last_name))

if len(first_name) > len(last_name):
    print("FirstName is Greater")
elif len(first_name) < len(last_name):
    print("FIrstName is Lesser")

num_one = 5
num_two = 4
add = num_one + num_two
sub = num_one - num_two
mul = num_one * num_two
div = num_one / num_two
remainder  = num_two % num_one # 4 % 5 = 4 (4 divided by 5 gives remainder 4)
exp = num_one ** num_two # 5^4 = 5 * 5 * 5 * 5 = 625
floor_division = num_one // num_two  # 5 / 4 = 1.25, but floor division removes the decimal part, so the result is 1
print("Addition:", add)
print("Subtration:", sub)
print("Multipication:", mul)
print("Division:", div)
print("Remainder:", remainder)     
print("Exponentiation:", exp)         
print("Floor Division:", floor_division)  

# Area=πr 
# Circumference=2πr

radius = 30
pie = 3.14
area = pie * radius ** 2
circumference = 2 * pie * radius
print("Area", area)
print("Circumference", circumference)

radius_user_input = float(input("Enter the Radius Value:"))
area = pie * radius_user_input ** 2
circumference = 2 * pie * radius_user_input
print("Area of the Circle from the User Input is:", area)

first_name = input("Enter the First Name: ")
last_name = input("Enter the Last Nmae: ")
country = input("Enter the Country Name: ")
age =   int(input("Enter the Age: "))

print("\nUser Information")
print("First Name is", first_name)
print("Last Name is", last_name)
print("Country", country)
print("Age", age)
help("keywords")