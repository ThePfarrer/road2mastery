# 1. Write a program to calculate the areas of a circle, a triangle, a parallelogram

# 2. From question 1, create functions for each formula...

# 3. Update the program to accept user input for all variables that are not constant.

import math


def area_circle(radius):
    # Area = pi * radius^2
    area = math.pi * radius ** 2
    return round(area, 2)


def area_triangle(base, height):
    # Area = (base * height) / 2
    area = (base * height) / 2
    return round(area, 2)


def area_parallelogram(base, height):
    #  Area = base * height
    area = base * height
    return area
    # OR 2 * area of triangle
    # return 2 * area_triangle(base, height)


circle_rad = int(input('Please enter a given circle radius: '))

print(f'The area of a circle with radius {circle_rad} is {area_circle(circle_rad)}')

base = int(input('Please enter a given triangle or parallelogram base: '))
height = int(input('Please enter a given triangle or parallelogram height: '))

print(f'The area of a triangle with base {base} and height {height} is {area_triangle(base, height)}')
print(f'The area of a parallelogram with base {base} and height {height} is {area_parallelogram(base, height)}')
# print(area_triangle(3, 3))
# print(area_parallelogram(3, 3))
