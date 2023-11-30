def magic_calculation(a, b):
    add, sub = magic_calculation_102.add, magic_calculation_102.sub

    if a < b:
        result = add(a, b)

        for i in range(4, 6):
            result = add(result, i)

        return result

    return sub(a, b)
