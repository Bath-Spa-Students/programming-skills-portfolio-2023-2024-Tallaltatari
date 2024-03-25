while True:
    age = input("Please, Enter your age: ")
    if age == 'quit':
        break
    age = int(age)
    if age <= 3:
        print("  You get in free!")
    elif age <= 13:
        print("  Your ticket costs $10.")
    else:
        print("  Your ticket costs $15.")