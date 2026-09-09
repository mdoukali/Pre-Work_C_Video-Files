# sales_analyzer.py

import csv

# Open original "sales_data.csv" and read through it
with open("sales_data.csv", "r") as file:
    read_data = csv.DictReader(file)

    revenue_total = 0
    revenue_product = {}
    product_quantity = {}
    day_revenue = {}
    for row in read_data:
        product = row["product"]
        quantity = int(row["quantity"])
        price = float(row["price"])
        date = row["date"]


        # Create the total revenue and store in in revenue_total
        revenue_total += quantity * price
        
        # Insert in a dictionary with the total revenue for Widget A, Widget B, and Widget C
        if product not in revenue_product:
            revenue_product[product] = 0
        revenue_product[product] += quantity * price

        # Insert in dictionary total quantity sold per product (Widget A, B, and C)
        if product not in product_quantity:
            product_quantity[product] = 0
        product_quantity[product] += quantity
        
        # Filter out the day with the highest total revenue
        if date not in day_revenue:
            day_revenue[date] = 0        
        day_revenue[date] += quantity * price

        largest = 0

        # Finds the day with the largest revenue
        for day in day_revenue:
            if day_revenue[day] > largest:
                largest = day_revenue[day]


# Write a formatted sales report to sales_report.txt

with open("sales_report.txt", "w") as file:
    file.write("*** SALES REPORT ***\n\n")
    file.write(f"Total revenue: ${revenue_total:.2f}\n\n")
    file.write("Revenue for each product: \n\n")
    for product in revenue_product:
        file.write(f"{product}: ${revenue_product[product]:.2f}\n")
    file.write(f"\nTotal quantity for each product: \n\n")
    for product in product_quantity:
        file.write(f"{product}: {product_quantity[product]} items\n")
    file.write("\nThe day with the largest revenue: \n")
    day = max(day_revenue, key = day_revenue.get)
    file.write(f"{day}: ${largest:.2f}")


# Writes a summary CSV called product_summary.csv with columns: product, total_quantity, total_revenue

with open("product_summary.csv", "w", newline="") as file:
    write = csv.DictWriter(file, fieldnames=["product", "total_quantity", "total_revenue"])
    write.writeheader()

    # Creates a new dictionary with the key (product), total quantity of that product, and total revenue of said product
    for product, revenue in revenue_product.items():
        quantity = product_quantity[product]
        product_row = {
            "product": product,
            "total_quantity": quantity,
            "total_revenue": f"${revenue:.2f}"
        }
        write.writerow(product_row)
        