# Exercise 1 - Turn the shopping cart program from yesterday into an object-oriented program

import math
item_stock = {
    'small water' :("Small Water", 2.50),
    'medium water' : ("Medium Water", 4.50),
    'large water' : ("Large Water", 6.00),
    'water case' : ("Water Case", 10.00),
    'model car' : ("Model Car", 25.00),
    'model tank' : ("Model Tank", 30.00),
    'model plane' : ("Model Plane", 28.00),
    'hammer' : ("Hammer", 8.00),
    'screwdriver' : ("Screwdriver", 5.50),
    'pliers' : ("Pliers", 4.20),
    'pasta' : ("Pasta", 5.00),
    'sausage': ("Sausage", 5.50),
    'hard drive': ("Hard Drive", 50.00),
    'sd card' : ("SD Card", 75.00)
}
class Cart(object):
    def __init__(self):
        self.items = []

    def add_item(self, item_name):
        if item_name in item_stock:
            self.items.append(item_name)

        

    def remove_item(self, item_name):
        if item_name not in self.items:
            print(f"{item_name} is not in your cart or your selection was misspelled.\n")
        else: self.items.remove(item_name), print(f"{item_name} has been removed!\n")


    def print_cart_nice(self):
        for item in self.items:
            pretty_name, price = item_stock[item]
            print(f"{pretty_name}: ${price:.2f}")


    def view_cart(self):
        print(f"Your cart currently has: ")
        self.print_cart_nice()


    def checkout(self):
        total_cost = sum([item_stock[item][1] for item in self.items])
        print(f"Your final cart consists of: ")
        self.print_cart_nice()
        print(f"Total cost: ${total_cost:.2f}")

cart = Cart()
for small_name, (pretty_name, price) in item_stock.items():
    print(f"{pretty_name}: ${price:.2f}")

while True:
    cart_item = input("Please enter an item to add to your cart. Enter 'Quit' when finished, or 'Cart' to view your cart or 'remove item' to delete a selection\n").lower().strip()
    if cart_item == "quit":
        cart.checkout()
        break

    elif cart_item == "cart":
        cart.view_cart()

    elif cart_item == "remove item":
        remove_item = input(f"What item would you like to be eradicated from your eternal container?\n")
        cart.remove_item(remove_item)

    elif cart_item in item_stock:
        cart.add_item(cart_item)
    else:
         print(f"Sorry, we do not have {cart_item}")

#Exercise 2 - Write a Python class which has two methods get_String and print_String.
# Get_String accept a string from the user and print_String print the string in upper case

class Stringy():
    def __init__(self):
        self.stringy = ""
    def get_String(self):
        self.stringy = input(f"Give me your string.\n")

    def print_String(self):
        print(self.stringy.upper())

stringy = Stringy()
stringy.get_String()
stringy.print_String()