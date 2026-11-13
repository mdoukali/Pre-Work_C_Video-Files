# def filter_list(l)

# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]


def filter_list(l):

    # Initialize an empty array
    filtered_list = []

    # Access each item in the list
    for item in l:
        try:
            if item == int(item):
                filtered_list.append(item)
        except ValueError:
            continue

    return filtered_list


filter_list([1, 2, "a", "b"])
