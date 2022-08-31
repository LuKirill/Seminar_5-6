# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = 2
x = random.randrange(0, 100, 1)
with open("text1.txt", "w", encoding="utf-8") as f:
    f.write("2 * x ** k + 4 * x + 5 = 0")
with open("text2.txt", "w", encoding="utf-8") as f:
    f.write("x ** k + 5 = 0")