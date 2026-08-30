# fragile_calc.py - Crashes on bad input
bill = float(input("Enter the bill amount: $"))
tip_rate = float(input("Enter tip percentage (e.g., 20)"))

tip = bill * (tip_rate / 100)
total = bill + tip

print(f"\nTip: ${tip:.2f}")
print(f"Total: ${total:.2f}")