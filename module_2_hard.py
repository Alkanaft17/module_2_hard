def password(n):
    name: list = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                name.extend(str(i) + str(j))
            else:
                continue
    return name
n = int(input('Введите число из диапазона (3,20): '))
print('Нужный пароль: ', n, '-', *password(n), sep='') # sep= нужен, чтобы убрать пробелы между 1 2 1 5 и тд.