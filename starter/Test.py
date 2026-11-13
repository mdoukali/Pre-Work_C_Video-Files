# Write a function that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zeroth index is even, therefore that character should be upper cased. Indexing resets for each word. In other words, the first letter of every word is index 0 (even), so it must always be uppercase, etc.

# The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

def to_weird_case(words):

    list_of_words = words.split()

    ans_list = []

    for word in list_of_words:
        
        new_word = to_word_weird_case(word)
        ans_list.append(new_word)

    return ' '.join(ans_list)

def to_word_weird_case(word):
    ans_word = []
    for index, char in enumerate(word):
        if index % 2 == 0:
            ans_word.append(char.upper())
        else:
            ans_word.append(char.lower())
    return ''.join(ans_word)

to_weird_case("THIs iS a TEST")