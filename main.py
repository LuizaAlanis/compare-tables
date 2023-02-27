def intersect_lists(list_1, list_2):
    # Return common values in both lists
    return list(set(list_1) & set(list_2))


def format_input(list_input):
    # Using split() to separate elements
    elements = list_input.split(",")

    # Create new string array
    array_strings = []

    # Put each element in string
    for element in elements:
        array_strings.append(str(element))

    return array_strings


if __name__ == '__main__':
    list_1 = format_input(input("Enter the first header list: "))
    list_2 = format_input(input("Enter the second header list: "))

    print(intersect_lists(list_1, list_2))
