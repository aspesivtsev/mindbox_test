#!/usr/bin/python3

from math import pi, sqrt
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def triangle_is_valid(a:float, b:float, c:float) -> bool:
    """Check if form of the triangle is correct (sum of min values is less than max value) and all values are positive"""
    triangle_values = [a, b, c]
    triangle_values.sort()
    return bool((sum(triangle_values[:2]) >= triangle_values[2]) and (a and b and c > 0))


def compute_circle_area_from_radius(radius:float) -> float:
    """Calculating the area of the circle by its radius rounded to .4 digits"""
    if radius > 0:
        return round(pi * radius ** 2, 4)
    logger.error('Value is not correct! Please check it.')
    raise ValueError('Value is not correct! Please check it.')


def compute_triangle_area_by_sides(a:float, b:float, c:float) -> float:
    """Calculating the area of the triangle by its sides rounded to .4 digits"""
    if triangle_is_valid(a, b, c):
        p = (a + b + c) / 2
        result = round(sqrt(p * (p-a) * (p-b) * (p-c)), 4)
        return result
    logger.error('Not all values are correct! Please check it.')
    raise ValueError('Not all values are correct! Please check it.')


def type_of_triangle(a:float, b:float, c:float) -> str:
    """Get the type of the triangle"""
    if a == b == c:
        # равносторонний
        return "equilateral"
    if a == b or b == c or a == c:
        #равнобедренный
        return "isosceles"
    # разносторонний
    return "versatile"


if __name__=="__main__":
    print(f'Area of the circle is {compute_circle_area_from_radius(3)}.')
    print(f'Area of the circle is {compute_circle_area_from_radius(15)}.')

    print(compute_triangle_area_by_sides(2,1,2))
    print(compute_triangle_area_by_sides(2, 1, 2.9))

    print(f'This is a {type_of_triangle(2, 1, 2.9)} triangle.')
    print(f'This is a {type_of_triangle(2, 2, 2)} triangle.')