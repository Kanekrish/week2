# Display the message "Where should I look?"
print("Where should I look?")

# Read the user's response
user_response = input()

# Check the user's response and display the corresponding message
if user_response == "in the bedroom":
    # Ask the user where in the bedroom to look
    bedroom_location = input("Where in the bedroom should I look? ")

    # Check the user's response and display the corresponding message
    if bedroom_location == "under the bed":
        print("Found some shoes but no phone")
    else:
        print("Found some mess but no phone.")

elif user_response == "in the bathroom":
    # Ask the user where in the bathroom to look
    bathroom_location = input("Where in the bathroom should I look? ")

    # Check the user's response and display the corresponding message
    if bathroom_location == "in the bathtub":
        print("Found a rubber duck but no phone")
    else:
        print("Found bathroom stuff but no phone.")

elif user_response == "in the living room":
    # Ask the user where in the living room to look
    living_room_location = input("Where in the living room should I look? ")

    # Check the user's response and display the corresponding message
    if living_room_location == "on the table":
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but no phone.")

else:
    # Display the message if the user's response is not recognized
    print("I do not know where that is but I will keep looking.")
