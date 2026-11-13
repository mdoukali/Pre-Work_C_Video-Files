# Function A: O(1). No matter how large the data set is, retrieving the first element will always result in the same processing time because the computer is completing the same process regardless of what is passed in.

# Function B: O(n). The variable count will realistically go up the more items that go through a for loop.

# Function C: O(n^2). For each i value in data, each j value will be paired with each i value, therefor creating an i x j situation. Because i and j have the same length, this could also be represented as i x i, j x j, i^2, or j^2.

# Function D: O(n log n). The log n part comes from continuously halving n. The variable n is getting exponentially smaller (the inverse of a logarithm is an exponential function). Count will go up by one everytime n goes through the while loop, which is where the n part comes from.

# Function E: O(n). While accessing the first element would by O(1), finding the sum of a set of data would most likely be O(n) because you would have to loop through each item most likely and add it to a total.

from collections import Counter

def count_pairs_nested(number, target):
    """O(n^2)"""

    count = 0

    n = len(number)

    for i in range(n):
        for j in range(i + 1, n):
            if number[i] + number[j] == target:
                count += 1

    return count

def count_pairs_set(number, target):
    """O(n)"""

    s = Counter()
    count = 0

    for item in number:
        count += s[target - item]
        s[item] += 1
    
    return count