# Функция перевода чисел из десятичной системы в двоичную
def convert_to_bin(intgr):
    bin_num = []
    while True:
        digit = intgr % 2
        bin_num.append(digit)
        intgr //= 2
        if intgr == 0:
            break
    result = ''
    bin_num.reverse()
    for i in bin_num:
        result += str(i)
    return result


# Функция деления
def division (a, b):
    return a / b