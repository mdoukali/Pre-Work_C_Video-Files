# Function A: O(1). No matter how large the data set is, retrieving the first element will always result in the same processing time because the computer is completing the same process regardless of what is passed in.

# Function B: O(n). The variable count will realistically go up the more items that go through a for loop.

# Function C: O(n^2). For each i value in data, each j value will be paired with each i value, therefor creating an i x j situation. Because i and j have the same length, this could also be represented as i x i, j x j, i^2, or j^2.

# Function D: O(n log n). The log n part comes from continuously halving n. The variable n is getting exponentially smaller (the inverse of a logarithm is an exponential function). Count will go up by one everytime n goes through the while loop, which is where the n part comes from.

# Function E: O(n). While accessing the first element would by O(1), finding the sum of a set of data would most likely be O(n) because you would have to loop through each item most likely and add it to a total.

from collections import Counter
import time 
import random

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10

def count_pairs_nested(data, target):
    """O(n^2)"""

    count = 0

    n = len(data)

    for i in range(n):
        for j in range(i + 1, n):
            if data[i] + data[j] == target:
                count += 1

    return count

def count_pairs_set(data, target):
    """O(n)"""

    s = Counter()
    count = 0

    for item in data:
        count += s[target - item]
        s[item] += 1
    
    return count

def benchmark(number):
    """Time how long a function takes to run."""
    start = time.time()
    end = time.time()
    return end - start

t_nested = benchmark(count_pairs_nested(data, target))
t_set = benchmark(count_pairs_set(data, target))

print(f"Nested = {t_nested:.8f}s    |   Set = {t_set:.8f}s")