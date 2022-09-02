# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

import random
a = []
for i in range(5):
    a.append(random.randint(1, 5))
print(a)
b = ' '.join(str(x) for x in a)
with open("file.txt", "w", encoding='utf-8') as f:
    f.write(str(b))
with open("file.txt", "r", encoding='utf-8') as fo:
    b = fo.read()
b = b.split(" ")
b = [int(x) for x in b]
b.sort()
for j in range(len(b) + 1):
    if b[j + 1] == b[j] + 1:
        b.append(b[j] + 1)
        break
print(b)

