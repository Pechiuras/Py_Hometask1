# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
n = int(input('Введите число: '))
d1 = n // 100
d2 = (n % 100) // 10
d3 = n % 10
print(d1 + d2 + d3)