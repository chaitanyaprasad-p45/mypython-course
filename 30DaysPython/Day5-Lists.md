#   Lists
There are four collection data types in Python :

*   **List:** is a collection which is ordered and changeable(modifiable). Allows duplicate members.
*   **Tuple:** is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
*   **Set:** is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
*   **Dictionary:** is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.

A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.

##  How to Create a List

In Python we can create lists in two ways:
*   Using list built-in function
```python
# syntax
lst = list()
empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0
```
*   Using square brackets, []
```python
# syntax
lst = []
empty_list = [] # this is an empty list, no item in the list
print(len(empty_list)) # 0
```

Lists with initial values. We use len() to find the length of a list.
```python
fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
```
```python
# Print the lists and its length
print('Fruits:', fruits)                                        #   Fruits: ['banana', 'orange', 'mango', 'lemon']
print('Number of fruits:', len(fruits))                         #   Number of fruits: 4
print('Vegetables:', vegetables)                                #   Vegetables: ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
print('Number of vegetables:', len(vegetables))                 #   Number of vegetables: 5
print('Animal products:',animal_products)                       #   Animal products: ['milk', 'meat', 'butter', 'yoghurt']
print('Number of animal products:', len(animal_products))       #   Number of animal products: 4
print('Web technologies:', web_techs)                           #   Web technologies: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
print('Number of web technologies:', len(web_techs))            #   Number of web technologies: 7
print('Countries:', countries)                                  #   Countries: ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
print('Number of countries:', len(countries))                   #   Number of countries: 5
```

*   Lists can have items of different data types
```python
lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types
```
---
##  Accessing List Items Using Positive Indexing
We access each item in a list using their index. A list index starts from 0. The picture below shows clearly where the index starts

```python
fruits = ['banana', 'orange', 'mango', 'lemon'] # [0, 1, 2, 3]
first_fruit = fruits[0]                         # we are accessing the first item using its index
print(first_fruit)                              # banana
second_fruit = fruits[1]
print(second_fruit)                             # orange
last_fruit = fruits[3]
print(last_fruit)                               # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
```

##  Accessing List Items Using Negative Indexing
Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item.
```python
fruits = ['banana', 'orange', 'mango', 'lemon']     #   [-4, -3, -2, -1]
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)                                  #   banana
print(last_fruit)                                   #   lemon
print(second_last)                                  #   mango
```
---

##  Unpacking List Items

```python
# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits 
print(first_fruit)      # banana
print(second_fruit)     # orange
print(third_fruit)      # mango
print(rest)             # ['lemon','lime','apple']
# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)            # 1
print(second)           # 2
print(third)            # 3
print(rest)             # [4,5,6,7,8,9]
print(tenth)            # 10
# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)               # Germany
print(fr)               # France
print(bg)               # Belgium
print(sw)               # Sweden
print(scandic)          # ['Denmark', 'Finland', 'Norway', 'Iceland']
print(es)               # Estonia
```
---

##  Slicing Items from a List
```python
fruits = ['banana', 'orange', 'mango', 'lemon']
```

*   Positive Indexing: We can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list. (default values for start = 0, end = len(lst) - 1 (last item), step = 1)

| Index | 0      | 1      | 2      | 3      |
|-------|--------|--------|--------|--------|
| Fruit | banana | orange | mango  | lemon  |

*   Negative Indexing: We can specify a range of negative indexes by specifying the start, end and step, the return value will be a new list.

| Index | -4     | -3     | -2     | -1     |
|-------|--------|--------|--------|--------|
| Fruit | banana | orange | mango  | lemon  |

| Slice         | Output                          | Explanation |
|--------------|--------------------------------|-------------|
| `fruits[0:4]` | `['banana', 'orange', 'mango', 'lemon']` | Extract all elements using positive indexes. |
| `fruits[1:3]` | `['orange', 'mango']` | Extract elements from index `1` to `2` (excluding `3`). |
| `fruits[1:]` | `['orange', 'mango', 'lemon']` | Extract all elements from index `1` to end. |
| `fruits[::2]` | `['banana', 'mango']` | Extract every second element. |
| `fruits[-4:]` | `['banana', 'orange', 'mango', 'lemon']` | Extract all elements using negative indexes. |
| `fruits[-3:-1]` | `['orange', 'mango']` | Extract elements from index `-3` to `-2` (excluding `-1`). |
| `fruits[-3:]` | `['orange', 'mango', 'lemon']` | Extract all elements from index `-3` to end. |
| `fruits[::-1]` | `['lemon', 'mango', 'orange', 'banana']` | Reverse the list. |
---

##  Modifying Lists

List is a mutable or modifiable ordered collection of items. Lets modify the fruit list.
```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']
```

##  Checking Items in a List

Checking an item if it is a member of a list using in operator. See the example below.

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False
```

##  Adding Items to a List

Adding Items to a List

```python
# syntax
lst = list()
lst.append(item)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)
```

##  Inserting Items into a List

We can use insert() method to insert a single item at a specified index in a list. Note that other items are shifted to the right. The insert() methods takes two arguments:index and an item to insert.

```python
# syntax
lst = ['item1', 'item2']
lst.insert(index, item)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)
```
##  Removing Items from a List

The remove method removes a specified item from a list
```python
# syntax
lst = ['item1', 'item2']
lst.remove(item)

fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']
```

##  Removing Items Using Pop

The pop() method removes the specified index, (or the last item if index is not specified):

```python
# syntax
lst = ['item1', 'item2']
lst.pop()       # last item
lst.pop(index)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']
```

##  Removing Items Using Del

The del keyword removes the specified index and it can also be used to delete items within index range. It can also delete the list completely

```python
# syntax
lst = ['item1', 'item2']
del lst[index] # only a single item
del lst        # to delete the list completely

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)       # ['orange', 'lime']
del fruits
print(fruits)       # This should give: NameError: name 'fruits' is not defined
```

##  Clearing List Items

The clear() method empties the list:

```python
# syntax
lst = ['item1', 'item2']
lst.clear()

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []
```

##  Copying a List

It is possible to copy a list by reassigning it to a new variable in the following way: list2 = list1. Now, list2 is a reference of list1, any changes we make in list2 will also modify the original, list1. But there are lots of case in which we do not like to modify the original instead we like to have a different copy. One of way of avoiding the problem above is using copy().

```python
# syntax
lst = ['item1', 'item2']
lst_copy = lst.copy()

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
```

##  Joining Lists

There are several ways to join, or concatenate, two or more lists in Python.

*   Plus Operator (+)
```python
# syntax
list3 = list1 + list2

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

*   Joining using extend() method The extend() method allows to append list in a list. See the example below.
```python
# syntax
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)

num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits ) # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

##  Counting Items in a List

The `count()` method returns the number of times an item appears in a list:
```python
# syntax
lst = ['item1', 'item2']
lst.count(item)

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3
```

##  Finding Index of an Item

The `index()` method returns the index of an item in the list:
```python
# syntax
lst = ['item1', 'item2']
lst.index(item)

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, the first occurrence
```

##  Reversing a List

The `reverse()` method reverses the order of a list.
```python
# syntax
lst = ['item1', 'item2']
lst.reverse()

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) # [24, 25, 24, 26, 25, 24, 19, 22]
```

##  Sorting List Items

To sort lists we can use sort() method or sorted() built-in functions. The sort() method reorders the list items in ascending order and modifies the original list. If an argument of sort() method reverse is equal to true, it will arrange the list in descending order.

*   **sort():** this method modifies the original list
```python
# syntax
lst = ['item1', 'item2']
lst.sort()                # ascending
lst.sort(reverse=True)    # descending
```

####    Example:
```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)             # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]
```

sorted(): returns the ordered list without modifying the original list **Example:**
```python
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
```

You are diligent and you have already achieved quite a lot. You have just completed day 5 challenges and you are 5 steps a head in to your way to greatness. Now do some exercises for your brain and muscles.

