import time
import random

def has_duplicate_nested(data):
    """Compare every element to every other element, so n * n. O(n^2)"""
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] == data[j]:
                return True
    return False

def has_duplicate_sort(data):
    """Sort first, then check neighbors. O(n log n)"""
    sorted_data = sorted(data)
    for i in range(len(sorted_data) - 1):
        if sorted_data[i] == sorted_data[i + 1]:
            return True
    return False

def has_duplicate_set(data):
    """Use a set - seen items are tracked for instant lookup. O(n)"""
    seen = set()

    for item in data:
        if item in seen:
            return True
        seen.add(item)
    return False

def benchmark(func, data):
    """Time how long a function takes."""
    start = time.time()
    func(data)
    end = time.time()
    return end - start

sizes = [1000, 5000, 10000, 20000]

print(f"{'n':>7}    |   {'Nested (n^2)':>12}    |   {'Sort (n log n)':>14}  |   {'Set (n)':>10}")

print("-" * 60)

for size in sizes:
    data = list(range(size))
    random.shuffle(data)

    t1 = benchmark(has_duplicate_nested, data)
    t2 = benchmark(has_duplicate_sort, data)
    t3 = benchmark(has_duplicate_set, data)

    print(f"n = {size:>6}   |   {t1:>10.4f}s  |    {t2:12.4}s    |   {t3:8.4}s")