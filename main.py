def intersect_lists(list_1, list_2):
    """
    Retorna os valores em comum entre duas listas.
    """
    return list(set(list_1) & set(list_2))


def format_input(list_input):
    # Separar elementos da lista usando o método split()
    elements = list_input.split(",")

    # Inicializar um novo array de strings
    array_strings = []

    # Adicionar cada elemento da lista ao array de strings
    for element in elements:
        array_strings.append(str(element))

    return array_strings


if __name__ == '__main__':
    list_1 = format_input(input("Enter the first header list: "))
    list_2 = format_input(input("Enter the second header list: "))

    print(intersect_lists(list_1, list_2))
