# Starting list of pizzas.
my_pizzas = ["Margherita", "Pepperoni", "Hawaiian"]

# Making a copy of the list for a friend.
friend_pizzas = my_pizzas[:]

# Adding a new pizza to each list.
my_pizzas.append("Veggie")
friend_pizzas.append("BBQ Chicken")

# Proving they are two separate lists.
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

