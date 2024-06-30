# Conditional statements allow you to execute certain code blocks based on conditions

# Example using if, elif, and else
age = 20

# Check if age is greater than or equal to 18
if age >= 18:
    print("You are eligible for a driver's license.")  # This block executes if the condition is True
elif age >= 16:
    print("You can apply for a learner's permit.")  # This block executes if the previous condition is False and this one is True
else:
    print("You are too young to drive.")  # This block executes if all previous conditions are False

# Example with multiple conditions using logical operators
score = 85

if score >= 90:
    print("Grade: A")  # Executes if score is 90 or above
elif score >= 80:
    print("Grade: B")  # Executes if score is 80 to 89
elif score >= 70:
    print("Grade: C")  # Executes if score is 70 to 79
else:
    print("Grade: D")  # Executes if score is below 70

# Example using logical operators and comparison
temperature = 25

if temperature > 30:
    print("It's a hot day.")
elif temperature < 10:
    print("It's a cold day.")
else:
    print("The weather is moderate.")

# Example with nested conditions
age = 18
has_permit = True

if age >= 18:
    if has_permit:
        print("You can drive.")
    else:
        print("You need a permit to drive.")
else:
    print("You are too young to drive.")
