# List of numbers from 1 to 10 (can be replaced with any previous list).
numbers = list(range(1, 11))

# Printing the first three items in the list.
print("The first three items in the list are:", numbers[:3])

# Printing three items from the middle of the list.
middle_index = len(numbers) // 2
print("Three items from the middle of the list are:", numbers[middle_index - 1:middle_index + 2])

# Printing the last three items in the list.
print("The last three items in the list are:", numbers[-3:])
