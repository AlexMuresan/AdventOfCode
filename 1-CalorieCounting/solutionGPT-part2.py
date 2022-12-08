# Open the file in read mode
with open("calories_test.txt", "r") as file:
    # Initialize a variable to store the maximum number of Calories
    max_calories = 0

    # Initialize a list to store the maximum number of Calories carried by each Elf
    max_calories_elves = []

    # Initialize a variable to store the total number of Calories
    total_calories = 0

    # Read the input from the file
    for line in file:
        # If the line is empty, we have reached the end of an Elf's inventory
        if not line.strip():
            # Update the list of maximum number of Calories carried by each Elf
            max_calories_elves.append(total_calories)

            # Sort the list in descending order
            max_calories_elves.sort(reverse=True)

            # Keep only the top three elements in the list
            max_calories_elves = max_calories_elves[:3]

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

    # Update the list of maximum number of Calories carried by each Elf (for the last Elf)
    max_calories_elves.append(total_calories)

    # Sort the list in descending order
    max_calories_elves.sort(reverse=True)

    # Keep only the top three elements in the list
    max_calories_elves = max_calories_elves[:3]

# Print the total number of Calories carried by the top three Elves
print(sum(max_calories_elves))
