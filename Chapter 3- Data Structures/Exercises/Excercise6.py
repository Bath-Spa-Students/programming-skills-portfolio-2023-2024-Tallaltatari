guest = ["Saad", "Haim", "Nabeel", "Danial"]
print(guest[0] + ", please come to dinner.")
print(guest[1] + ", please come to dinner.")
print(guest[2] + ", please come to dinner.")
print(guest[3] + ", please come to dinner.")

print("Sadly " + guest[2] + ", will be unable to join us at the dinner")

guest.remove("Nabeel")
New_guests = guest.append("Azmath")
print(guest[0] + ", please come to dinner.")
print(guest[1] + ", please come to dinner.")
print(guest[2] + ", please come to dinner.")
print(guest[3] + ", please come to dinner.")

print("Sorry, we can only invite two people to dinner.")

name = guest.pop()
print("Sorry, " + name + " there's no room at the table.")
name = guest.pop()
print("Sorry, " + name + " there's no room at the table.")
name = guest[0].title()
print(name + ", please come to dinner.")
name = guest[1].title()
print(name + ", please come to dinner.")

del(guest[0])
del(guest[0])

print(guest)