def restos(lista1, lista2):
    new_list = []
    for i in range(len(min(lista1, lista2))):
        if lista1[i] > lista2[i]:
            num = lista1[i] % lista2[i]
            new_list.append(num)
        else:
            num = lista2[i] % lista1[i]
            new_list.append(num)
    return new_list


if "__main__" == __name__:
    lista1 = [8, 12, 2, 10]
    lista2 = [3, 4, 5, 5]
    print(restos(lista1, lista2))
