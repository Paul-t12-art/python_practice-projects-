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
