"""Module for testing"""

import unittest
from typing import Any
from mindbox_squares import triangle_is_valid
from mindbox_squares import compute_circle_area_from_radius
from mindbox_squares import type_of_triangle

class TestTriangle(unittest.TestCase):
    """Testing Traingle"""
    def test_negative_triangle(self: Any) -> None:
        """Testing if a triangle has any negative side."""
        self.assertFalse(triangle_is_valid(1, 2, -1))

    def test_wrong_sides_triangle(self: Any) -> None:
        """Testing if a triangle has any wrong side."""
        self.assertFalse(triangle_is_valid(1, 2, 4))

    def test_correct_triangle(self: Any) -> None:
        """Testing if a triangle has all correct sides."""
        self.assertTrue(triangle_is_valid(1, 1, 1))
        #self.assertTrue(triangle_is_valid(1, 2, 2.9))


class TestCircle(unittest.TestCase):
    """Testing the circle area"""
    def test_correct_circle_area(self):
        """Testing with the correct value"""
        self.assertEqual(compute_circle_area_from_radius(3), 28.2743)

    def test_on_zero_radius(self):
        """Testing with the zero radius"""
        with self.assertRaises(ValueError):
            compute_circle_area_from_radius(0)

    def test_on_negative_radius(self):
        """Testing with the negative radius"""
        with self.assertRaises(ValueError):
            compute_circle_area_from_radius(-1)


class TestTriangleType(unittest.TestCase):
    """Testing the triangle type"""
    def test_versatile_triangle(self):
        """Testing with the versatile triangle"""
        self.assertEqual(type_of_triangle(2, 1, 2.9), "versatile")

    def test_equiliteral_triangle(self):
        """Testing with the equilateral triangle"""
        self.assertEqual(type_of_triangle(2, 2, 2), "equilateral")

    def test_isosceles_triangle(self):
        """Testing with the isosceles triangle"""
        self.assertEqual(type_of_triangle(2, 1, 2), "isosceles")


if __name__ == "__main__":
    unittest.main()
