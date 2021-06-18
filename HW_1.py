# Задание 1
#Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

from math import factorial

def combinations(n1, n2, k):
    return int(factorial(n1) / (factorial(k) * factorial(n1 - k))) / \
           int(factorial(n2) / (factorial(k) * factorial(n2 - k)))
print(combinations(13, 52, 4))

def combinatins2(n1, n2, k):
    return 1 - (int(factorial(n1) / (factorial(k) * factorial(n1 - k))) / \
           int(factorial(n2) / (factorial(k) * factorial(n2 - k))))
print(combinatins2(48, 52, 4))

# Задание 2
# На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами
# от 0 до 9. Код содержит три цифры, которые нужно нажать одновременно. Какова вероятность
# того, что человек, не знающий код, откроет дверь с первой попытки?

def combinations(n, k):
    return 1 / int(factorial(n) / (factorial(k) * factorial(n - k)))

print (combinations(10, 3))

# Задание 3
# В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным
# образом извлекает 3 детали. Какова вероятность того, что все извлеченные детали окрашены?

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

n = combinations(15, 3)

def combinations2(n, k):

    return int(factorial(n) / (factorial(k) * factorial(n - k)))

m = combinations2(9, 4)

P = m/n
print(P)

# Задание 4
# В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того,
# что 2 приобретенных билета окажутся выигрышными?
# n - количество выйгрышных билетов, к - количество билетов, m - количество купленных билетов

def combinations(n, m, k):
    M = int(factorial(n)/(factorial(m) * factorial(n-m)))
    N = int(factorial(k)/(factorial(n) * factorial(k-n)))
    return M/N

print(combinations(2, 2, 100))





