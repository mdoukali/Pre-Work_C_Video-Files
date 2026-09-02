# Dictionary of at least four products

inventory = {
    "Hoodies": {"price": 29.99, "quantity": 50},
    "T-shirts": {"price": 15.99, "quantity": 25},
    "Jeans": {"price": 42.99, "quantity": 15},
    "Sneakers": {"price": 23.99, "quantity": 20},
    "Hats": {"price": 12.99, "quantity": 30}
}

# Display the full inventory in a formatted table

def display_inventory():
    """Print out inventory."""
    print("\n" + "=" * 40)
    print("     Inventory")
    print("=" * 40)
    print(f"{'Item':<12}{'Price'}{'Quantity':>12}")

    for key, info in inventory.items():
        price = info.get("price")
        quantity = info.get("quantity")
        print(f"{key:<12}${price:.2f}{quantity:>12}")

display_inventory()

# Display the capital of the inventory

value = 0

for key, info in inventory.items():
    value += info.get("price") * info.get("quantity")
    
print(f"\nThe total value of all of the inventory is ${value:.2f}.")


# Look up inventory

search = input("\nLook up an item in the system: ")

item = inventory.get(search)

if item:
    print(f"\nItem: {(search)}")
    print(f"Price: ${item.get('price')}")
    print(f"Quantity: {item.get('quantity')}")
else:
    print("Product not found.")
    exit()

# Update the quantity of a product (a sale or restock)

update = input("\nEnter the product you wish to update the quantity of: ")

item = inventory.get(update)

if item:
    sold_restocked = int(input("\nEnter how many products sold or restocked (e.g. +5 or -5): "))
    if -sold_restocked > item['quantity']:
        print("Sorry, but that would result in a negative quantity. Try again.")
        exit()

    item['quantity'] += sold_restocked

    print(f"\nUpdated: {update}")
    print(f"New Quantity: {item['quantity']}")
    print(f"Sold/Restocked: {sold_restocked}")

    stock_low = set()
    for name, info in inventory.items():
        if info['quantity'] < 10:
            low = stock_low.add(name)
            print(f"Alert! {name} are running low. Consider restocking. ")

else:
   print("Product not found.")
   exit()




        

