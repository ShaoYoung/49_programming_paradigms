# Ваша задача
# Реализовать секундомер на любом языке программирования в любой парадигме. Секундомер должен поддерживать
# следующий функционал:
# ○ Запуск
# ○ Пауза
# ○ Выход из паузы
# ○ Остановка


import time


def watch():
    result_time = start_time = 0
    is_start = False
    is_pause = False
    while True:
        command = int(input('Введите команду: '))
        match command:
            case 1:
                if not is_start:
                    start_time = time.time()
                    is_start = True
                    print('Секундомер запущен')
            case 2:
                if is_start:
                    if not is_pause:
                        result_time += time.time() - start_time
                    is_pause = True
                    start_time = 0
                    print(f'Пауза. Прошло {int(result_time)} секунд')
            case 3:
                if is_start:
                    if is_pause:
                        start_time = time.time()
                        is_pause = False
                        print('Секундомер запущен после паузы')
            case 4:
                if is_start:
                    if not is_pause:
                        result_time += time.time() - start_time
                    print(f'Секундомер остановлен. Прошло {int(result_time)} секунд')
                    break
            case _:
                print('Повторите ввод')


if __name__ == '__main__':
    watch()
