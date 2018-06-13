# -*- coding: utf-8 -*-
import unittest
from workshop import arrays


class ArraysTest(unittest.TestCase):

    def test_should_return_the_first_element_of_an_array(self):
        array = [5, 4, 3, 1]
        self.assertEqual(5, arrays.first(array))

    def test_should_return_the_last_element_of_an_array(self):
        array = [5, 4, 3, 1]
        self.assertEqual(1, arrays.last(array))

    def test_should_return_the_middle_element_of_an_array_even(self):
        array = [5, 4, 3, 1]
        self.assertEqual(3, arrays.middle(array))

    def test_should_return_the_middle_element_of_an_array_odd(self):
        array = [5, 4, 3, 1, 2]
        self.assertEqual(3, arrays.middle(array))

    def test_should_count_how_many_occurences_of_a_element(self):
        array = [5, 4, 3, 1, 2, 2]
        self.assertEqual(2, arrays.count(array, 2))
