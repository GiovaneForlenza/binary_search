import time
from random import randint

array = []
# range_max = int(input('What\'s the max range? '))
range_max = 100
range_min = 1

count = 1
for i in range(range_max):
    array.append(i + 1)  # print(f'{i}, ', end='')  # time.sleep(0.3)


def get_random_int(min, max):
    return randint(min, max)


def binary_search():
    global i
    tries_array = []
    for i in range(1000000):
        selected_num = get_random_int(range_min, range_max)
        found = False
        checked_min = range_min
        checked_max = range_max
        picked_number = -1
        tries = 0
        while not found:
            tries += 1
            picked_number = get_random_int(checked_min, checked_max)
            if picked_number == selected_num:
                found = True
            else:
                if picked_number > selected_num:
                    checked_max = picked_number - 1
                elif picked_number < selected_num:
                    checked_min = picked_number + 1
        tries_array.append(tries)
    print(f'Games: {len(tries_array)}')
    # print(f'Tries per game: {tries_array}')
    average = sum(tries_array) / len(tries_array)
    print(f'Average tries to find: {int(average)}')


binary_search()
