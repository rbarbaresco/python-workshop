# -*- coding: utf-8 -*-
import unittest
from workshop import strings


class StringsTest(unittest.TestCase):

    def test_should_return_the_amount_of_vowels_in_a_string(self):
        string = "2 vowels"
        self.assertEqual(2, strings.vowels(string))

    def test_should_return_the_amount_of_words_in_a_string(self):
        string = "It should be six words... right?"
        self.assertEqual(5, strings.words(string))

    def test_should_count_how_many_occurences_of_a_string(self):
        string = "Distribuído com marcação de audiência 26/01/2011 / 8:40 - Una"
        self.assertEqual(1, strings.count(string, "Audiência"))

    def test_should_return_the_list_of_infinitive_verbs_in_a_string(self):
        string = "Para participar do workshop de python, basta querer aprender e ter um computador com o python instalado. Com isso, nada poderá interferir no seu aprendizado."
        expected_list = ["participar", "querer", "aprender", "ter", "interferir"]
        self.assertEqual(expected_list, strings.infinitive_verbs(string))

    def test_should_return_the_amount_of_each_character_in_a_string(self):
        string = "Para participar do workshop de python, basta querer aprender e ter um computador com o python instalado. Com isso, nada poderá interferir no seu aprendizado."
        expected_dict = {',': 2, '.': 2, 'C': 1, 'P': 1, 'a': 14, 'b': 1, 'c': 3, 'd': 9, 'e': 12, 'f': 1, 'h': 3, 'i': 7, 'k': 1,
                         'l': 1, 'm': 4, 'n': 8, 'o': 15, 'p': 9, 'q': 1, 'r': 15, 's': 6, 't': 8, 'u': 4, 'w': 1, 'y': 2, 'z': 1, 'á': 1}
        self.assertEqual(expected_dict, strings.character_count(string))