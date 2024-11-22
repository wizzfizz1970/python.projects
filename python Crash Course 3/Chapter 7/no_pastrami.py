# List of sandwich orders
sandwich_orders = ["tuna sandwich", "chicken sandwich", "veggie sandwich", "pastrami","pastrami","pastrami"]

# Empty list to store finished sandwiches
finished_sandwiches = []

# no pastrami
print('Soorry there be no pastrami sandwich due to we run out')

# remove pastrami from list

sandwich_orders = [sandwich for sandwich in sandwich_orders if sandwich != "pastrami"]

# Process each sandwich order
while sandwich_orders:
    # Get the first sandwich order
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich}.")
    
    # Add the made sandwich to the finished sandwiches list
    finished_sandwiches.append(current_sandwich)

# Print the list of all finished sandwiches
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")