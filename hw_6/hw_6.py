# Бинарный поиск
# ● Контекст
# Предположим, что мы хотим найти элемент в массиве (получить его индекс). Мы можем это сделать просто перебрав
# все элементы. Но что, если массив уже отсортирован? В этом случае можно использовать бинарный поиск. Принцип прост:
# сначала берём элемент находящийся посередине и сравниваем с тем, который мы хотим найти. Если центральный элемент
# больше нашего, рассматриваем массив слева от центрального, а если больше - справа и повторяем так до тех пор, пока не
# найдем наш элемент.
# ● Ваша задача
# Написать программу на любом языке в любой парадигме для бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.
# Описать выбор парадигмы.

# Для решения поставленной задачи использованы процедурная (создание функции binary_search) и структурная (описание
# условий в функции, отсутствие goto) парадигмы программирования. Использование встроенной в Python функции len можно
# было бы отнести к декларативной парадигме, однако её влияние не велико.


def binary_search(sorted_list: list, start: int, end: int, number: int) -> int | str:
    if start == end and sorted_list[start] != number or len(sorted_list) == 1 and sorted_list[0] != number:
        return -1
    middle = start + (end - start) // 2
    if number == sorted_list[middle]:
        return f'Индекс элемента {number} равен {middle}'
    elif number > sorted_list[middle]:
        return binary_search(sorted_list, middle+1, end, number)
    elif number < sorted_list[middle]:
        return binary_search(sorted_list, start, middle-1, number)


if __name__ == '__main__':
    sorted_list = [1, 3, 4, 6, 7, 8, 10, 13, 14]
    number = 4
    print(binary_search(sorted_list, 0, len(sorted_list) - 1, number))
