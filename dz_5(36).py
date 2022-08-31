# Дан список чисел. Создать список, в который попадают числа,
# описываемые возрастающую последовательность.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя

my_list = [1, 5, 2, 3, 4, 6, 1, 7]
ascending_sequence = []
ascending_sequence.append(min(my_list))
ascending_sequence.append(max(my_list))
print(ascending_sequence)