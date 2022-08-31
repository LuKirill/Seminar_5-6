# Дан список чисел. Создать список в который попадают числа,
# описывающие возрастающую последовательность и содержащие максимальное количество элементов.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#    [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя

#нужно сделать список, где list[i - 1] < list[i] < list[i + 1]
#начинаем со 2го элемента, если list[i - 1] <= list[i] - удаляем list[i - i] из списка
#если list[i] >= list[i + 1] - удаляем list[i] из списка
#для последнего элемента списка list[i] > list[i - 1]
my_list = [1, 5, 2, 3, 4, 6, 1, 7]
try:
    for i in range(1, len(my_list)):
        for j in range(i + 1, len(my_list)):
            for k in range(i - 1, len(my_list)):
                if my_list[i] < my_list[j]:
                    if my_list[i] > my_list[k]:
                        print(my_list)
                else:
                    del my_list[i]
except IndexError:
    print("list index out of range")
# print(my_list)