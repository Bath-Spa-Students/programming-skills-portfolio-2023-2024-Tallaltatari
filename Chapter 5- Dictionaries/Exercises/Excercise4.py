rivers = {
    'Nile': 'Egypt',
    'Mississippi': 'United States',
    'Amazon': 'South America',
    'Missouri': 'United States',
    'Yangtze': 'China',
}
for river, country in rivers.items():
    print("The " + river + " flows through " + country + ".")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(river)

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(country)
