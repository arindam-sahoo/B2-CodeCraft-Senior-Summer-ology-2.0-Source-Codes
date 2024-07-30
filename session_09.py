# Dictionaries
# Definition: A dictionary is a collection of key-value pairs.
# It is an unordered collection of data.

# Creating a Dictionary
courses = {}
print("Courses' Dictionary:", courses)
students = {'Myra': 90, 'Aarna': 85, 'Niranjan': 95, 'Reyansh': 80}
print("Students' Dictionary:", students)

# Accessing a key
print("Marks secured by Reyansh:", students['Reyansh'])

# Adding Values to dictionaries
courses['course_name'] = 'Python'
courses['course_length'] = '16'
courses['number_of_students'] = 3
print("Courses' Dictionary:", courses)

# Updating Values of a dictionary
courses['number_of_students'] = 4
print("Courses' Dictionary:", courses)

# Removing using deleting a key-value pair
del courses['number_of_students']
print("Courses' Dictionary:", courses)

# Removing using pop() method
courses.pop('course_length')
print("Courses' Dictionary:", courses)

# List of Dictionary Keys
print(students.keys())

# List of Dictionary Values
print(students.values())

# List of Dictionary Items
print(students.items())

# Iterating through a dictionary
for key in students:
    print(key, ":", students[key])

# Nested
data = {
    'course_name':
    'B2 CodeCraft Senior Summer-ology 2.0',
    'course_subject':
    'Python',
    'course_length':
    '16',
    'students': [{
        'student_name': 'Myra',
        'grade': 5
    }, {
        'student_name': 'Reyansh',
        'grade': 6
    }, {
        'student_name': 'Aarna',
        'grade': 6
    }, {
        'student_name': 'Niranjan',
        'grade': 6
    }]
}

print(data['students'][3]['student_name'])

# Set
# Definition: A set is a collection of unique elements.
s = set()
s = {51, 62, 39, 73, 96}
print(s)

l = ['science', 'mathematics', 'history', 'geography', 'science']
print(l)
l = set(l)
print(l)
l = list(l)
print(l)

# Adding values
s.add(66)
print(s)

# Removing values
s.remove(39)
print(s)
s.discard(73)
print(s)

# Checking membership
print(62 in s)
print(73 in s)

# Set Operations
numbers = {1, 2, 3, 4, 5, '6', '7'}
characters = {'a', 'b', 'c', 'd', 'e', '6', '7'}
# Union
union_set1 = numbers | characters
print(union_set1)
union_set2 = numbers.union(characters)
print(union_set2)
# Intersection
intersection_set1 = numbers & characters
print(intersection_set1)
intersection_set2 = numbers.intersection(characters)
print(intersection_set2)
