
# Inventory Management System

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount):
        self.quantity += amount
        print(f"Added {amount} units of {self.name}. New stock: {self.quantity}")

    def sell(self, amount):
        if amount > self.quantity:
            print(f"Insufficient stock for {self.name}. Available: {self.quantity}")
        else:
            self.quantity -= amount
            print(f"Sold {amount} units of {self.name}. Remaining stock: {self.quantity}")

    def __str__(self):
        return f"{self.name} - Price: ${self.price}, Quantity: {self.quantity}"

# Inventory management class
class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, name, price, quantity):
        if name in self.products:
            print(f"{name} already exists in the inventory. Use 'restock' instead.")
        else:
            self.products[name] = Product(name, price, quantity)
            print(f"Added {name} to the inventory.")

    def restock_product(self, name, amount):
        if name in self.products:
            self.products[name].add_stock(amount)
        else:
            print(f"{name} does not exist in the inventory.")

    def sell_product(self, name, amount):
        if name in self.products:
            self.products[name].sell(amount)
        else:
            print(f"{name} does not exist in the inventory.")

    def view_inventory(self):
        print("\nCurrent Inventory:")
        for product in self.products.values():
            print(product)

# Main program to interact with the inventory system
if __name__ == "__main__":
    inventory = Inventory()

    # Add some initial products to the inventory
    inventory.add_product("Apple", 0.50, 100)
    inventory.add_product("Orange", 0.70, 80)
    inventory.add_product("Milk", 1.50, 50)

    # Perform some operations
    inventory.restock_product("Apple", 20)  # Restock Apples
    inventory.sell_product("Orange", 30)    # Sell Oranges
    inventory.view_inventory()              # View current inventory
