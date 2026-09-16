# buggy_program.py - Contains 4 bugs. Find and fix them all.

def calculate_stats(numbers):
   
    number = list(numbers)
    total = sum(numbers)
    count = len(number)
    average = total / count

    above_average = [num for num in numbers if num > average]

    return {
        "total": total,
        "average": average,
        "above_average": above_average,
        "above_count": len(above_average)
    }

scores = [93, 92, float("inf")]
result = calculate_stats(scores)

print(f"Total: {result['total']}")
print(f"Average: {result['average']}")
print(f"Above average: {result['above_count']} scores")