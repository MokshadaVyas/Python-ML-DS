# Using ==
# == checks for value equality

a = [1, 2, 3]
b = [1, 2, 3]

# Both lists have the same values
print(a == b)  # Output: True

# Using is
# is checks for identity equality

# Although a and b have the same values, they are different objects in memory
print(a is b)  # Output: False

# Assigning b to a
b = a

# Now a and b refer to the same object in memory
print(a is b)  # Output: True

# Comparing immutable types
# Strings with the same value are often stored at the same memory location

s1 = "hello"
s2 = "hello"

print(s1 == s2)  # Output: True (values are the same)
print(s1 is s2)  # Output: True (both refer to the same object in memory)

# Comparing integers
x = 1000
y = 1000

print(x == y)  # Output: True (values are the same)
print(x is y)  # Output: False (different objects in memory for large integers)

# For small integers and short strings, Python may cache the objects
x = 100
y = 100

print(x == y)  # Output: True (values are the same)
print(x is y)  # Output: True (both refer to the same object in memory due to interning)