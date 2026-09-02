# Header
print("*" * 40)
print("\n           My To-Do List\n")
print("*" * 40)

# Display and create three tasks on to-do list
to_do_list = ["Call Mom", "Clean the bathroom", "Make dinner"]

print(f"\n1. {to_do_list[0]} \n2. {to_do_list[1]} \n3. {to_do_list[2]}")

print(f"\nTotal tasks: {len(to_do_list)}")

# Let the user add or remove a task
choices_list = ["Add a task", "Remove a task"]

print("\nWhat would you like to do?")
print(f"1. {choices_list[0]} \n2. {choices_list[1]}")

try:
    choose = int(input("\nChoose an option: "))
except ValueError:
    print("Sorry, but what you put was not an option. Exiting now.")
    exit()

if choose == 1:
    new_task = input("Enter new task: ")
    to_do_list.append(new_task)
    print(f"\n1. {to_do_list[0]} \n2. {to_do_list[1]} \n3. {to_do_list[2]} \n4. {to_do_list[3]}")
    new_length = len(to_do_list)
    print(f"\nTotal tasks: {new_length}")

elif choose == 2:
    try:
        remove_task = int(input("Remove a task (choose a number instead of typing the task, e.g. type 1 instead of 'Call Mom'): "))
    except ValueError:
        print("Sorry, but what you put was not an option. Exiting now.")
        exit()
    to_do_list.pop(remove_task-1)
    print(f"\n1. {to_do_list[0]} \n2. {to_do_list[1]}")
    new_length = len(to_do_list)
    print(f"\nTotal tasks: {new_length}")
else:
    print("Sorry, but what you put was not an option. Exiting now.")
    exit()