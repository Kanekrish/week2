# Prompt the user to enter the cover type of the book
cover_type = input("What is the cover type of the book? (hard or soft) ")

# Check if the book has a soft cover
if cover_type == "soft":
    # Ask the user if the book is perfect bound
    is_perfect_bound = input("Is the book perfect bound? (yes/no) ")

    # Check if the book is perfect bound
    if is_perfect_bound == "yes":
        # Display the message for soft cover, perfect bound books
        print("Soft cover, perfect bound books are very popular!")
    else:
        # Display the message for soft covers with coils or stitches
        print("Soft covers with coils or stitches are great for short books")
# Check if the book has a hard cover
elif cover_type == "hard":
    # Display the message for hard cover books
    print("Books with hard covers can be more expensive!")
else:
    # Display an error message for invalid cover type
    print("Invalid cover type")
