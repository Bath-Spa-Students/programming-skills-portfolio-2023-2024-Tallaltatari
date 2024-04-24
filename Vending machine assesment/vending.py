#Made by: Tallal Khan Tatari

#Class is used to store a group of function which can than be called indiviually later on.
#The class VendingMachine is used to store all the functions needed to operate the vending machine.
class VendingMachine:
    def __init__(self):
        # self.items is the dictionary which has the 
        # code for the item, 
        # item name, 
        # its price and 
        # the amount in stock when the program is run.
        self.items = {
            'A1': {'name': 'Apple juice', 'price': 2.50, 'stock': 10},
            'A2': {'name': 'Mango juice', 'price': 2.50, 'stock': 10},
            'A3': {'name': 'Water', 'price': 1.00, 'stock': 10},
            'B1': {'name': 'Lays', 'price': 3.20, 'stock': 10},
            'B2': {'name': 'M&M', 'price': 2.00, 'stock': 10},
            'B3': {'name': 'Kinder Bueno', 'price': 2.70, 'stock': 10},
            'C1': {'name': 'Oman chips', 'price': 1.00, 'stock': 10},
            'C2': {'name': 'Snickers', 'price': 2.70, 'stock': 10},
            'C3': {'name': 'Doritos', 'price': 3.20, 'stock': 10},
            'D1': {'name': 'Oreo', 'price': 2.25, 'stock': 10},
            'D2': {'name': 'Kitkat', 'price': 3.00, 'stock': 10},
            'D3': {'name': 'Pringles', 'price': 4.00, 'stock': 10},
        }
        self.money_inserted = 0  #money inserted when initialized is set to 0

    #Function: display_items
    # Displays all the items in the dictionary self.items() for user to choose from 
    def display_items(self):
        print("---Vending Machine Menu---")
        for code, item in self.items.items():
            print(f"{code}: {item['name']} - AED {item['price']} (Stock: {item['stock']})")
        print("********************")
    
    #Function select_item
    # Lets the user input the item code to choose
    # if item not in the dictionary displays an invalid item code output.
    def select_item(self):
        item_code = input("Enter item code: ")
        if item_code in self.items:
            return item_code
        else:
            print("Invalid item code. Please try again.")
            return self.select_item()
        

    #Function insert_money 
    #Lets the user input the amount for the item they selected 
    # displays a message if the amount is not enough or when there is an invalid input. 
    def insert_money(self):
        try:
            amount = float(input("Insert money: AED"))
            if amount >= 0:
                self.money_inserted += amount
            else:
                print("Amount not enough.")
                self.insert_money()
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            self.insert_money()

    #Function insert_money 
    #Dispenses the item chosen after checking wether the item is in stock or wether the amount entered is correct. 
    def dispense_item(self, code):
        item = self.items[code]
        if item['stock'] > 0 and self.money_inserted >= item['price']:
            item['stock'] -= 1
            self.money_inserted -= item['price']
            print(f"{item['name']} dispensed. Enjoy your snack!")
            if self.money_inserted > 0:
                print(f"Change returned: ${self.money_inserted:.2f}")
        elif item['stock'] == 0:
            print("Sorry, this item is out of stock. Please choose another item.")
        else:
            print("Insufficient funds. Please insert more money or choose a cheaper item.")

    #Function buy_more
    #Asks the user if the want to buy or more snack 
    # if yes is entered, the code starts again or else it breaks in run function.
    def buy_more(self):
        return input("Do you want to purchase more snacks? (yes/no): ").lower() == 'yes'

    #Function create_bill
    #if no is selected in the buy_more() function than the bill is made and shown to the user.
    def create_bill(self, items):
        bill = "=== Vending Machine Bill ===\n"
        for item in items:
            bill += f"\t{item['name']} -- AED {item['price']:.2f}\n"

        total_sum = sum(item['price'] for item in items)
        bill += f"\tTotal Sum --- AED {total_sum:.2f}\n"

        return bill
    
    #Function run
    #This is the main function that calls all the other functions in order to make the vending machine work.
    def run(self):
        purchased_items = []
        while True:
            self.display_items()
            selected_item = self.select_item()
            self.insert_money()
            self.dispense_item(selected_item) #dispense item input by the user
            purchased_items.append(self.items[selected_item])
          
            if not self.buy_more(): #check if user wants to buy more
                print("Thank you for using the vending machine. Have a great day!")
                break

        # Generate and print the bill
        bill = self.create_bill(purchased_items)
        print(bill)
