def rot13(message):
    
    # List of every letter in alphabet
    alphabet_list_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    alphabet_list_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    n = 13

    ciphered = []
    
    # Should go through each letter, starting with the first
    for char in message:

        # Check if letter is uppercase
        # Get index
        if char.isupper():
            alphabet_index_upper = alphabet_list_upper.index(char)
            rote13_index_upper = alphabet_index_upper + 13
            if rote13_index_upper > 25:
                ciphered.append(alphabet_list_upper[alphabet_index_upper % n])
            else:
                ciphered.append(alphabet_list_upper[alphabet_index_upper + 13])
        elif char.islower():
            alphabet_index_lower = alphabet_list_lower.index(char)
            rote13_index_lower = alphabet_index_lower + 13
            if rote13_index_lower > 25:
                ciphered.append(alphabet_list_lower[alphabet_index_lower % n])
            else:
                ciphered.append(alphabet_list_lower[alphabet_index_lower + 13])
        else:
            ciphered.append(char)

    return ''.join(ciphered)

rot13("aA bB zZ 1234 *!?%")