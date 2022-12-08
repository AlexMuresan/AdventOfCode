# Open the file in read mode
with open("calories_test.txt", "r") as file:
    # Initialize a variable to store the maximum number of Calories
    max_calories = 0

    # Initialize a variable to store the maximum number of Calories carried by an Elf
    max_calories_elf = 0

    # Initialize a variable to store the total number of Calories
    total_calories = 0

    # Read the input from the file
    for line in file:
        # If the line is empty, we have reached the end of an Elf's inventory
        if not line.strip():
            # Update the maximum number of Calories carried by an Elf if needed
            max_calories_elf = max(max_calories_elf, total_calories)

            # Reset the total number of Calories
            total_calories = 0

            # Continue to the next iteration of the loop
            continue

        # Convert the line to an integer
        calories = int(line)

        # Update the maximum number of Calories if needed
        max_calories = max(max_calories, calories)

        # Update the total number of Calories
        total_calories += calories

    # Update the maximum number of Calories carried by an Elf if needed (for the last Elf)
    max_calories_elf = max(max_calories_elf, total_calories)

# Print the maximum number of Calories carried by an Elf
print(max_calories_elf)