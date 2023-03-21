import unittest
from config import TTime

import unittest
from yandex_testing_lesson import reverse

a = TTime('1:2')
b = TTime(1, 5)


class TestReverse(unittest.TestCase):
    def test_init_0(self):
        TTime('1:2')

    def test_init_1(self):
        TTime(1, 5)

    def test_init_2(self):
        with self.assertRaises(Exception):
            TTime(1)

    def test_add_T(self):
        self.assertEqual((a + b).__repr__(), TTime(2, 7).__repr__())

    def test_sub_T(self):
        self.assertEqual((a - b).__repr__(), TTime(23, 57).__repr__())

    def test_add_int(self):
        self.assertEqual((a + 24 * 60).__repr__(), TTime(1, 2).__repr__())

    def test_sub_int(self):
        self.assertEqual((a - 24 * 60).__repr__(), TTime(1, 2).__repr__())
