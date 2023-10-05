import unittest
from CalculatriceCrypto import CalculatriceCrypto as crypto

class DecimalABinaire(unittest.TestCase):

    def test_decimal_a_binaire_29(self):
        vingtNeuf = crypto.decimal_a_binaire(29).strip()
        print("29 = " + vingtNeuf)
        self.assertTrue(
            vingtNeuf == "11101" or 
            vingtNeuf == "1 1101" or 
            vingtNeuf == "0001 1101")    

    def test_decimal_a_binaire_big(self):
        big = crypto.decimal_a_binaire(198_524_689).strip()
        self.assertTrue(
            big == "1011 1101 0101 0011 1111 0001 0001" or
            big == "1011110101010011111100010001")

    def test_decimal_a_binaire_ones(self):
        ones = crypto.decimal_a_binaire(65_535).strip()
        self.assertTrue(
            ones == "1111 1111 1111 1111" or
            ones == "1111111111111111")    

    def test_decimal_a_binaire_29_separateur(self):
        vingtNeuf = crypto.decimal_a_binaire(29).strip()
        self.assertTrue(
            vingtNeuf == "1 1101" or
            vingtNeuf == "0001 1101")

    def test_decimal_a_binaire_big_separateur(self):
        big = crypto.decimal_a_binaire(198_524_689).strip()
        self.assertEqual("1011 1101 0101 0011 1111 0001 0001", big)
        ones = crypto.decimal_a_binaire(65_535).strip()
        self.assertEqual("1111 1111 1111 1111", ones)

    def test_decimal_a_binaire_29_leading_0s(self):
        vingtNeuf = crypto.decimal_a_binaire(29).strip()
        self.assertEqual("0001 1101", vingtNeuf)

if __name__ == '__main__':
    unittest.main()