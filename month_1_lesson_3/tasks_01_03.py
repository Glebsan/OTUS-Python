import itertools
# def power(a, p=2):
#     """
#     Написать функцию, которая принимает N целых чисел и возвращает список квадратов эих чисел. Бонусом будет сделать keyword аргумент для выбора степени, в которую будут возводиться числа.
#     РЕШЕНИЕ ЧЕРЕЗ APPEND ЭЛЕМЕНТА В СПИСОК
#     :param a: список целых чисел
#     :param p: степень
#     :return: возвращает ноый список
#     """
#     answ = []
#     for i in a:
#         answ.append(i ** p)
#     return answ


def power(a, p=2):
    """РЕШЕНИЕ ЧЕРЕЗ COMPREHENSION"""
    answ = [i ** p for i in a]
    return answ

def power(a, p=2):
    """РЕШЕНИЕ ЧЕРЕЗ MAP
       :param a: список целых чисел
       :param p: степень
       :return: возвращает ноый список
       """
    return list(map(pow, a, itertools.repeat(p)))

def prime_num(a):
    """ПРОВЕРКА НА ПРОСТОЕ ЧИСЛО True/False"""
    i = 2
    while a > 1 and i * i < a and a % i != 0:
        i += 1
    return i * i > a

ODD = 'odd'
EVEN = 'even'
SIMPLE = 'simple'


def numbers(a, b = EVEN):
    if b == 'even':
        answ = list(filter(lambda x: x % 2 == 0, a))
    elif b == 'odd':
       answ = list(filter(lambda x: x % 2 != 0, a))
    elif b == 'simple':
        answ = list(filter(prime_num, a))
    return answ



test = [1, 2, 3, 4, 5]

print("Написать функцию, которая принимает N целых чисел и возвращает список квадратов этих чисел.")
print('Функция принимает на вход список:', test, 'и возводит в степень.(по-умолчанию "2"):', power(test))
print('Функция принимает на вход список:', test, 'и возводит в степень(4) указанную во втором аргументе функции:',
      power(test, 4))
print()
print("Написать функцию, которая на вход принимает список из целых чисел, и возвращает только чётные/нечётные/простые числа")
print("Функция принимает на вход список:", test, "и возвращает тоько четные числа (по-умолчанию):",numbers(test))
print("Функция принимает на вход список:", test, "и возвращает тоько нечетные числа (по-умолчанию):",numbers(test, ODD))
print("Функция принимает на вход список:", test, "и возвращает тоько простые числа (по-умолчанию):",numbers(test, SIMPLE))
