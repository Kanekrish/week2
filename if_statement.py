# Ask the user for the type of book
book_type = input("What type of book is it? ")

# Check if the book is an adventure book
if book_type == "adventure":
    # Display a message if it is an adventure book
    print("I like adventure books!")

else:
    print("Wrong Input")
    # Display a message indicating that the program has finished reading the book
    print("Done!")
