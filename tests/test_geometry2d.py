# -*- coding: utf-8 -*-
import unittest
from workshop import geometry2d


class Geometry2dTest(unittest.TestCase):

    def test_should_calc_the_area_of_a_square(self):
        self.assertEquals(1, geometry2d.area_square(1))
        self.assertEquals(4, geometry2d.area_square(2))
        self.assertEquals(9, geometry2d.area_square(3))
        self.assertEquals(6.25, geometry2d.area_square(2.5))
        self.assertAlmostEqual(11.11, geometry2d.area_square(3.333), 2)

    def test_should_calc_the_area_of_a_rectacgle(self):
        self.assertEquals(2, geometry2d.area_rect(1, 2))
        self.assertEquals(6, geometry2d.area_rect(2, 3))
        self.assertEquals(12, geometry2d.area_rect(3, 4))
        self.assertEquals(5, geometry2d.area_rect(2.5, 2))
        self.assertAlmostEqual(9.265, geometry2d.area_rect(3.333, 2.78), 2)

    def test_should_calc_the_area_of_a_triangle(self):
        self.assertEquals(1, geometry2d.area_triangle(1, 2))
        self.assertEquals(3, geometry2d.area_triangle(2, 3))
        self.assertEquals(6, geometry2d.area_triangle(3, 4))
        self.assertEquals(8.75, geometry2d.area_triangle(2.5, 7))
        self.assertAlmostEqual(16.631, geometry2d.area_triangle(3.333, 9.98), 2)

    def test_should_calc_the_area_of_a_circle(self):
        self.assertEquals(3.14, geometry2d.area_circle(1))
        self.assertEquals(12.56, geometry2d.area_circle(2))
        self.assertEquals(28.26, geometry2d.area_circle(3))
        self.assertEquals(19.625, geometry2d.area_circle(2.5))
        self.assertAlmostEqual(34.881, geometry2d.area_circle(3.333), 2)

    def test_should_calc_the_perimeter_of_a_square(self):
        self.assertEquals(4, geometry2d.perimeter_square(1))
        self.assertEquals(8, geometry2d.perimeter_square(2))
        self.assertEquals(12, geometry2d.perimeter_square(3))
        self.assertEquals(10, geometry2d.perimeter_square(2.5))
        self.assertAlmostEqual(13.332, geometry2d.perimeter_square(3.333), 2)

    def test_should_calc_the_perimeter_of_a_rectacgle(self):
        self.assertEquals(6, geometry2d.perimeter_rect(1, 2))
        self.assertEquals(10, geometry2d.perimeter_rect(2, 3))
        self.assertEquals(14, geometry2d.perimeter_rect(3, 4))
        self.assertEquals(9, geometry2d.perimeter_rect(2.5, 2))
        self.assertAlmostEqual(12.226, geometry2d.perimeter_rect(3.333, 2.78), 2)

    def test_should_calc_the_perimeter_of_a_triangle(self):
        self.assertEquals(6, geometry2d.perimeter_triangle(1, 2, 3))
        self.assertEquals(9, geometry2d.perimeter_triangle(2, 3, 4))
        self.assertEquals(12, geometry2d.perimeter_triangle(3, 4, 5))
        self.assertEquals(19.5, geometry2d.perimeter_triangle(2.5, 7, 10))
        self.assertAlmostEqual(14.873, geometry2d.perimeter_triangle(3.333, 9.98, 1.56), 2)

    def test_should_calc_the_perimeter_of_a_straight_triangle(self):
        self.assertAlmostEqual(12, geometry2d.perimeter_straight_triangle(3, 4), 2)
        self.assertAlmostEqual(6.828, geometry2d.perimeter_straight_triangle(2, 2), 2)
        self.assertAlmostEqual(34.142, geometry2d.perimeter_straight_triangle(10, 10), 2)
        self.assertAlmostEqual(16.933, geometry2d.perimeter_straight_triangle(2.5, 7), 2)
        self.assertAlmostEqual(23.834, geometry2d.perimeter_straight_triangle(3.333, 9.98), 2)

    def test_should_calc_the_perimeter_of_a_eq_triangle(self):
        self.assertAlmostEqual(9, geometry2d.perimeter_eq_triangle(3), 2)
        self.assertAlmostEqual(6, geometry2d.perimeter_eq_triangle(2), 2)
        self.assertAlmostEqual(30, geometry2d.perimeter_eq_triangle(10), 2)
        self.assertAlmostEqual(7.5, geometry2d.perimeter_eq_triangle(2.5), 2)
        self.assertAlmostEqual(9.999, geometry2d.perimeter_eq_triangle(3.333), 2)

    def test_should_calc_the_perimeter_of_a_circle(self):
        self.assertEquals(6.28, geometry2d.perimeter_circle(1))
        self.assertEquals(12.56, geometry2d.perimeter_circle(2))
        self.assertEquals(18.84, geometry2d.perimeter_circle(3))
        self.assertEquals(16.014, geometry2d.perimeter_circle(2.55))
        self.assertAlmostEqual(20.931, geometry2d.perimeter_circle(3.333), 2)
