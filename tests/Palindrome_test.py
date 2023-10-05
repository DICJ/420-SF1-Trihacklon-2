import unittest
from CalculatriceCrypto import CalculatriceCrypto as crypto

class PalindromeTest(unittest.TestCase):
    def test_est_palindrome_pair(self):
        self.assertTrue(crypto.est_palindrome(22))
        self.assertFalse(crypto.est_palindrome(54))
    
    def test_est_palindrome_gros_pair(self):
        self.assertTrue(crypto.est_palindrome(1_234_554_321))
        self.assertFalse(crypto.est_palindrome(1_234_564_321))
    
    def test_est_palindrome_impair(self):
        self.assertTrue(crypto.est_palindrome(2))
        self.assertFalse(crypto.est_palindrome(367))
        self.assertTrue(crypto.est_palindrome(363))
    
    def test_est_palindrome_impair_gros(self):
        self.assertTrue(crypto.est_palindrome(123_454_321))
        self.assertFalse(crypto.est_palindrome(123_454_361))
    
    def test_est_tout_pareil(self):
        self.assertTrue(crypto.est_tout_pareil(2))
        self.assertFalse(crypto.est_tout_pareil(202))
    
    def test_est_tout_pareil_gros(self):    
        self.assertTrue(crypto.est_tout_pareil(1111111111))
        self.assertTrue(crypto.est_tout_pareil(222222))
        self.assertFalse(crypto.est_tout_pareil(1111111119))
    