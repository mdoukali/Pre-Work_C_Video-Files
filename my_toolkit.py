# my_toolkit.py

numbers = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

# 

def calculate_average(numbers):
    """Calculates the average from a set of numbers, then returns the average."""
    average = 0
    sum_numbers = 0
    if not numbers:
        return 0
    for number in numbers:
        sum_numbers += number
        average = sum_numbers / len(numbers)

    return average

def find_max_and_min(numbers):
    """Find the highest and lowest numbers from a set of numbers, then returns the maximum and minimum value."""

    if not numbers:
        return 0, 0
    max_val = numbers[0]
    
    for number in numbers:
        if number > max_val:
            max_val = number

    min_val = max_val

    for number in numbers:
        if number < min_val:
            min_val = number

    return max_val, min_val

def count_occurrences(items, target):
    """Find every instance of a specified target and count them. Return how many of that specified target there is."""
    count = 0
    
    for item in items:
        if item == target:
            count += 1

    return count

def is_palindrome(text):
    """Determines if a string meets the requirements to be a palindrome. If it does, it returns true, if it doesn't it returns false."""

    text = text.lower().replace(" ", "")
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        elif text[left] == text[right]:
            left += 1
            right -= 1
    return True

def create_report(title, scores):
    """Creates a report with a title of the user's choosing and lists the average, maximum, and minimum number within the list."""
    average = calculate_average(scores)
    (max_val, min_val) = find_max_and_min(scores)

    formatted_string = f"=== {title} ===\n Average: {average:.1f}\n Max Score: {max_val:.1f}\n Min Score: {min_val:.1f}"

    return formatted_string

if __name__ == "__main__":
    # Test each function
    test_scores = [85, 92, 85, 95, 85, 70, 93]
    
    print(f"Average: {calculate_average(test_scores):.1f}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'A man a plan a canal Panama' palindrome: {is_palindrome('a')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print(create_report("Class Scores", test_scores))