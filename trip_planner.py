# Input
destination_name = input("Destination: ")
total_distance = float(input("Total Distance (in miles): "))
fuel_efficiency = int(input("Fuel efficiency for car: "))
current_gas_price_per_gallon = float(input("Current price per gallon: $"))
number_of_nights = int(input("Number of nights: "))
average_hotel_cost_per_night = float(input("Cost of hotel stay per night: $"))
daily_food_budget = float(input("Daily food budget: $"))

# Calculations
gallons_needed = total_distance / fuel_efficiency
total_gas_cost = gallons_needed * current_gas_price_per_gallon
total_hotel_cost = number_of_nights * average_hotel_cost_per_night
total_food_cost = (number_of_nights + 1) * daily_food_budget
grand_total = total_gas_cost + total_hotel_cost + total_food_cost

# Output
print("*** 2026 Road Trip Budget ***")
print(f"\nDestination: {destination_name}")
print(f"Distance (in miles): {total_distance:.2f}")
print("\n*** Cost Breakdown ***")
print(f"\nGas ({int(gallons_needed)} gal x ${current_gas_price_per_gallon:.2f}/gal): ${total_gas_cost:.2f}")
print(f"Hotel ({number_of_nights} nights x ${average_hotel_cost_per_night:.2f}): ${total_hotel_cost:.2f}")
print(f"Food ({number_of_nights + 1} days x ${daily_food_budget:.2f}): ${total_food_cost:.2f}\n")
print("*" * 22)
print(f"\nEstimated Total: ${grand_total:.2f}")
