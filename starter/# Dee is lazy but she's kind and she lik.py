# Dee is lazy but she's kind and she likes to eat out at all the nice restaurants and gastropubs in town. To make paying quick and easy she uses a simple mental algorithm she's called The Fair %20 Rule. She's gotten so good she can do this in a few seconds and it always impresses her dates but she's perplexingly still single. Like you probably.

# This is how she does it:

# She rounds the price P at the tens place e.g:
# 25 becomes 30
# 24 becomes 20
# 5 becomes 10
# 4 becomes 0
# She figures out the base tip T by dropping the singles place digit e.g:
# when P = 24 she rounds to 20 drops 0 T = 2
# P = 115 rounds to 120 drops 0 T = 12
# P = 25 rounds to 30 drops 0 T = 3
# P = 5 rounds to 10 drops 0 T = 1
# P = 4 rounds to 0 T = 0
# She then applies a 3 point satisfaction rating R to T i.e:
# When she's satisfied: R = 1 and she'll add 1 to T
# Unsatisfied: R = 0 and she'll subtract 1 from T
# Appalled: R = -1 she'll divide T by 2, rounds down and subtracts 1
# Your Task
# Implement a method calc_tip that takes two integer arguments for price p

# where 1 <= p <= 1000 and a rating r which is one of -1, 0, 1.

# The return value T should be a non negative integer.

# Note: each step should be done in the order listed.

# Dee always politely smiles and says "Thank you" on her way out. Dee is nice. Be like Dee.


def calc_tip(p, r):

    # last_digit
    last_digit = p % 10
    first_two_digits = 0

    # If number ends in 5 or more, round up.
    if last_digit >= 5:
        first_two_digits = p // 10
        first_two_digits += 1
    else:
        # If number ends in 4 or less, round down.
        first_two_digits = p // 10

    if r == 1:
        first_two_digits += 1
        return first_two_digits
    elif r == 0:
        first_two_digits -= 1
        if first_two_digits < 0:
            first_two_digits += 1
            return first_two_digits
        return first_two_digits
    elif r == -1:
        first_two_digits = (first_two_digits // 2) - 1
        if first_two_digits < 0:
            first_two_digits += 1
        return first_two_digits

calc_tip(4, -1)
