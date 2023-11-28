# Ваша задача
# Реализовать процедуру для вычисления MSE на любом языке в любой парадигме. Программа получает
# на вход два вектора и возвращает число - оценку MSE для этих векторов.


def sub_lists(list_1: list, list_2: list) -> float:
    return sum([(list_1[i] - list_2[i]) ** 2 for i in range(len(list_1))]) / len(list_1)


if __name__ == '__main__':
    list_1 = [1, 2, 3, 4]
    list_2 = [5, 6, 7, 8]
    print(sub_lists(list_1, list_2))
