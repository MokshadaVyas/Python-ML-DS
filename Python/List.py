# Lists can hold multiple items of various types
li1 = [1, 2, 3, 4, 5]  # List of integers
li2 = ['a', 'b', 'c', 'd']  # List of strings
li3 = [1, 2.5, "a", "b", True]  # List with mixed data types

# Printing the lists
print(li1)  # Output: [1, 2, 3, 4, 5]
print(li2)  # Output: ['a', 'b', 'c', 'd']
print(li3)  # Output: [1, 2.5, 'a', 'b', True]

# Accessing elements by index
print(li1[0])  # Output: 1 (first element of li1)
print(li2[1])  # Output: b (second element of li2)
print(li3[3])  # Output: b (fourth element of li3)

# Defining a 2D list (matrix)
li4 = [
    [1, 2, 3],  # First row
    [4, 5, 6],  # Second row
    [7, 8, 9]   # Third row
]

# Printing the matrix
print(li4)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements in a matrix
print(li4[0][0])  # Output: 1 (first element of the first row)
print(li4[1][2])  # Output: 6 (third element of the second row)
print(li4[2][1])  # Output: 8 (second element of the third row)
