# Lists and Tuples

# Primitive Data Types are the Types of Variables which can store only one value.
# Non-Primitive Data Types are the Types of Variables which can store multiple values.

# Lists
# Definition: A list is a sequence of values. It is a collection of values.
from typing import List

list_name = []
fruits = ['apple', 'banana', 'orange', 'mango', 'pineapple']
print(fruits)
print(type(fruits))

print(len(fruits))

list_of_values = [1, 2, 3e4, 'apple', "Python", True, False, 3.14]

# Accessing the elements
print(fruits[0])
print(fruits[3])
print(fruits[-3])

# Slicing the list
print(list_of_values[1:4])
print(list_of_values[:3])  # Start to Index 2
print(list_of_values[3:])  # Index 3 to End
print(list_of_values[:])  # All the values
print(list_of_values[::2])  # All the values skipping 1
print(list_of_values[::-1])  # Reverse

# Lists are Mutable and that's why they can be modified or changed.
fruits[0] = 'grapes'
print(fruits)

## Appending to a list: Adding a value to the end of the list.
fruits.append('kiwi')
print(fruits)

## Inserting to a list: Adding a value to a specific index.
fruits.insert(2, 'papaya')
print(fruits)

## Removing from a list: Removing a value from the list.
fruits.remove('grapes')
print(fruits)

## Popping from a list: Removing a value from a specific index.
fruits.pop(4)
print(fruits)

## Sorting a list: Sorting the list in ascending order.
fruits.sort()
print(fruits)

## Reverse Sorting a list: Sorting the list in descending order.
fruits.sort(reverse=1)
print(fruits)

## Sorting a list: Sorting the list in ascending order.
list_of_values.reverse()
print(list_of_values)

# Tuples
# Definition: A tuple is a sequence of values. It is a collection of values.
# They are immutable.
latlong = (12.9797, 77.5946)
months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
          "Nov", "Dec")

print(months)
print(type(months))

# Accessing the elements
print(months[0])  # Jan
print(months[3])  # Apr
print(months[-3])  # Oct

# Slicing the list
print(months[1:4])  # ("Feb", "Mar", "Apr")
print(months[:3])  # ("Jan", "Feb", "Mar")
print(months[3:]
      )  # ( "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov","Dec")
print(months[::2])  # ("Jan", "Mar", "May", "Jul", "Sep", "Nov")
print(
    months[::-1]
)  # ("Dec", "Nov", "Oct", "Sep", "Aug", "Jul", "Jun", "May","Apr", "Mar", "Feb", "Jan")

# Exercise 1: Basic List Operations (Reyansh's Task)
# Create a list of numbers with the elements [1, 2, 3, 4, 5].
x = [1, 2, 3, 4, 5]
print(x)
# Append the number 6 to the list.
x.append(6)
print(x)
# Could you insert the number 0 at the beginning of the list?
x.insert(0, 0)
print(x)
# Remove the number 3 from the list.
x.remove(3)
print(x)
# Sort the list in descending order.
x.sort(reverse=True)
print(x)
# Print the list and its length.
print(len(x))

# Exercise 2: Basic Tuple Operations
# Create a tuple fruits with the elements ('apple', 'banana', 'cherry').
fruits = ('apple', 'banana', 'cherry')
# Print the first and last elements of the tuple.
print(fruits[0], fruits[-1])
# Create a new tuple more_fruits by adding ('orange', 'grape') to fruits.
more_fruits = list(fruits)
more_fruits.append('orange')
more_fruits.append('grape')
print(tuple(more_fruits))
# Check if 'banana' is in the tuple fruits.
print('banana' in fruits)
