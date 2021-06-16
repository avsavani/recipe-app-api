from django.test import TestCase
from .calc import add2, sub
class ClacTest(TestCase):
    def test_calc_add(self):
        self.assertEqual(add2(3,3),6)

    def test_sub_clac(self):
        self.assertEqual(sub(3,3),0)
