from random import randint

num = randint(0, 1000)
tries = 10
for i in range(tries+1):
    if i == tries:
        print("Попыток больше нет")
        break
    x = int(input("Введите число "))
    if x == num:
        print("Верно")
        break
    if x < num:
        print("Нужное число больше")
    if x > num:
        print("Нужное число меньше")
