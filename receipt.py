# List out input values

item1_name = "Notebook"
item1_price = "4.99"
item1_qty = "2"

item2_name = "Pen Pack"
item2_price= "7.50"
item2_qty = "1"

item3_name = "Backpack"
item3_price = "34.99"
item3_qty = "1"

tax_rate = "0.075"  # 7.5% sales tax

# Convert str to int or float values

first_item = float(item1_price)
second_item = float(item2_price)
third_item = float(item3_price)

first_item_quantity = int(item1_qty)
second_item_quantity = int(item2_qty)
third_item_quantity = int(item3_qty)

tax_percentage = float(tax_rate)

# Equations

price_1 = first_item * first_item_quantity
price_2 = second_item * second_item_quantity
price_3 = third_item * third_item_quantity

total_price = price_1 + price_2 + price_3

tax_amount = total_price * tax_percentage

grand_total = tax_amount + total_price

# Format the receipt

print("=" * 40)
print("\n              STORE RECEIPT\n")
print("=" * 40)

print(f"\n{item1_name}    ${first_item} x {first_item_quantity}    ${price_1}")
print(f"\n{item2_name}    ${second_item:.2f} x {second_item_quantity}    ${price_2:.2f}")
print(f"\n{item3_name}    ${third_item} x {third_item_quantity}    ${price_3}\n")

print("-" * 40)
print(f"\nSubtotal:        ${total_price}")
print(f"Tax ({tax_percentage * 100}%):      ${tax_amount:.2f}")
print(f"Total:           ${grand_total:.2f}\n")

print("=" * 40)
