# Помните игру с конфетами из модуля "Математика и Информатика"?
# Создайте такую игру для игры человек против человека
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

def game():
    n = int(input("Введите кол-во конфет: "))
    m = int(input("Максимальное кол-во за ход: "))
    while n > m:
        a = n % (m + 1)
        if a == 0:
            a += 1
        n -= a
        print("Я взял ", a, " конфет(ы/у)")
        print("осталось ", n, " конфет(ы/у), Ваш ход")
        a = int(input("Какое количество вы возьмете? "))
        while (a < 1) or (a > m):
            a = int(input("Вы ввели недопустимое значение, попробуйте еще раз: "))
        n -= a
        print("Вы взяли: ", a, " конфет(ы/у)")
        print("осталось ", n, " конфет(ы/у)")
    if n == m + 1:
        a = m
        print("Я забираю", a, "конфет(ы/у), вам остается 1, Вы выиграли")
    elif n == 0:
        print("Вы забрали последние конфеты, Вы выиграли!")
    else:
        print("Я забираю последние ", n, " конфет(ы/у), Вы проиграли!")
game()
f = input('ещё раз?\n')
if f == 'да':
    game()
else:
    print('пока\n')