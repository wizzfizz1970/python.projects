prompt = "\nThere are three exits numbered 1, 2 and 3 please enter one ?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    exit = input(prompt)
    if exit == 'quit':
        break
    exit = int(exit)

    if exit == 3:
        print("You used exit 3")
    elif exit == 2:
        print("You used exit 2")
    else:
        print("You used exit 1")
