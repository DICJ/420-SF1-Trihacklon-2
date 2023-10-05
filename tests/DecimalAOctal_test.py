import unittest
from CalculatriceCrypto import CalculatriceCrypto as crypto

class decimal_a_octal_(unittest.TestCase):      

    def test_decimal_a_octal_29(self):
        vingtNeuf = crypto.decimal_a_octal(29).strip()
        self.assertTrue(
            vingtNeuf == "35" or
            vingtNeuf == "035")   

    def test_decimal_a_octal_big(self):
        big = crypto.decimal_a_octal(19_852_489).strip()
        self.assertTrue(
            big == "113566311" or
            big == "113 566 311")
    
    def test_decimal_a_octal_ones(self):
        ones = crypto.decimal_a_octal(65_535).strip()
        self.assertTrue(
            ones == "177777" or
            ones == "177 777")    
    
    def test_decimal_a_octal_big_separateur(self):
        big = crypto.decimal_a_octal(19_852_489).strip()
        self.assertEqual("113 566 311", big)
    
    def test_decimal_a_octal_ones_separateur(self):
        ones = crypto.decimal_a_octal(65_535).strip()
        self.assertEqual("177 777", ones)
   
    def test_decimal_a_octal_29_leading_0s(self):
        vingtNeuf = crypto.decimal_a_octal(29).strip()
        self.assertEqual("035", vingtNeuf)
    
