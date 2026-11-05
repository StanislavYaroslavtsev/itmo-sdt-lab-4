import math
import unittest

from circle import area, perimeter


class CircleAreaTestCase(unittest.TestCase):
    def test_zero_radius(self):
        self.assertEqual(area(0), 0)

    def test_unit_radius(self):
        self.assertAlmostEqual(area(1), math.pi)

    def test_integer_radius(self):
        self.assertAlmostEqual(area(4), 16 * math.pi)

    def test_float_radius(self):
        self.assertAlmostEqual(area(2.5), 6.25 * math.pi)


class CirclePerimeterTestCase(unittest.TestCase):
    def test_zero_radius(self):
        self.assertEqual(perimeter(0), 0)

    def test_unit_radius(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)

    def test_integer_radius(self):
        self.assertAlmostEqual(perimeter(4), 8 * math.pi)

    def test_float_radius(self):
        self.assertAlmostEqual(perimeter(2.5), 5 * math.pi)