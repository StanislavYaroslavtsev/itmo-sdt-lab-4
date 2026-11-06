import unittest

from square import area, perimeter


class SquareAreaTestCase(unittest.TestCase):
    def test_zero_side(self):
        self.assertEqual(area(0), 0)

    def test_unit_side(self):
        self.assertEqual(area(1), 1)

    def test_integer_side(self):
        self.assertEqual(area(4), 16)

    def test_float_side(self):
        self.assertAlmostEqual(area(2.5), 6.25)

    def test_large_side(self):
        self.assertEqual(area(1e6), 1e12)

    def test_negative_side_raises(self):
        with self.assertRaises(ValueError):
            area(-2)

    def test_string_side_raises(self):
        with self.assertRaises(TypeError):
            area("2")


class SquarePerimeterTestCase(unittest.TestCase):
    def test_zero_side(self):
        self.assertEqual(perimeter(0), 0)

    def test_unit_side(self):
        self.assertEqual(perimeter(1), 4)

    def test_integer_side(self):
        self.assertEqual(perimeter(4), 16)

    def test_float_side(self):
        self.assertAlmostEqual(perimeter(2.5), 10.0)

    def test_negative_side_raises(self):
        with self.assertRaises(ValueError):
            perimeter(-2)

    def test_string_side_raises(self):
        with self.assertRaises(TypeError):
            perimeter("2")