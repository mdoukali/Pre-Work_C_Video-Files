# Snippet 1
# print("The answer is: " + "42")

# Snippet 2 
# favorite = int(input("Favorite number: "))
# result = favorite + 10
# print(result)

# Snippet 3
# print("Hello World")

# Snippet 4
# age = int("25")

# Snippet 5
# username = input("Enter your username: ")
# print(username)

try:
    enter_1 = int(input("Enter number 1: "))
except ValueError:
    enter_1 = 0
    print("That's not a valid number. Using 0 instead.")

try: 
    enter_2 = int(input("Enter number 2: "))
except ValueError:
    enter_2 = 0
    print("That's not a valid number. Using 0 instead.")

try: 
    enter_3 = int(input("Enter number 3: "))
except ValueError:
    enter_3 = 0
    print("That's not a valid number. Using 0 instead.")

sum = enter_1 + enter_2 + enter_3
average = (sum / 3)

print(f"Your numbers: {enter_1}, {enter_2}, {enter_3}")
print(f"Sum: {sum}")
print(f"Average: {average:.2f}")