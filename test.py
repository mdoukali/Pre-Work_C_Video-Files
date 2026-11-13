def descending_order(num):
    
    number = [int(n) for n in str(num)]

    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            if number[j] > number[i]:
                number[i], number[j] = number[j], number[i]
        final_number = "".join(str(n) for n in number)

    return int(final_number)

descending_order(64392745)