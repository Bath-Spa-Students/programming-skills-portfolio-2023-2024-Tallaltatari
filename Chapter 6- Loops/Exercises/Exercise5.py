sandwich_orders = ["egg and cheese","pastrami", "chicken","pastrami", "salami","pastrami", "veggie"]
finished_sandwiches = []

print("The deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich")
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print("your " + sandwich + " sandwich is finsihed!")    