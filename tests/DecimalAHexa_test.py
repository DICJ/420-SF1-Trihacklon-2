import unittest
from CalculatriceCrypto import CalculatriceCrypto as crypto

class decimal_a_hexa_(unittest.TestCase):    
    
    def test_decimal_a_hexa_29(self):
        self.assertEqual("1D", crypto.decimal_a_hexa(29).strip())
        self.assertEqual("CE", crypto.decimal_a_hexa(206).strip())

    def test_decimal_a_hexa_big(self):
        big = crypto.decimal_a_hexa(198_524_689).strip()
        self.assertTrue(
            big == "BD53F11" or
            big == "B D5 3F 11" or
            big == "0B D5 3F 11")

    def test_decimal_a_hexa_ones(self):
        ones = crypto.decimal_a_hexa(65_535).strip()
        self.assertTrue(
            ones == "FFFF" or
            ones == "FF FF")

    def test_decimal_a_hexa_big_separateur(self):
        big = crypto.decimal_a_hexa(198_524_689).strip()
        self.assertTrue(
            big == "B D5 3F 11" or
            big == "0B D5 3F 11")

    def test_decimal_a_hexa_ones_separateur(self):
        ones = crypto.decimal_a_hexa(65_535).strip()
        self.assertEqual("FF FF", ones)

    def test_decimal_a_hexa_big_leading_0s(self):
        big = crypto.decimal_a_hexa(198_524_689).strip()
        self.assertEqual("0B D5 3F 11", big)
