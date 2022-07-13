# 1 - Напишите программу, которая принимает на вход вещественное 
# число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11



num = input("Введите число: ")

def fun_sum(a):
    sum = 0

    for i in str(a):
        if i == "," or i == ".":
            continue
        sum += int(i)
    return sum



print(fun_sum(num))


