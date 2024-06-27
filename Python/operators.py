# Here are some operators
"""
Arithmetic operators: +, -, *, /, %, **, //
    +   : addition
    -   : subtraction
    *   : multiplication
    /   : division
    %   : modulus (remainder)
    **  : exponentiation
    //  : floor division

Assignment operators: =, +=, -=, *=, /=, %=, **=, //=
    =   : assignment
    +=  : add and assign
    -=  : subtract and assign
    *=  : multiply and assign
    /=  : divide and assign
    %=  : modulus and assign
    **= : exponentiate and assign
    //= : floor divide and assign

Comparison operators: ==, <, >, <=, >=, !=
    ==  : equal to
    <   : less than
    >   : greater than
    <=  : less than or equal to
    >=  : greater than or equal to
    !=  : not equal to

Logical operators: and, or, not
    and : logical AND
    or  : logical OR
    not : logical NOT
"""

# Examples of using these operators

# Arithmetic operators
a = 10
b = 3
print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.3333...
print(a % b)  # 1
print(a ** b) # 1000
print(a // b) # 3

# Assignment operators
a = 5
a += 2   # a = a + 2
print(a) # 7

a -= 3   # a = a - 3
print(a) # 4

a *= 2   # a = a * 2
print(a) # 8

a /= 4   # a = a / 4
print(a) # 2.0

a %= 2   # a = a % 2
print(a) # 0.0

a **= 3  # a = a ** 3
print(a) # 0.0

a = 7
a //= 2  # a = a // 2
print(a) # 3

# Comparison operators
print(5 == 5)   # True
print(5 < 3)    # False
print(5 > 3)    # True
print(5 <= 5)   # True
print(5 >= 4)   # True
print(5 != 5)   # False

# Logical operators
print(True and False) # False
print(True or False)  # True
print(not True)       # False
