while True:
    topping = input("Enter a pizza topping (type 'quit' to finish): ")
    if topping == 'quit':
        print("Quitting the pizza topping selection. Enjoy your pizza!")
        break
    print(f"We'll add {topping} to your pizza.")
