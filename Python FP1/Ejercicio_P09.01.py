def binary_search(sorted_sequence, value):
    if sorted_sequence == []:
        return False
    elif len(sorted_sequence) == 1:
        if sorted_sequence[0] == value:
            return True
        return False
    else:
        for elemento in sorted_sequence:
            if value == elemento:
                return True


if __name__ == "__main__":
    data = [
        38, 48, 56, 65, 76, 89, 92, 95, 105, 107,
        112, 117, 120, 126, 128, 130, 145, 154
    ]

    for num in range(90, 100):
        found = binary_search(data, num)
        print(f"¿Está el número {num}? {'Sí' if found else 'No'}")
