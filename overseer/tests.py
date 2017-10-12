# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Avaliation

# Create your tests here.
class AvaliationModelTests(TestCase):
    def test_processed_file_result_control_01(self):
        with open('./overseer/tests/test01.txt', "r") as file_content:
            avaliation = Avaliation(upload=file_content)
            self.assertEqual(avaliation.process(), '4123-1233-1223-3422 [Valid] \n')

    def test_processed_file_result_control_02(self):
        with open('./overseer/tests/test02.txt', "r") as file_content:
            avaliation = Avaliation(upload=file_content)
            self.assertEqual(avaliation.process(), '4123123312233422 [Valid] \n')

    def test_processed_file_result_with_no_digit_character(self):
        with open('./overseer/tests/test03.txt', "r") as file_content:
            avaliation = Avaliation(upload=file_content)
            self.assertEqual(avaliation.process(), '4123123312233a22 [Invalid] \n')

    def test_processed_file_result_with_invalid_separation(self):
        with open('./overseer/tests/test04.txt', "r") as file_content:
            avaliation = Avaliation(upload=file_content)
            self.assertEqual(avaliation.process(), '4123_1233-1223-3422 [Invalid] \n')

    def test_processed_file_result_with_identical_sequencial_digits_01(self):
        with open('./overseer/tests/test05.txt', "r") as file_content:
            avaliation = Avaliation(upload=file_content)
            self.assertEqual(avaliation.process(), '4123123333233422 [Invalid] \n')

    def test_processed_file_result_with_identical_sequencial_digits_02(self):
        with open('./overseer/tests/test06.txt', "r") as file_content:
            avaliation = Avaliation(upload=file_content)
            self.assertEqual(avaliation.process(), '4123-1233-3323-3422 [Invalid] \n')

    def test_processed_file_result_with_starter_digit_invalid(self):
        with open('./overseer/tests/test08.txt', "r") as file_content:
            avaliation = Avaliation(upload=file_content)
            self.assertEqual(avaliation.process(), '1123-1233-3323-3422 [Invalid] \n')

    def test_processed_file_result_with_divergent_N_value(self):
        with open('./overseer/tests/test09.txt', "r") as file_content:
            avaliation = Avaliation(upload=file_content)
            self.assertEqual(avaliation.process(), 'The N (first line) value diverges from the card numbers found')

    def test_processed_file_result_with_N_greater_than_99(self):
        with open('./overseer/tests/test10.txt', "r") as file_content:
            avaliation = Avaliation(upload=file_content)
            self.assertEqual(avaliation.process(), 'N can\'t be greater than 100')
