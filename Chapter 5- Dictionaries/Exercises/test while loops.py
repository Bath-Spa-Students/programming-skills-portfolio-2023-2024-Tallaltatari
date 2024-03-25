i = 1 
while i <= 20:
    print(i)
    i += 1

    num = 1
while num <= 10:
    print("Num is:", num)
    num += 1 

i = 1 
while i <= 20:
    print(i)
    if i == 10:
        break
    i += 1


while True:
    topping = input("Enter a pizza topping (type 'quit' to finish): ")

    if topping == 'quit':
        print("Quitting the pizza topping selection. Enjoy your pizza!")
        break

    print(f"We'll add {topping} to your pizza.")