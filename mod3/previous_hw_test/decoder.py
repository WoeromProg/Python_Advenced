def decoder(cipher):
    result = []

    for i in cipher:
        result.append(i)

        if len(result) > 2 and result[-1] == '.' and result[-2] == '.':
            result.pop()
            result.pop()
            if len(result) > 0:
                result.pop()

    result = ''.join(x for x in result if x != '.')
    return result


#print(decoder(input("Введите шифр (3 задание):")))