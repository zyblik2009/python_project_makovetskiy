while True:
    a = input("Введите трехзначное число: ")
    try:
        a = int(a)
    except ValueError:
        print("Введите корректное число")
    if a <= 100 or a >= 999:
        print("Число не трехзначное")
    else:
        break
b = a % 10
c = a // 10
print(b * 100 + c)