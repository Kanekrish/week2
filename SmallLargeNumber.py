# Prompt the user to enter the first number
first_number = (input("Enter the first number: "))

# Read in the user's first number
first_num = int(first_number)

# Prompt the user to enter the second number
second_number = (input("Enter the second number: "))

# Read in the user's second number
second_num = int(second_number)

# Decide which of the two numbers is the smallest and display the corresponding message
if first_num > second_num:
    print("The first number is the Largest!")
elif first_num < second_num:
    print("The second number is the Largest!")
else:
    print("Both are equal!")
