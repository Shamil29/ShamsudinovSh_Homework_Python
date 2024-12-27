from math import ceil


def square(a):
    return ceil(a*a)


side = float(input("Введите сторону квадрата: "))
print(f"Площадь квадрата: {square(side)}")
