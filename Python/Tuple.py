# Defining tuples
tuple1 = (1, 2, 3, 4, 5)  # Tuple of integers
tuple2 = ('a', 'b', 'c', 'd')  # Tuple of strings
tuple3 = (1, 2.5, "a", "b", True)  # Tuple with mixed data types

# Printing tuples
print("tuple1:", tuple1)  # Output: (1, 2, 3, 4, 5)
print("tuple2:", tuple2)  # Output: ('a', 'b', 'c', 'd')
print("tuple3:", tuple3)  # Output: (1, 2.5, 'a', 'b', True)

# Accessing elements by index
print("First element of tuple1:", tuple1[0])  # Output: 1
print("Second element of tuple2:", tuple2[1])  # Output: b
print("Fourth element of tuple3:", tuple3[3])  # Output: b

# Tuples are immutable, so you cannot modify their elements
# tuple1[0] = 10  # This will raise a TypeError

# Tuple methods
print("Count of 1 in tuple1:", tuple1.count(1))  # Output: 1
print("Index of 'b' in tuple2:", tuple2.index('b'))  # Output: 1

# Tuples can be used to store related data together
person = ("John", 30, "Engineer")
print("Person tuple:", person)  # Output: ('John', 30, 'Engineer')

# Unpacking tuples
name, age, profession = person
print("Name:", name)  # Output: John
print("Age:", age)  # Output: 30
print("Profession:", profession)  # Output: Engineer

# Tuples with a single element need a comma
single_element_tuple = (42,)
print("Single element tuple:", single_element_tuple)  # Output: (42,)

# Concatenating tuples
tuple4 = tuple1 + tuple2
print("Concatenated tuple:", tuple4)  # Output: (1, 2, 3, 4, 5, 'a', 'b', 'c', 'd')

# Slicing tuples
print("Slice of tuple1:", tuple1[1:4])  # Output: (2, 3, 4)
print("Reversed tuple1:", tuple1[::-1])  # Output: (5, 4, 3, 2, 1)

# Nested tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested_tuple)  # Output: ((1, 2), (3, 4), (5, 6))
print("First element of the first tuple:", nested_tuple[0][0])  # Output: 1
