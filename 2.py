while True:
    try:
        n = int(input("Введите число от 1 до 10000 "))
    except ValueError:
        print("Введите число")
        if a < 0 or a > 100000:
            print("Недопустимое число")
        else:
            break
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
    if count == 0:
        print("Число простое")
    else:
        print("Число составное")
else:
