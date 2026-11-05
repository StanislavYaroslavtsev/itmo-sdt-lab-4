import unittest

from rectangle import area, perimeter


class RectangleAreaTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(area(10, 0), 0)

    def test_both_zero(self):
        self.assertEqual(area(0, 0), 0)

    def test_square_mul(self):
        self.assertEqual(area(10, 10), 100)

    def test_integer_sides(self):
        self.assertEqual(area(3, 4), 12)

    def test_float_sides(self):
        self.assertAlmostEqual(area(1.5, 6.2), 9.3)

    def test_commutative(self):
        self.assertEqual(area(3, 7), area(7, 3))


class RectanglePerimeterTestCase(unittest.TestCase):
    def test_both_zero(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_one_zero(self):
        self.assertEqual(perimeter(5, 0), 10)

    def test_integer_sides(self):
        self.assertEqual(perimeter(4, 2), 12)

    def test_square_case(self):
        self.assertEqual(perimeter(10, 10), 40)

    def test_float_sides(self):
        self.assertAlmostEqual(perimeter(1.5, 6.2), 15.4)

    def test_commutative(self):
        self.assertEqual(perimeter(3, 7), perimeter(7, 3))