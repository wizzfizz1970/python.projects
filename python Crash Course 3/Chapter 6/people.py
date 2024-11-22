# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {'first_name': 'Kevin',
          'last_name': 'brown',
            'age': 55,            
            'city':'sydney',
          }

people.append(person)

person = {'first_name': 'Rebecca',
    'last_name': 'jones', 
    'age': 46, 
    'city':'queenlands',
    }
people.append(person)

person = {'first_name': 'chelse',
          'last_name': 'green',
            'age': 18, 
            'city':'brisbrane',
            }

people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()
    
         