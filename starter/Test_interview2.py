# You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet).

# Input:

# If, you can read?

# Output:

# India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?

# Note:

# There is a preloaded dictionary that you can use, named NATO. It uses uppercase keys, e.g. NATO['A'] is "Alfa". See comments in the initial code to see how to access it in your language.
# The set of used punctuation is ,.!?.
# Punctuation should be kept in your return string, but spaces should not.
# Xray should not have a dash within.
# Every word and punctuation mark should be seperated by a space ' '.
# There should be no trailing whitespace

def to_nato(words : str) -> str:

    military_alphabet = {
        "A": "Alfa",
        "B": "Beta",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliett",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "Xray",
        "Y": "Yankee",
        "Z": "Zulu"
    }

    converted_sentence = []

    for char in words:
        if char == "?":
            converted_sentence.append(char)
        elif char == "!":
            converted_sentence.append(char)
        elif char ==".":
            converted_sentence.append(char)
        elif char == " ":
            continue
        else:
            uppercase = char.upper()
            converted_sentence.append(military_alphabet[uppercase])

    return ' '.join(converted_sentence)

print(to_nato("Do You Know Where Your Children Are?"))