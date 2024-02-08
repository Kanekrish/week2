# Initialize variables to count even and odd numbers
count_even = 0
count_odd = 0

# Ask the user to enter three numbers
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

# Check if each number is even or odd and increment the corresponding counter
if first_number % 2 == 0:
    count_even = count_even + 1
else:
    count_odd += 1

if second_number % 2 == 0:
    count_even += 1
else:
    count_odd += 1

if third_number % 2 == 0:
    count_even += 1
else:
    count_odd += 1

    # Display the number of even and odd numbers entered
    print("Number of even numbers:", count_even)
    print("Number of odd numbers:", count_odd)
