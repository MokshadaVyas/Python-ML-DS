# Example string
s = "Hello, World!"

# capitalize() - Capitalizes the first character of the string
print(s.capitalize())  # Output: "Hello, world!"

# lower() - Converts all characters to lowercase
print(s.lower())  # Output: "hello, world!"

# upper() - Converts all characters to uppercase
print(s.upper())  # Output: "HELLO, WORLD!"

# title() - Capitalizes the first character of each word
print(s.title())  # Output: "Hello, World!"

# swapcase() - Swaps the case of all characters
print(s.swapcase())  # Output: "hELLO, wORLD!"

# find() - Finds the first occurrence of a substring
print(s.find('World'))  # Output: 7

# rfind() - Finds the last occurrence of a substring
print(s.rfind('l'))  # Output: 10

# index() - Finds the first occurrence of a substring and raises an error if not found
print(s.index('World'))  # Output: 7

# rindex() - Finds the last occurrence of a substring and raises an error if not found
print(s.rindex('l'))  # Output: 10

# count() - Counts the occurrences of a substring
print(s.count('l'))  # Output: 3

# replace() - Replaces occurrences of a substring with another substring
print(s.replace('World', 'Python'))  # Output: "Hello, Python!"

# split() - Splits the string into a list of substrings
print(s.split(','))  # Output: ['Hello', ' World!']

# join() - Joins elements of an iterable with the string as a separator
words = ['Hello', 'World']
print(', '.join(words))  # Output: "Hello, World"

# strip() - Removes leading and trailing whitespace (or specified characters)
s2 = "  Hello, World!  "
print(s2.strip())  # Output: "Hello, World!"

# lstrip() - Removes leading whitespace (or specified characters)
print(s2.lstrip())  # Output: "Hello, World!  "

# rstrip() - Removes trailing whitespace (or specified characters)
print(s2.rstrip())  # Output: "  Hello, World!"

# startswith() - Checks if the string starts with a specified substring
print(s.startswith('Hello'))  # Output: True

# endswith() - Checks if the string ends with a specified substring
print(s.endswith('!'))  # Output: True

# isalpha() - Checks if all characters in the string are alphabetic
print("Hello".isalpha())  # Output: True
print("Hello123".isalpha())  # Output: False

# isdigit() - Checks if all characters in the string are digits
print("123".isdigit())  # Output: True
print("Hello123".isdigit())  # Output: False

# isalnum() - Checks if all characters in the string are alphanumeric
print("Hello123".isalnum())  # Output: True
print("Hello 123".isalnum())  # Output: False

# isspace() - Checks if all characters in the string are whitespace
print("   ".isspace())  # Output: True
print("Hello".isspace())  # Output: False

# len() - Gets the length of the string
print(len(s))  # Output: 13
