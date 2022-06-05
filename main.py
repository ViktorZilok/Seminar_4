# Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию.

from random import randint

array = [randint(-100, 100) for i in range(21)]
print(array)


def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        position = i

        while position > 0 and arr[position - 1] > cursor:
            arr[position] = arr[position - 1]
            position = position - 1
        arr[position] = cursor
    return arr


with open('task_04.txt', 'w') as f:
    for i in array:
        str(i)
    array = ['{}'.format(i) for i in array]
    for i in array:
        i = i + '\n'
        f.write(i)

array = []

with open('task_04.txt', 'r') as f:
    array = f.readlines()
    array = list(map(int, array))
    array = insertion_sort(array)
    print(array)


with open('task_04.txt', 'w') as f:
    for i in array:
        str(i)

    array = ['{}'.format(i) for i in array]

    for i in array:
        i = i + '\n'
        f.write(i)

# Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя

my_list = [1, 5, 2, 3, 4, 6, 1, 7]

my_array = []
my_arr = []
j = 1

while j < len(my_list):
    i = j
    my_nums = my_list[:]
    while i < len(my_nums) - 1:
        if my_nums[i] < my_nums[i + 1]:
            my_arr.append(my_nums[i])
            i += 1
        else:
            my_nums.pop(i + 1)

    j += 1
    if len(my_array) < len(my_arr):
        my_array = my_arr
    my_arr = []

if my_list[-1] > my_array[-1]:
    my_array.append(my_list[-1])

if my_list[0] < my_array[0]:
    my_array.insert(0, my_list[0])

print(my_array)

