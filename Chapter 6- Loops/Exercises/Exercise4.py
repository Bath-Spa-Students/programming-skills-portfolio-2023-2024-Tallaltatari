sandwich_orders = ["egg and cheese", "chicken", "salami", "veggie"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich")
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print("your " + sandwich + " sandwich is finsihed!")    