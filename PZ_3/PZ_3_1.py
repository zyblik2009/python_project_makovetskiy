#Проверить истинность высказывания: "Среди трех данных целых чисел есть хотя бы одна пара совпадающих'
while True:
    a = input("Введите первое число: ")
    try:
        a = int(a)
        break
    except ValueError:
        print("Число неккоректное")
while True:
    b = input("Введите второе число: ")
    try:
        b = int(b)
        break
    except ValueError:
        print("Число неккоректное")
while True:
    c = input("Введите третье число: ")
    try:
        c = int(c)
        break
    except ValueError:
        print("Число неккоректное")
if a == b or b == c or c == a:
    print("Среди чисел есть пара")
else:
    print("Пар нет")