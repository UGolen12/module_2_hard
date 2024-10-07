number = int(input('Введите целое число от 3 до 20: '))


def get_password(number):
    result = ''
    for i in range(1, number):
        for j in range(1, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                result += str(i) + str(j)
    return result


result = get_password(number)
print('Пароль:', result)
