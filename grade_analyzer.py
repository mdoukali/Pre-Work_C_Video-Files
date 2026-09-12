# Start with an array of student's scores
scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

# Title of the program
print("=== Grade Analyzer ===")

# Find total of all scores

print(f"\nTotal number of scores: {len(scores)}")

# Use a for loop to iterate through the scores and categorize each one:

# Initializing variables
number_of_as = 0
number_of_bs = 0
number_of_cs = 0
number_of_ds = 0
number_of_fs = 0
total_score = 0
highest = 0
lowest = 100
pass_score = 0
fail_score = 0

for score in scores:
    # Calculate total score
    total_score += score

    # Calculate highest and lowest score
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score

    # Sorts scores into pass vs fail
    if score < 60 and score >= 0:
        fail_score += 1
    elif score >= 60 and score <= 100:
        pass_score += 1

    # Sorts scores and counts how many A's, B's, C's, D's, F's
    if score >= 90 and score <= 100:
        number_of_as += 1
    elif score >= 80 and score <= 89:
        number_of_bs += 1
    elif score >= 70 and score <= 79:
        number_of_cs += 1
    elif score >= 60 and score <= 69:
        number_of_ds += 1
    elif score >= 0 and score <= 59:
        number_of_fs += 1
    else:
        print("Scores can't be negative or above 100.")

# Printing the grade distribution
print("\nGrade Distribution:")
print(f"\nNumber of A's: {number_of_as}")
print(f"Number of B's: {number_of_bs}")
print(f"Number of C's: {number_of_cs}")
print(f"Number of D's: {number_of_ds}")
print(f"Number of F's: {number_of_fs}")

# Find the average of the scores and print
average = total_score / len(scores)
print(f"\nAverage score: {average:.1f}%.")

# Print the highest and lowest score
print(f"\nHighest score: {highest}%.")
print(f"Lowest score: {lowest}%.")

# Find the amount of people who pass and who fail
print(f"\nNumber of Passing Scores: {pass_score} ({(pass_score/len(scores))*100:.1f}%).")
print(f"Number of Failing Scores: {fail_score} ({(fail_score/len(scores))*100:.1f}%).")

# Add more scores
print("-- Add More Scores --")

while True:
    # Enter a new score
    enter_score = input("Enter a new score (or 'done' to finish): ")

    # If the user enters "done" the program break
    if enter_score.lower() == "done":
        average = total_score / len(scores)
        print(f"Final average: {average:.1f}")
        break

    # Catches errors like "a" and scores that are above 100 and below 0
    try:
        float_enter_score = float(enter_score)
        if float_enter_score >= 0 and float_enter_score <= 100:
            scores.append(float_enter_score)
            total_score += float_enter_score
            new_average = total_score / len(scores)
            print(f"Updated average: {new_average:.1f}")

        else:
            print("That score is less than zero and greater than one-hundred. Try again.")
    except ValueError:
        print("That's not a score or the word 'done'. Please try again.")


    
