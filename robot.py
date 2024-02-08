# Prompt the user for a direction
direction = input("Which direction should the robot move in? (up, down, left, right) ")

# Determine the robot's next move
if direction == "up":
    # The robot should move up
    print("The robot should move up.")
elif direction == "down":
    # The robot should move down
    print("The robot should move down.")
elif direction == "left":
    # The robot should move left
    print("The robot should move left.")
elif direction == "right":
    # The robot should move right
    print("The robot should move right.")
else:
    # The user input an invalid direction
    print("Invalid direction.")

# Exit the program
