# Strings can be represented by " " or ' '
a = "python"
b = 'java'
print(a, ",", b)  # Output: python , java

# String concatenation
a = "python"
b = " is an easiest language"
c = a + b
print(c)  # Output: python is an easiest language

# Type conversion
a = "100"     # String representation of a number
b = type(a)   # Get the type of variable a
print(b)      # Output: <class 'str'>
c = int(a)    # Convert string to integer
d = type(c)   # Get the type of variable c
print(d)      # Output: <class 'int'>

# Formatted strings
name = "john"
age = 20
print(f"My name is {name} and I am {age} years old")  # Output: My name is john and I am 20 years old
print("My name is {} and I am {} years old".format(name, age))  # Output: My name is john and I am 20 years old

# String indexing
str = '123456789'
#   index: 012345678
print(str)          # Output: 123456789
print(str[0:6])     # Output: 123456 (slicing from index 0 to 5)
print(str[:])       # Output: 123456789 (full string)
print(str[0:9:1])   # Output: 123456789 (slicing with step 1)
print(str[0:9:2])   # Output: 13579 (slicing with step 2)
print(str[-1])      # Output: 9 (last character)
print(str[::-1])    # Output: 987654321 (reversed string)

# Multi-line string representation
multi_line_str = """This is a
multi-line string."""
print(multi_line_str)
