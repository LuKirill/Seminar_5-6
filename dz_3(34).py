# Даны два файла в каждом из которых находится запись многочлена.
# Сформировать файл содержащий сумму многочленов.

# 2*(x**46) + 4*(x**1) + 5*(0**0)
# 1*(x**46) + 0 + 5*(0*0)
# => (2 + 1) + (4 + 0) + (5 + 5)

with open("text1.txt", "r", encoding="utf-8") as f:
    read_txt1 = f.read()[:-4]
read_txt1 = read_txt1.replace(read_txt1[read_txt1.find("** ") + 2:read_txt1.find("** ") + 5], "")
x_list1 = read_txt1.split()
num_list1 = [int(num) for num in filter(
    lambda num: num.isnumeric(), x_list1)]
print(num_list1)

with open("text2.txt", "r", encoding="utf-8") as fu:
    read_txt2 = fu.read()[:-4]
read_txt2 = read_txt2.replace(read_txt2[read_txt2.find("** ") + 2:read_txt2.find("** ") + 5], "")
x_list2 = read_txt2.split()
x_list2.insert(0, "1")
x_list2.insert(3, "0")
num_list2 = [int(num) for num in filter(
    lambda num: num.isnumeric(), x_list2)]
print(num_list2)

polinomial_sum = [x + y for x, y in zip(num_list1, num_list2)]
print(polinomial_sum)
polinomial_sum.insert(1, "x")
polinomial_sum.insert(2, "**")
polinomial_sum.insert(3, 48)
polinomial_sum.insert(4, "+")
polinomial_sum.insert(6, "x")
polinomial_sum.insert(7, "+")
polinomial_sum = [str(x) for x in polinomial_sum]
polinomial_sum = " ".join(list(polinomial_sum))
print(polinomial_sum)
with open("pol_num.txt", 'w', encoding="utf=8") as fp:
    fp.write(str(polinomial_sum))