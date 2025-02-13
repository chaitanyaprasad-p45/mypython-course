# Python Learning Journey

...(Table of Contents - Same as before)...

## 📖 Topic Descriptions (with Detailed Real-Time Examples)

### 1. Introduction
Overview of Python, its history, and why Python is popular.

### 2. Variables, Built-in Functions
- Variables: Store data. Dynamically typed.
- Built-in Functions: Pre-defined functions.

**Detailed Real-Time Examples:**

1.  **E-commerce Product Price Calculation:**
    ```python
    product_name = "Wireless Headphones"
    price = 99.99
    quantity = 3
    tax_rate = 0.07  # 7% sales tax

    total_cost = (price * quantity) * (1 + tax_rate)

    print(f"Total cost of {quantity} {product_name}: ${total_cost:.2f}") 
    # Output: Total cost of 3 Wireless Headphones: $320.97
    ```

2.  **User Profile Creation:**
    ```python
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email: ")

    user_profile = {
        "name": name,
        "age": age,
        "email": email
    }

    print(user_profile)
    ```

### 3. Operators
- Arithmetic, Comparison, Logical, Assignment.

**Detailed Real-Time Examples:**

1.  **Loan Calculation:**
    ```python
    loan_amount = 10000
    interest_rate = 0.05  # 5% annual interest
    loan_term = 3  # 3 years

    monthly_interest_rate = interest_rate / 12
    num_payments = loan_term * 12

    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**-num_payments)

    print(f"Your monthly payment will be: ${monthly_payment:.2f}")
    ```

2.  **Password Strength Checker:**
    ```python
    password = input("Enter your password: ")

    is_long_enough = len(password) >= 8
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)

    is_strong = is_long_enough and has_uppercase and has_lowercase and has_digit

    if is_strong:
        print("Strong password!")
    else:
        print("Weak password.  Make sure it's at least 8 characters long and includes uppercase, lowercase, and digits.")
    ```

### 4. Strings
- Immutable sequences. String methods.

**Detailed Real-Time Examples:**

1.  **Data Cleaning - Phone Number Formatting:**
    ```python
    phone_number = "  (123) 456-7890  "

    cleaned_number = phone_number.strip().replace("(", "").replace(")", "").replace("-", "").replace(" ", "")

    formatted_number = f"({cleaned_number[:3]}) {cleaned_number[3:6]}-{cleaned_number[6:]}"

    print(formatted_number)  # Output: (123) 456-7890
    ```

2.  **Text Analysis - Word Count:**
    ```python
    text = "This is a sample text. This text contains some words."

    words = text.lower().split()  # Convert to lowercase and split into words

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    print(word_counts)
    ```

### 5. Lists
- Ordered, mutable collections.

**Detailed Real-Time Examples:**

1.  **Inventory Management:**
    ```python
    inventory = []

    while True:
        action = input("Enter action (add, remove, list, quit): ")

        if action == "add":
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory.append({"item": item, "quantity": quantity})
        elif action == "remove":
            item = input("Enter item to remove: ")
            for i in range(len(inventory)):
                if inventory[i]["item"] == item:
                    inventory.pop(i)
                    break
        elif action == "list":
            for item in inventory:
                print(f"{item['item']}: {item['quantity']}")
        elif action == "quit":
            break
        else:
            print("Invalid action.")
    ```

2.  **Student Grade Management:**
    ```python
    students = []

    while True:
      name = input("Enter student name (or 'done'): ")
      if name == 'done':
        break
      grades = []
      while True:
        grade_str = input(f"Enter grade for {name} (or 'done'): ")
        if grade_str == 'done':
          break
        try:
          grade = float(grade_str)
          grades.append(grade)
        except ValueError:
          print("Invalid grade. Please enter a number.")
      students.append({"name": name, "grades": grades})

    for student in students:
      average_grade = sum(student["grades"]) / len(student["grades"]) if student["grades"] else 0
      print(f"{student['name']}: Average Grade = {average_grade:.2f}")
    ```

### 6. Tuples
- Ordered, immutable collections.

**Detailed Real-Time Examples:**

1.  **Representing Geographical Coordinates:**
    ```python
    coordinates = (37.7749, -122.4194)  # San Francisco latitude and longitude

    latitude, longitude = coordinates  # Unpacking the tuple

    print(f"Latitude: {latitude}, Longitude: {longitude}")
    ```

2.  **Returning Multiple Values from a Function:**
    ```python
    def get_student_info(student_id):
        # ... (Code to retrieve student data from database) ...
        name = "Alice"
        major = "Computer Science"
        gpa = 3.8
        return name, major, gpa  # Returning a tuple

    student_name, student_major, student_gpa = get_student_info(123)

    print(f"Student Name: {student_name}, Major: {student_major}, GPA: {student_gpa}")
    ```

### 7. Sets
- Unordered collections of unique elements.

**Detailed Real-Time Examples:**

1.  **Finding Unique Website Visitors:**
    ```python
    visitor_ips = ["192.168.1.1", "10.0.0.1", "192.168.1.1", "172.16.0.1", "10.0.0.1"]

    unique_visitors = set(visitor_ips)

    print(f"Number of unique visitors: {len(unique_visitors)}")
    print(f"Unique visitor IPs: {unique_visitors}")
    ```

2.  **Implementing a Recommendation System (Simplified):**
    ```python
    user_purchases = {"A": {"item1", "item3", "item5"}, "B": {"item2", "item3", "item6"}}

    def recommend_items(user_id):
        purchased_items = user_purchases.get(user_id, set())  # Get user's purchased items or empty set
        all_items = set()
        for items in user_purchases.values():
          all_items.update(items)
        other_items = all_items - purchased_items
        return other_items

    recommendations = recommend_items("A")
    print(f"Recommended items for user A: {recommendations}")
    ```

### 8. Dictionaries
- Key-value mappings.

**Detailed Real-Time Examples:**

1.  **Contact Management System:**
    ```python
    contacts = {}

    while True:
        name = input("Enter contact name (or 'done'): ")
        if name == 'done':
            break
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        contacts[name] = {"phone": phone, "email": email}

    while True:
      search_name = input("Enter name to search (or 'done'): ")
      if search_name == 'done':
        break
      contact_info = contacts.get(search_name)
      if contact_info:
        print(f"Phone: {contact_info['phone']}, Email: {contact_info['email']}")
      else:
        print("Contact not found.")
    ```

2.  **E-commerce Product Catalog:**
    ```python
    products = {
        "123": {"name": "Laptop", "price": 999.99, "category": "Electronics"},
        "456": {"name": "Smartphone", "price": 799.99, "category": "Electronics"},
        "789": {"name": "T-shirt", "price": 29.99, "category": "Clothing"},
    }

    product_id = input("Enter product ID: ")
    product = products.get(product_id)

    if product:
        print(f"Product Name: {product['name']}")
        print(f"Price: ${product['price']:.2f}")
        print(f"Category: {product['category']}")
    else:
        print("Product not found.")
    ```

### 9. Conditionals
- `if`, `elif`, `else` statements.

**Detailed Real-Time Examples:**

1.  **Automated System for Temperature Control:**
    ```python
    current_temp = float(input("Enter current temperature (Celsius): "))
    target_temp = 22  # Desired room temperature

    if current_temp < target_temp:
        print("Turning on the heater.")
    elif current_temp > target_temp:
        print("Turning on the air conditioning.")
    else:
        print("Temperature is perfect.")

    # Add more sophisticated logic based on time of day, outside temperature, etc.
    ```

2.  **Decision-Making in a Game:**
    ```python
    player_health = 80
    enemy_health = 50

    if player_health > enemy_health:
        print("Attack the enemy!")
    elif player_health < enemy_health:
        print("Flee and heal!")
    else:
        print("Prepare for a fierce battle!")

    # Add more complex game logic, including special abilities, items, etc.
    ```

### 10. Loops
- `for` and `while` loops.

**Detailed Real-Time Examples:**

1.  **Processing Data from a CSV File:**
    ```python
    import csv

    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            # Process each row of data
            name = row[0]
            age = int(row[1])
            # ... perform calculations or other operations ...
            print(f"Name: {name}, Age: {age}")
    ```

2.  **Simulating a User Authentication System:**
    ```python
    username = "admin"
    password = "password123"
    attempts = 3

    while attempts > 0:
        entered_username = input("Enter username: ")
        entered_password = input("Enter password: ")

        if entered_username == username and entered_password == password:
            print("Login successful!")
            break
        else:
            attempts -= 1
            print(f"Incorrect username or password. {attempts} attempts remaining.")

    if attempts == 0:
        print("Login failed. Too many attempts.")
    ```

### 11. Functions
- Reusable blocks of code.

**Detailed Real-Time Examples:**

1.  **Calculating the Area and Perimeter of a Rectangle:**
    ```python
    def calculate_rectangle_properties(length, width):
        area = length * width
        perimeter = 2 * (length + width)
        return area, perimeter

    length = 10
    width = 5
    area, perimeter = calculate_rectangle_properties(length, width)

    print(f"Area: {area}, Perimeter: {perimeter}")
    ```

2.  **Data Validation Function:**
    ```python
    def validate_email(email):
      if "@" not in email or "." not in email:
        return False
      return True

    email = input("Enter email: ")
    if validate_email(email):
      print("Valid email")
    else:
      print("Invalid email")

    ```

### 12. Modules
- Collections of functions and variables.

**Detailed Real-Time Examples:**

1.  **Using the `random` module to generate a lottery number:**
    ```python
    import random

    def generate_lottery_number():
        numbers = random.sample(range(1, 50), 6)  # Choose 6 unique numbers between 1 and 49
        return numbers

    lottery_number = generate_lottery_number()
    print(f"Your lottery number: {lottery_number}")
    ```

2.  **Using the `datetime` module to calculate the time difference between two events:**
    ```python
    import datetime

    event1_time = datetime.datetime(2024, 1, 1, 10, 0, 0)  # January 1st, 2024, 10:00 AM
    event2_time = datetime.datetime(2024, 1, 1, 12, 30, 0)  # January 1st, 2024, 12:30 PM

    time_difference = event2_time - event1_time

    print(f"Time difference: {time_difference}")
    ```

### 13. List Comprehension
- Concise way to create lists.

**Detailed Real-Time Examples:**

1.  **Extracting all the words longer than 5 characters from a sentence:**
    ```python
    sentence = "This is a sample sentence with some long words."

    long_words = [word for word in sentence.split() if len(word) > 5]

    print(long_words)  # Output: ['sample', 'sentence', 'words.']
    ```

2.  **Creating a list of tuples containing the square and cube of each number from 1 to 10:**
    ```python
    numbers = [(x**2, x**3) for x in range(1, 11)]

    print(numbers)
    ```

### 14. Higher Order Functions
- Functions that take other functions as arguments or return functions.

**Detailed Real-Time Examples:**

1.  **Using `map` to apply a function to each element of a list:**
    ```python
    numbers = [1, 2, 3, 4, 5]

    squared_numbers = list(map(lambda x: x**2, numbers))

    print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
    ```

2.  **Using `filter` to filter a list based on a condition:**
    ```python
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    print(even_numbers)  # Output: [2, 4, 6, 8, 10]
    ```

### 15. Type Errors
- Occur when an operation is performed on an object of the wrong type.

**Detailed Real-Time Examples:**

1.  **Trying to add a string and an integer:**
    ```python
    age = 25
    message = "Your age is: "

    # result = message + age  # This will cause a TypeError

    # Correct way:
    result = message + str(age)
    print(result)  # Output: Your age is: 25
    ```

2.  **Trying to access a list element using a string index:**
    ```python
    my_list = [10, 20, 30]

    # element = my_list["1"]  # This will cause a TypeError

    # Correct way:
    element = my_list[1]
    print(element)  # Output: 20
    ```

### 16. Date Time
- Working with dates and times using the `datetime` module.

**Detailed Real-Time Examples:**

1.  **Calculating the age of a person given their birthdate:**
    ```python
    import datetime

    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d").date()  # Parse the date string

    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    print(f"You are {age} years old.")
    ```

2.  **Formatting dates in different ways:**
    ```python
    import datetime

    now = datetime.datetime.now()

    print(now.strftime("%Y-%m-%d %H:%M:%S"))  # YYYY-MM-DD HH:MM:SS
    print(now.strftime("%m/%d/%Y"))  # MM/DD/YYYY
    print(now.strftime("%A, %B %d, %Y"))  # Day of the week, Month Day, Year
    ```

### 17. Exception Handling
- Using `try`, `except`, `finally` blocks to handle errors.

**Detailed Real-Time Examples:**

1.  **Handling file reading errors:**
    ```python
    try:
        with open("myfile.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")
    except Exception as e:  # Catch other potential errors
        print(f"An error occurred: {e}")
    finally:
        print("This will always be executed, even if an exception occurs.")
    ```

2.  **Handling invalid user input:**
    ```python
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
              raise ValueError("Age cannot be negative") # Raise custom exception
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
          print(f"An unexpected error occurred: {e}")

    print(f"Your age is: {age}")
    ```

### 18. Regular Expressions
- Pattern matching using the `re` module.

**Detailed Real-Time Examples:**

1.  **Extracting email addresses from a text:**
    ```python
    import re

    text = "Contact us at info@example.com or support@example.net for any inquiries."

    email_addresses = re.findall(r"[^@]+@[^@]+\.[^@]+", text)

    print(email_addresses)  # Output: ['info@example.com', 'support@example.net']
    ```

2.  **Validating a password:**
    ```python
    import re

    def is_valid_password(password):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        # Explanation:
        # ^: Matches the beginning of the string.
        # (?=.*[a-z]): Positive lookahead assertion. Ensures that the string contains at least one lowercase letter.
        # (?=.*[A-Z]): Positive lookahead assertion. Ensures that the string contains at least one uppercase letter.
        # (?=.*\d): Positive lookahead assertion. Ensures that the string contains at least one digit.
        # (?=.*[@$!%*?&]): Positive lookahead assertion. Ensures that the string contains at least one special character from the set [@$!%*?&].
        # [A-Za-z\d@$!%*?&]{8,}: Matches 8 or more characters from the set of uppercase letters, lowercase letters, digits, and special characters.
        # $: Matches the end of the string.
        return bool(re.match(pattern, password))

    password = input("Enter your password: ")
    if is_valid_password(password):
        print("Valid password.")
    else:
        print("Invalid password.  Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
    ```

### 19. File Handling
- Reading and writing files.

**Detailed Real-Time Examples:**

1.  **Reading data from a CSV file and calculating the average score:**
    ```python
    import csv

    def calculate_average_score(filename):
        total_score = 0
        count = 0
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row (if it exists)
                for row in reader:
                    try:
                        score = int(row[1])  # Assuming the score is in the second column
                        total_score += score
                        count += 1
                    except ValueError:
                        print(f"Invalid score: {row[1]}. Skipping this row.")
            if count > 0:
              return total_score/count
            else:
              return 0
        except FileNotFoundError:
            print("File not found.")
            return 0

    average_score = calculate_average_score("student_scores.csv")
    print(f"Average score: {average_score}")
    ```

2.  **Writing data to a JSON file:**
    ```python
    import json

    data = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }

    with open("user_data.json", "w") as file:
        json.dump(data, file, indent=4)  # Use indent for pretty printing
    ```

### 20. Package Manager (pip)
- Installing and managing Python packages.

**Detailed Real-Time Examples:**

1.  **Installing a specific version of a package:**
    ```bash
    pip install requests==2.28.1
    ```

2.  **Installing a package from a requirements file:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Upgrading all installed packages:**
    ```bash
    pip freeze --local | grep -v '^-e' | cut -d = -f 1  | xargs -n1 pip install -U
    ```

### 21. Classes and Objects
- Object-oriented programming.

**Detailed Real-Time Examples:**

1.  **Creating a `BankAccount` class:**
    ```python
    class BankAccount:
        def __init__(self, account_number, balance=0):
            self.account_number = account_number
            self.balance = balance

        def deposit(self, amount):
            self.balance += amount
            return self.balance

        def withdraw(self, amount):
            if amount > self.balance:
                return "Insufficient funds"
            self.balance -= amount
            return self.balance

        def get_balance(self):
            return self.balance

    my_account = BankAccount("1234567890", 1000)
    my_account.deposit(500)
    my_account.withdraw(200)
    print(f"Current balance: {my_account.get_balance()}")
    ```

2.  **Creating a `ShoppingCart` class:**
    ```python
    class ShoppingCart:
        def __init__(self):
            self.items = []

        def add_item(self, item, quantity):
            self.items.append({"item": item, "quantity": quantity})

        def remove_item(self, item):
            for i in range(len(self.items)):
                if self.items[i]["item"] == item:
                    self.items.pop(i)
                    return
            print("Item not found in cart.")

        def calculate_total(self):
            total = 0
            for item in self.items:
                # Assuming each item has a price attribute
                total += item["item"].price * item["quantity"] # Example: item is Product object
            return total

        def display_items(self):
          for item in self.items:
            print(f"{item['item'].name} x {item['quantity']}") # Example: item is Product object

    # Example Product class (would be defined elsewhere)
    class Product:
      def __init__(self, name, price):
        self.name = name
        self.price = price

    cart = ShoppingCart()
    product1 = Product("Laptop", 999)
    product2 = Product("Mouse", 25)
    cart.add_item(product1, 1)
    cart.add_item(product2, 2)
    cart.display_items()
    print(f"Total: ${cart.calculate_total()}")
    cart.remove_item(product1)
    cart.display_items()
    print(f"Total: ${cart.calculate_total()}")

    ```

### 22. Web Scraping
- Extracting data from websites.

**Detailed Real-Time Examples:**

1.  **Scraping product information from an e-commerce website:**
    ```python
    import requests
    from bs4 import BeautifulSoup

    def scrape_product_info(url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

            soup = BeautifulSoup(response.content, "html.parser")

            name = soup.find("h1", class_="product-title").text.strip() # Example class name, inspect website
            price_str = soup.find("span", class_="price").text.strip() # Example class name, inspect website
            price = float(price_str.replace("$", "").replace(",", "")) # Clean the price string
            description = soup.find("div", class_="product-description").text.strip() # Example class, inspect website

            return {
                "name": name,
                "price": price,
                "description": description,
            }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL: {e}")
            return None
        except AttributeError as e: # Handle cases where elements are not found
            print(f"Error parsing HTML: {e}.  Check website structure.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    product_url = "https://www.example-ecommerce-site.com/product/123" # Replace with actual URL
    product_info = scrape_product_info(product_url)

    if product_info:
        print(product_info)
    ```

2.  **Scraping news headlines from a news website:**
    ```python
    import requests
    from bs4 import BeautifulSoup

    def scrape_news_headlines(url):
        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")

            headlines = []
            for headline_tag in soup.find_all("h2", class_="headline"): # Example class, inspect website
                headline = headline_tag.text.strip()
                headlines.append(headline)

            return headlines
        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL: {e}")
            return None
        except AttributeError as e: # Handle cases where elements are not found
            print(f"Error parsing HTML: {e}.  Check website structure.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    news_url = "https://www.example-news-site.com"  # Replace with actual URL
    headlines = scrape_news_headlines(news_url)

    if headlines:
        for headline in headlines:
            print(headline)
    ```

### 23. Virtual Environment
- Creating isolated Python environments.

**Detailed Real-Time Examples:**

1.  **(Setting up a virtual environment for a web project):**
    ```bash
    # Create the virtual environment
    python3 -m venv .venv  # Or python -m venv .venv on some systems

    # Activate the virtual environment (Linux/macOS)
    source .venv/bin/activate

    # Activate the virtual environment (Windows)
    .venv\Scripts\activate

    # Install project dependencies
    pip install Flask requests beautifulsoup4

    # Deactivate the virtual environment
    deactivate
    ```

2.  **(Using a virtual environment for a data science project):**
    ```bash
    # Create the virtual environment
    python3 -m venv data_env

    # Activate the virtual environment (Linux/macOS)
    source data_env/bin/activate

    # Activate the virtual environment (Windows)
    data_env\Scripts\activate

    # Install data science libraries
    pip install numpy pandas matplotlib scikit-learn

    # Deactivate the virtual environment
    deactivate
    ```

### 24. Statistics
- Basic statistical functions.

**Detailed Real-Time Examples:**

1.  **Analyzing student test scores:**
    ```python
    import statistics

    test_scores = [85, 92, 78, 90, 88, 75, 95]

    mean_score = statistics.mean(test_scores)
    median_score = statistics.median(test_scores)
    mode_score = statistics.mode(test_scores) # Raises StatisticsError if no unique mode. Handle with try/except
    stdev_score = statistics.stdev(test_scores)

    print(f"Mean score: {mean_score}")
    print(f"Median score: {median_score}")
    try:
        print(f"Mode score: {mode_score}")
    except statistics.StatisticsError:
        print("No unique mode found.")
    print(f"Standard deviation: {stdev_score}")
    ```

2.  **Calculating the correlation coefficient between two variables:**
    ```python
    import statistics

    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 6]

    correlation = statistics.correlation(x, y)

    print(f"Correlation coefficient: {correlation}")
    ```

### 25. Pandas
- Data manipulation and analysis.

**Detailed Real-Time Examples:**

1.  **Analyzing sales data from a CSV file:**
    ```python
    import pandas as pd

    # Read the sales data from a CSV file
    sales_data = pd.read_csv("sales.csv")

    # Calculate total sales for each region
    region_sales = sales_data.groupby("Region")["Sales"].sum()

    # Calculate the average sales amount
    average_sales = sales_data["Sales"].mean()

    # Find the top-selling product
    top_product = sales_data.loc[sales_data["Sales"].idxmax()]

    print("Sales by Region:\n", region_sales)
    print("\nAverage Sales:", average_sales)
    print("\nTop Selling Product:\n", top_product)

    ```

2.  **Cleaning and transforming data in a DataFrame:**
    ```python
    import pandas as pd

    data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
            'Age': [25, 30, None, 28, 22],
            'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney']}
    df = pd.DataFrame(data)

    # Fill missing values
    df['Age'].fillna(df['Age'].mean(), inplace=True) # Fill with mean age
    df['Name'].fillna('Unknown', inplace=True) # Fill with 'Unknown'
    df.dropna(subset=['City'], inplace=True) # Remove rows with missing City

    # Convert age to integer
    df['Age'] = df['Age'].astype(int)

    print(df)
    ```

### 26. Python Web (Flask/FastAPI)
- Building web applications.

**Detailed Real-Time Examples (Flask):**

1.  **(Creating a simple web application to display a list of products):**
    ```python
    from flask import Flask, render_template

    app = Flask(__name__)

    products = [
        {"name": "Laptop", "price": 999.99},
        {"name": "Smartphone", "price": 799.99},
        {"name": "Tablet", "price": 299.99},
    ]

    @app.route("/")
    def index():
        return render_template("index.html", products=products)

    if __name__ == "__main__":
        app.run(debug=True)
    ```

    `index.html`:
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Product List</title>
    </head>
    <body>
        <h1>Products</h1>
        <ul>
            {% for product in products %}
            <li>{{ product.name }} - ${{ product.price }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    ```

2.  **(Creating a web application to handle user input from a form):**
    ```python

    from flask import Flask, render_template, request

    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def index():
        message = None
        if request.method == "POST":
            name = request.form.get("name")
            email = request.form.get("email")
            message = f"Hello, {name}! Your email is {email}."

        return render_template("index.html", message=message)

    if __name__ == "__main__":
        app.run(debug=True)
    ```

    `index.html`:
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>User Input</title>
    </head>
    <body>
        <h1>Enter Your Information</h1>
        <form method="POST">
            Name: <input type="text" name="name"><br>
            Email: <input type="email" name="email"><br>
            <input type="submit" value="Submit">
        </form>
        {% if message %}
        <p>{{ message }}</p>
        {% endif %}
    </body>
    </html>
    ```

### 27. Python with MongoDB
- Interacting with MongoDB databases.

**Detailed Real-Time Examples:**

1.  **(Storing and retrieving user data):**
    ```python
    from pymongo import MongoClient

    client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string
    db = client["mydatabase"]  # Replace with your database name
    collection = db["users"]  # Replace with your collection name

    def create_user(name, email):
        user = {"name": name, "email": email}
        result = collection.insert_one(user)
        return result.inserted_id

    def get_user(user_id):
        user = collection.find_one({"_id": user_id})
        return user

    # Example usage:
    user_id = create_user("Alice", "alice@example.com")
    retrieved_user = get_user(user_id)
    print(retrieved_user)

    # Find all users
    for user in collection.find():
      print(user)
    ```

2.  **(Storing and retrieving product data):**
    ```python
    # ... (same client and db setup as above)

    product_collection = db["products"]

    def create_product(name, price, category):
        product = {"name": name, "price": price, "category": category}
        result = product_collection.insert_one(product)
        return result.inserted_id

    def get_product(product_id):
        product = product_collection.find_one({"_id": product_id})
        return product

    # Example usage:
    product_id = create_product("Laptop", 999.99, "Electronics")
    retrieved_product = get_product(product_id)
    print(retrieved_product)
    ```

### 28. API
- Application Programming Interface.

### 29. Building API (Flask/FastAPI)
- Creating RESTful APIs.

**Detailed Real-Time Examples (Flask):**

1.  **(Creating a REST API for a to-do list):**
    ```python
    from flask import Flask, jsonify, request

    app = Flask(__name__)

    tasks = []  # In-memory storage for tasks (replace with database later)

    @app.route("/tasks", methods=["GET"])
    def get_tasks():
        return jsonify(tasks)

    @app.route("/tasks", methods=["POST"])
    def create_task():
        data = request.get_json()
        task = {"id": len(tasks) + 1, "title": data["title"], "completed": False}
        tasks.append(task)
        return jsonify(task), 201  # 201 Created status code

    @app.route("/tasks/<int:task_id>", methods=["PUT"])
    def update_task(task_id):
        data = request.get_json()
        for task in tasks:
            if task["id"] == task_id:
                task["title"] = data.get("title", task["title"])  # Update title if provided
                task["completed"] = data.get("completed", task["completed"])  # Update completed status
                return jsonify(task)
        return jsonify({"message": "Task not found"}), 404  # 404 Not Found

    @app.route("/tasks/<int:task_id>", methods=["DELETE"])
    def delete_task(task_id):
        for i in range(len(tasks)):
            if tasks[i]["id"] == task_id:
                tasks.pop(i)
                return jsonify({"message": "Task deleted"})
        return jsonify({"message": "Task not found"}), 404

    if __name__ == "__main__":
        app.run(debug=True)
    ```

2.  **(Creating a REST API for a blog):**  (This example would be significantly more complex, involving database integration, user authentication, etc.  I'll provide a simplified structure)

    ```python
    # ... (Flask app setup)

    @app.route("/posts", methods=["GET"])
    def get_posts():
        # ... (Code to retrieve blog posts from database)
        return jsonify(posts)

    @app.route("/posts", methods=["POST"])
    def create_post():
        # ... (Code to create a new blog post in database)
        return jsonify(new_post), 201

    # ... (Similar routes for updating and deleting posts)
    ```

### 30. Conclusions
- Summary of the learning journey.
- Next steps: Explore advanced topics, build projects, contribute to open source.

## 🚀 How to Use This Guide
- Click on any topic to explore detailed explanations and examples.
- Follow along by writing code and experimenting.
- Complete exercises in each section to reinforce learning.

Happy Learning! 🎯