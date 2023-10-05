import unittest
from CalculatriceCrypto import CalculatriceCrypto as crypto

class FibonnaciTest(unittest.TestCase):
    
    def test_est_dans_fibo(self):
        self.assertTrue(crypto.est_dans_fibonacci(2))
        self.assertFalse(crypto.est_dans_fibonacci(4))
    
    def test_est_dans_fibo_moyen(self):
        self.assertTrue(crypto.est_dans_fibonacci(317_811))
        self.assertFalse(crypto.est_dans_fibonacci(417_811))

    def test_est_dans_fibo_large(self):
        self.assertTrue(crypto.est_dans_fibonacci(701_408_733))
        self.assertFalse(crypto.est_dans_fibonacci(701_408_734))

    def test_est_dans_fibo_position(self):
        self.assertEqual(3, crypto.position_fibonacci(2))
    
    def test_est_dans_fibo_moyen_position(self):
        self.assertEqual(28, crypto.position_fibonacci(317_811))
    
    def test_est_dans_fibo_large_position(self):
        self.assertEqual(44,crypto.position_fibonacci(701_408_733))
