#Проверка числа
<<<<<<< HEAD
while True:
    print()
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

        # Проверка на полный квадрат
        Root = int(Number ** 0.5)
        if Number >= 0 and (Root * Root == Number):
            print("Полный квадрат: да")
        else:
            print("Полный квадрат: нет")

        # Повтор анализа для нового числа
    Again = input("\nПроверить ещё одно число? (да/нет): ").strip().lower()
    if Again != "да":
        print("Работа программы завершена.")
        break
=======
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
>>>>>>> 0e98f037f0bf9061a5de78833c811c2ae3932c1d
