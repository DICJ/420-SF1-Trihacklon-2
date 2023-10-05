import unittest
from CalculatriceCrypto import CalculatriceCrypto as crypto

class PremierTest(unittest.TestCase): 
    def test_est_premier_simple(self):
        self.assertTrue(crypto.est_premier(23))
        self.assertFalse(crypto.est_premier(12))
    
    def test_est_premier_limite(self):
        self.assertFalse(crypto.est_premier(1))
        self.assertTrue(crypto.est_premier(2))
    
    def test_est_premier_gros(self):
        self.assertTrue(crypto.est_premier(278_786_533))
        self.assertFalse(crypto.est_premier(27_109 * 15_199))
        
    def test_est_premier_moyen(self):
        self.assertTrue(crypto.est_premier(781_967_633))
        self.assertFalse(crypto.est_premier(2_579_609))
    
    def test_est_premier_gros_encore(self):
        self.assertTrue(crypto.est_premier(336_954_173))
        self.assertFalse(crypto.est_premier(9_643 * 18_353))
    
    def test_est_premier_sophie_germain(self):
        self.assertTrue(crypto.est_premier_sophie_germain(82_223))
        self.assertFalse(crypto.est_premier_sophie_germain(4_837_492))
        self.assertFalse(crypto.est_premier_sophie_germain(689_141))
    
    def test_est_premier_sophie_germain_petit(self):    
        self.assertTrue(crypto.est_premier_sophie_germain(5))
        self.assertFalse(crypto.est_premier_sophie_germain(7))
        self.assertTrue(crypto.est_premier_sophie_germain(11))
    
    def test_est_premier_sur(self):
        self.assertTrue(crypto.est_premier_sur(164_447))
        self.assertFalse(crypto.est_premier_sur(689_141))
    
    def test_est_premier_sur_petit(self):
        self.assertTrue(crypto.est_premier_sur(5))
        self.assertFalse(crypto.est_premier_sur(29))
        self.assertTrue(crypto.est_premier_sur(7))
    
    def test_est_premier_jumeau(self):    
        self.assertFalse(crypto.est_jumeau(23))
        self.assertFalse(crypto.est_jumeau(12))
        self.assertTrue(crypto.est_jumeau(29))
        self.assertTrue(crypto.est_jumeau(31))
    
    def test_est_premier_jumeau_large(self):
        self.assertTrue(crypto.est_jumeau(557_519))
        self.assertTrue(crypto.est_jumeau(557_521))
        self.assertTrue(crypto.est_jumeau(27_941)) 
        self.assertFalse(crypto.est_jumeau(28_069))
