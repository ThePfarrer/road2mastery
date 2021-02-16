# 4. Write a program that performs factorization using the general formula
# (so called all mighty formula)

import math


def almight_formula(a, b, c):
    # Almight formula -> x = (-b +/- sqrt(b**2 - 4*a*c) / 2 * a

    denom1 = -b + math.sqrt(b ** 2 - 4 * a * c)
    denom2 = -b - math.sqrt(b ** 2 - 4 * a * c)
    numem = 2 * a

    print(denom1 / numem, denom2 / numem)


a, b, c = [int(i) for i in input('Enter values for a, b and c: ').split()]

almight_formula(a, b, c)
