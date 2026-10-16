#Проверка числа
try:
    Number = int(input("Введите число: "))
except ValueError:
    print("Ошибка: введено не целое число")
else:
    print(f"Ваше число: {Number}")

    #Знак числа
    if Number > 0:
        print("Положительное: да")
    elif Number < 0:
        print("Положительное: нет (отрицательное)")
    else:
        print("Положительное: нет (ноль)")

    #Чётность
    if Number % 2 == 0:
        print("Четное: да")
    else:
        print("Четное: нет")

    #Делимость на 3
    if Number % 3 == 0:
        print("Делится на 3: да")
    else:
        print("Делится на 3: нет")

    #Делимость на 5
    if Number % 5 == 0:
        print("Делится на 5: да")
    else:
        print("Делится на 5: нет")

    #Проверка на простое число
    IsSimple = Number > 1
    for i in range(2, int(Number ** 0.5) + 1):
        if Number % i == 0:
            IsSimple = False
            break
    if IsSimple:
        print("Простое: да")
    else:
        print("Простое: нет")

    #Количество цифр
    DigitsCount = len(str(abs(Number)))
    print(f"Количество цифр: {DigitsCount}")