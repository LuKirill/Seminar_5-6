# Даны два файла в каждом из которых находится запись многочлена.
# Сформировать файл содержащий сумму многочленов.

with open("text1.txt", "r", encoding="utf-8") as f:
    read_txt1 = f.read()[:-4]
print(read_txt1)
with open("text2.txt", "r", encoding="utf-8") as fu:
    read_txt2 = fu.read()[:-4]
polinomial_sum = " + ".join([read_txt1, read_txt2])
with open("pol_num.txt", 'w', encoding="utf=8") as fp:
    fp.write(polinomial_sum)
