# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:

duration = int(input("Введите количество секунд, котоорые вы хотите преобразовать: "))
duration1 = duration // 60
duration2 = duration // 60 // 60
duration3 = duration // 24 // 60 // 60

while duration > 60:
    duration -= 60

while duration1 > 60:
    duration1 -= 60

while duration2 > 60:
    duration2 -= 60

print("Сутки: ", duration3, "Часы:", + duration2, "Минуты: ", duration1, "Секунды: ", duration)


# 2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:

def sum_digits(value):
    res = 0

    while value != 0:
        res += value % 10
        value //= 10

    return res


arr = [i**3 for i in range(1, 1001, 2)]

res1 = sum(filter(lambda num: sum_digits(num) % 7 == 0, arr))
res2 = sum(filter(lambda num: sum_digits(num + 17) % 7 == 0, arr))

print(res1)
print(res2)

# 3. Реализовать склонение...

# per = int(input("Введите число от 1 до 20: "))

for per in range(21):
    if per % 10 == 1 and per % 100 != 11:
        print(per, "процент")
    elif 1 < per % 10 < 5 and not 11 < per % 100 < 15:
        print(per, "процента")
    else:
        print(per, "процентов")

