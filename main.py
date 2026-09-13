"""This is a 7 days practice guide on w3school.com(Beginner stage)"""
import random

from django.template.defaultfilters import upper

#Python print synthax
print("i am", end= ' ')
print(30, "The next month")

#Python Variables
x = 7
y  = 3
print(x * y)
print(x + y)
print(x % y)
print(x // y)

#data type casting
x = str(3)
y = int(5)
z = float(2)
print(x)
print(y)
print(z)

#Using the type function
_x = 2
my_name = "Paul"
print(type(_x))
print(type(my_name))

# Many values to multiple variables
x,y,z = "Yam", "Beans", "Bread"
print(x)
print(y)
print(z)
x=y=z = 4
print(x)
print(y)
print(z)

#Unpacking items in a list to multiple variables
fruits = ["apple", "banana", "cherry"]
a,b,c = fruits
print(a)
print(b)
print(c)

#Create a variable outside of a function, and use it inside the function,and creating a new variable inside the function
x = "Awesome life"

def my_function():
    x = "Ellegant"
    print("my life is an " + x)

my_function()
print("My life is an " + x)

#Using the global keyword
x = "Nonchalant"
def my_function():
    global x #will only and always use the variable inside the function
    x = "Awesome life"
    print("my life is an " + x)
my_function()
print("My life is an " + x)

#Python data types
a = 5
b = "bool"
z = True
y = ['cat', 'dog', 'fish']
#use the type() module to find out their types
print(type(a))
print(type(b))
print(type(z))
print(type(y))

#Python Numbers
a = 5
b = 5.4
c = 10j
d = None
#Print variables as type
print(type(a))
print(type(b))
print(type(c))
print(type(d))
#Converting number types in python
a = float(a)
b = int(b)
c = complex(a)
print(a)
print(b)
print(c)

#Using the random module in python
num = []
num1 = random.randrange(1, 50)
num.append(num1)
print(num)

#Python Casting
num1 = 2
num2 = 2.3
num3 = '4'
#casting the data types
num1 = float(num1)
num2 = int(num2)
num3 = int(num3)
print(num1, num2, num3)

#Python Strings -- string slicing
a = 'Hello World'
print(a[0:5])
#looping through a string
for i in "Banana":
    print(i)
#using the len() function
a = 'Hello World'
b = 'Stay positive'
print(len(a),'and', len(b))
#String check
txt = 'python is one of the free and easy languages'
print('python' in txt)
#using if statement
txt = 'python is one of the free and easy languages'
if 'python' in txt:
    print('python is one of the free and easy languages')
#check if not string
txt = 'python is one of the free and easy'
print('play' not in txt)

if "play" not in txt:
    print(txt)
#Modifying strings
name = 'paul'
print(name)
if name == upper(" "):
    print('it is uppercase')
else:
    print('it is lowercase')
#The replace() method replaces a string with another string:
a = 'Hello, World'
print(a.replace("H", "L",))

#String Concact>>>>>>Joining Strings
a = "name"
b = "is"
c = "Paul"
up = c.upper()
d = a + b + up
print(d)

d = a + ' ' + b + ' ' + up
print(d)

#String formating
name = 'paul'
age = 30
txt = f'My name is {name} and I am {age} years old'
print(txt)

price_in_dollars = 50
txt = f'price in dollars is ${price_in_dollars:.2f}'
print(txt)

#Escape characters>>>>>Backslash \
txt = "We are the so called \"Best\" students from the east"
print(txt)

#Boolean and conditional statements
#Print a message based on whether the condition is True or False:
a = 300
b = 200
if a > b:
    print(f'a {a} is greater than b {b}')
else:
    print(f'a {a} is not greater than b {b}')

#Python Operators
num1 = 5
num2 = num1 + 5
num3 = num1 + num2
print(num3)

x = 3
x += 10
print(x)

y = 100
x = y + 250
z = y + x // 10
_x_y_zOutcome = z

if _x_y_zOutcome > y:
    print(f"Outcome is {_x_y_zOutcome}")
print(z)

scaler = 10
if scaler == 9 or scaler == 8:
    print("Scale at 9 units")
elif scaler == 7 or scaler == 6:
    print("Scale at 7 units")
else:
    print(f"{scaler} is properly used for scaling")

#Python List>>>>>>> this is my list
fruits = ["ball", "Brok", "clothes", "income", "Action", "Movie"]
#Print list
print(fruits)
#Print the last item of the list
print(fruits[5])
print(fruits[2:-1])
print(fruits[:4])
#Using the if conditional statement to find if book is in list
if 'Book' in fruits:
    print("Book is in fruits")
else:
    print("Book is not in fruits")
#using the loop and if statement together
for j in fruits:
    if j == 'Brok':
        print("Brok is in fruits")
    else:
        print("Brok is not in fruits")
        break
#Change the second and third items in fruits
fruits = ["ball", "Brok", "clothes", "income", "Action", "Movie"]
fruits[1:-3] = 'Vest', 'Orange'
print(fruits)
#let us use the append method
fruits.append("Mangoes")
fruits.append("Dagger")
print(fruits)
#using the insert method to add item to list
fruits.insert(2,"Teeth")
print(fruits)
#Creat two lists and combine list a and b to one list, general list
listA =  ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
listA.extend(tropical)
new_list = []
new_list.append(listA)
print(new_list)

#The remove() method removes the specified item....... still use the fruits list to see outcome. Remove "ball":
fruits = ["ball", "Brok", "clothes", "income", "Action", "Movie"]
fruits.remove("ball")
print(fruits)
#The pop() method removes the specified index.
fruits.pop(0)
fruits.pop() #Takes off the last index in the list
del fruits[1] #deletes index 1 inside the list
print(fruits)

# Loop through a list
fruits = ["ball", "Brok", "clothes", "income", "Action", "Movie"]
for fruit in fruits:
    print(fruit)
for i in range(len(fruits)):
    print(i)
    print(fruits[i])

#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_List = []
for x in fruits:
    if "a" or "c" in x:
        new_List.append(x)
        print(new_List)
        break
    for x in new_List:
        if "a" in x:
            print(new_List)
            break

#Sort List Alphanumerically
my_fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
my_fruits.sort() #This method will sort the list changing the index of the list
print(my_fruits) #The list is already sorted alphabetically>> it will print the list

#Sorting through numeric index in the list
num_list = [100, 50, 65, 82, 23]
num_list.sort()
print(num_list) #Arranges the numeric elements from the lowest num to the highest

#Sort Descending >>>>> To sort descending, use the keyword argument reverse = True:
num_list = [100, 50, 65, 82, 23]
num_list.sort(reverse=True)
print(num_list)

my_fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
my_fruits.sort(reverse=True)
print(my_fruits)

"""Customize Sort Function
You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first):"""
def myfunc(n):
    return abs(n - 50)
num_list.sort(key=myfunc)
print(num_list)

"""What if you want to reverse the order of a list, regardless of the alphabet?

The reverse() method reverses the current sorting order of the elements."""
my_fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
my_fruits.reverse()
print(my_fruits)

#COPY A LIST IN PYTHON >>>>>> You can use the built-in List method copy() to copy a list.
my_fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
_2nd_List = my_fruits.copy()
print(_2nd_List)

"""Join Two Lists
There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator."""
my_fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
num_list = [100, 50, 65, 82, 23]
comb_list = my_fruits + num_list
print(comb_list)

#Using the for loop to join list 1 and 2
for x in my_fruits:
    num_list.append(x)
print(num_list)

#Use the extend() method to add list2 at the end of list1:
my_fruits.extend(num_list)
my_fruits.clear()
print(my_fruits)

'''Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list'''

# Create a list
colors = ["red", "green", "blue"]
# Print the first item
print(colors[0])
# Change the second item to "yellow"
colors[2] = "yellow"
# Add "purple" to the end
colors.append("purple")

# Remove "red"
colors.remove("red")

# Print the list
print(colors)

"""PYTHON TUPLE
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets."""

my_tuple = ("apple", "banana", "cherry")
print(my_tuple[1])

if "banana" in my_tuple:
    print("Yes, Banana is in tuple")

"""Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

"""
my_tuple = ("apple", "banana", "cherry")
my_list = list(my_tuple)
my_list[0] = "Mango"
my_list[1] = "Orange"
my_list[2] = "Kiwi"
print(my_list)

trp = tuple(my_list)
print(trp)

"""Add Items
Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple."""
my_tuple = ("apple", "banana", "cherry")
fruit_list = list(my_tuple)
fruit_list.append("mango")
print(fruit_list)

fruit_tup = tuple(fruit_list)
print(fruit_tup)
""". Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:"""
my_tuple = ("apple", "banana", "cherry")
o = ("Orange",)
my_tuple += o
print(my_tuple)

"""Remove Items
Note: You cannot remove items in a tuple.

Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:"""
my_tuple = ("apple", "banana", "cherry")
list_ = list(my_tuple)
list_.remove("cherry")
list_.append("orange")
print(list_)

new_tuple = tuple(list_)
print(new_tuple) #Change tuple to list and do anything you want, then change back to a tuple

"""Unpacking a Tuple
When we create a tuple, we normally assign values to it. This is called "packing" a tuple:But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":"""
my_tuple = ("apple", "banana", "cherry")
a,b,c = my_tuple
print(a,b,c)
print(type(a))

"""Loop Through a Tuple
You can loop through the tuple items by using a for loop."""
my_tuple = ("apple", "banana", "cherry")
for x in my_tuple:
    if "apple" in x:
        print("Eat apple in the morning")

"""Loop Through the Index Numbers
You can also loop through the tuple items by referring to their index number.

Use the range() and len() functions to create a suitable iterable."""

my_tuple = list(my_tuple) #Converting tuple to a list
my_tuple.append("orange") #Adding item to the list using the .append () function
print(my_tuple)
my_tuple = tuple(my_tuple) #Changing the list back to tuple
print(my_tuple)

for i in range(len(my_tuple)): #Iterating through the tuple (for Loop)
    if "orange" in my_tuple:    ## using if conditional statement to find variable item "Orange"
        print("Yes, orange is in tuple")
        print(my_tuple)
    else:
        print("No, orange is not in tuple")
        break

"""Join Two Tuples
To join two or more tuples you can use the + operator:"""

my_tuple = ("apple", "banana", "cherry")
num_tuple = (1,2,3)
joined_tuple = my_tuple + num_tuple

joined_tuple = list(joined_tuple)
add_list = ["Brain", 2, "them", 5]
new_List = joined_tuple + add_list
new_List.append("are you sure")
print(new_List)
fresh_tuple = tuple(new_List)
print(fresh_tuple)

for x in fresh_tuple:
    if 1 in fresh_tuple:
        print("Number is present")
        break
    else:
        print([x])

"""PYTHON SETS ... >>>>Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets.<<<<    Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members."""
my_set = {"pin", "bag", 2, True, 0, "paul"}
set_index = len(my_set)
print("my_set has",set_index, "items")
# Access Items
# You cannot access items in a set by referring to an index or a key.
for i in my_set:
    print(i, "is a set item")
print("pon" in my_set) # "pon" is not in set it returns false
#Add Items
#Once a set is created, you cannot change its items, but you can add new items.

#To add one item to a set use the add() method.
my_set.add("yellow")
print(my_set)
my_set.remove(0)
print(my_set)

"To add items from another set into the current set, use the update() method."
my_set = {"pin", "bag", 2, True, 0, "paul"}
top_sets = {"bread", 'tea'}
my_set.update(top_sets)
print(my_set)

"""Add Any Iterable
The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.)."""
my_set = {"pin", "bag", 2, True, 0, "paul"}
top_sets = ["bread", 'tea']
my_set.update(top_sets)
print(my_set)

"""Remove Item
To remove an item in a set, use the remove(), or the discard() method."""
my_set = {"pin", "bag", 2, True, 0, "paul"}
my_set.remove("paul")
print(my_set)
## OR
my_set.discard("pin")
print(my_set)

"""Join Sets
There are several ways to join two or more sets in Python.
The union() and update() methods joins all items from both sets.
The intersection() method keeps ONLY the duplicates.
The difference() method keeps the items from the first set that are not in the other set(s).
The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""
my_set = {"pin", "bag", 2, True, 0, "paul"}
new_set = {"weak", 55, 1000, "comehome"}
updated_set = my_set.union(new_set) # Using the set union function to join two sets
print(updated_set)

# Joining multiple sets to become one

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
all_sets = set1 | set2 | set3 # using the | on key board to unite all sets, same as the union function in python
print(all_sets)

"""Join a Set and a Tuple
The union() method allows you to join a set with other data types, like lists or tuples.

The result will be a set."""
set1 = {"a", "b", "c"}
set2 = ["John", "Elena"]
union_set = set1.union(set2)
print(union_set)

num_set = {1, 2, 3, 4, 5}
num2_set = {2, 4, 6, 8, 10}
main_set = num_set.update(num2_set)
print(main_set)

"""Intersection
Keep ONLY the duplicates

The intersection() method will return a new set, that only contains the items that are present in both sets."""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
set3 = set2.intersection_update(set1)
print(set3)

"""Set Methods
Python has a set of built-in methods that you can use on sets.

Method	Shortcut	Description
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns True if all items of this set is present in another set
 	<	Returns True if all items of this set is present in another, larger set
issuperset()	>=	Returns True if all items of another set is present in this set
 	>	Returns True if all items of another, smaller set is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others"""

# Create the set
colors = {"red", "green", "blue"}
# Print the set
print(colors)
# Add "yellow"
colors = colors.add("yellow")
# Print the number of item
print(colors)


"Python Dictionaries"
"""Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values:

Example
Create and print a dictionary:"""

my_dict = {
    "Object": "Car",
    "Model": "Toyota",
    "country": "Japan",
    "Year": 1995
}
print(my_dict["Year"], ["Model"])
print(my_dict["country"])

#Dictionary Data types >>>>>>>> it contains all kinds of data types but do not allow duplicates

my_dict = {
    "Object": "Car",
    "Model": "Toyota",
    "country": "Japan",
    "England": False,
    "Year": 1995,
    "Year": 2026,
    "colors": ["red", "green", "blue"]
}
print(my_dict)
print(len(my_dict))

"""Accessing Items
You can access the items of a dictionary by referring to its key name, inside square brackets:

Example
Get the value of the "model" key:"""
my_dict = {
    "Object": "Car",
    "Model": "Toyota",
    "country": "Japan",
    "England": False,
    "Year": 1995,
    "Year": 2026,
    "colors": ["red", "green", "blue"]
}
x = my_dict.get("Model") #Using the get() method, this will return the value in model == Toyota
print(x)
y = my_dict.keys() #returns all keys in the dictionary
print(y)
z = my_dict.values() #Returns all values in the dictionary
print(z)

my_dict["House"] = "Duplex"
print(my_dict)
# Checking if "Model" exixt in the dict. >>>> using the if statement
if "Model" and "Fame" in my_dict:
    print("Yes, Model is in dictionary")
else:
    print("No, Fame is not in dictionary")

import pandas as pd
df = pd.DataFrame({
    "Name": ["Bennie", "Paul", "Peter", "John"],
    "Age": [23,33,54,19],
    "Sex": ["Female", "male", "Male", "male"],
})
print(df)
