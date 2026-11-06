import unittest

from triangle import area, perimeter


class TriangleAreaTestCase(unittest.TestCase):
    def test_zero_side(self):
        self.assertEqual(area(0, 5), 0)

    def test_zero_height(self):
        self.assertEqual(area(5, 0), 0)

    def test_integer_values(self):
        self.assertEqual(area(4, 2), 4)

    def test_float_result(self):
        self.assertAlmostEqual(area(3, 5), 7.5)

    def test_float_values(self):
        self.assertAlmostEqual(area(2.5, 4), 5.0)

    def test_negative_side_raises(self):
        with self.assertRaises(ValueError):
            area(-2, 4)

    def test_string_side_raises(self):
        with self.assertRaises(TypeError):
            area("4", 2)


class TrianglePerimeterTestCase(unittest.TestCase):
    def test_integer_sides(self):
        self.assertEqual(perimeter(4, 2, 3), 9)

    def test_equilateral(self):
        self.assertEqual(perimeter(5, 5, 5), 15)

    def test_float_sides(self):
        self.assertAlmostEqual(perimeter(1.5, 2.5, 3.5), 7.5)

    def test_order_independent(self):
        self.assertEqual(perimeter(3, 4, 5), perimeter(5, 3, 4))

    def test_zero_side_raises(self):
        with self.assertRaises(ValueError):
            perimeter(0, 4, 5)

    def test_inequal_triangle_raises(self):
        with self.assertRaises(ValueError):
            perimeter(1, 2, 10)

    def test_string_sides_raises(self):
        with self.assertRaises(TypeError):
            perimeter("3", "4", "5")