# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "profession": "Engineer"
}

# Printing the dictionary
print("Person dictionary:", person)  # Output: {'name': 'Alice', 'age': 30, 'profession': 'Engineer'}

# Accessing values by key
print("Name:", person["name"])  # Output: Alice
print("Age:", person["age"])  # Output: 30

# Adding a new key-value pair
person["city"] = "New York"
print("Updated dictionary:", person)  # Output: {'name': 'Alice', 'age': 30, 'profession': 'Engineer', 'city': 'New York'}

# Modifying an existing value
person["age"] = 31
print("Modified dictionary:", person)  # Output: {'name': 'Alice', 'age': 31, 'profession': 'Engineer', 'city': 'New York'}

# Removing a key-value pair using pop()
profession = person.pop("profession")
print("Removed profession:", profession)  # Output: Engineer
print("Dictionary after pop:", person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}

# Using get() to access values
profession = person.get("profession", "Not available")
print("Profession:", profession)  # Output: Not available

# Iterating over dictionary keys
for key in person:
    print(f"Key: {key}, Value: {person[key]}")

# Iterating over dictionary items
for key, value in person.items():
    print(f"{key}: {value}")

# Checking if a key exists
if "name" in person:
    print("Name exists in the dictionary.")

# Dictionary methods
print("Keys:", person.keys())  # Output: dict_keys(['name', 'age', 'city'])
print("Values:", person.values())  # Output: dict_values(['Alice', 31, 'New York'])
print("Items:", person.items())  # Output: dict_items([('name', 'Alice'), ('age', 31), ('city', 'New York')])

# Clearing the dictionary
person.clear()
print("Cleared dictionary:", person)  # Output: {}

# Creating a dictionary using dict()
person = dict(name="Bob", age=25, profession="Doctor")
print("New dictionary:", person)  # Output: {'name': 'Bob', 'age': 25, 'profession': 'Doctor'}

# Nested dictionary
people = {
    "person1": {"name": "John", "age": 28},
    "person2": {"name": "Doe", "age": 22}
}

print("Nested dictionary:", people)
print("Person1's name:", people["person1"]["name"])  # Output: John
