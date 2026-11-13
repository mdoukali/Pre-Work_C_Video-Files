# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):

    vowel = 0

    for char in sentence:
        if char == "a":
            vowel += 1
        elif char == "e":
            vowel += 1
        elif char == "o":
            vowel += 1
        elif char == "i":
            vowel += 1
        elif char == "u":
            vowel += 1

    return vowel

get_count("abracadabra")
    