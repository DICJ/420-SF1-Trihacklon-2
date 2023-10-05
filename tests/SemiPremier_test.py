import unittest
from CalculatriceCrypto import CalculatriceCrypto as crypto

class SemiPremierTest(unittest.TestCase): 
    def test_est_semi_premier_simple(self):
        self.assertTrue(crypto.est_semi_premier(22))
        self.assertFalse(crypto.est_semi_premier(12))
    
    def test_est_semi_premier_simple_encore(self):
        self.assertFalse(crypto.est_semi_premier(23))
        self.assertFalse(crypto.est_semi_premier(29 * 23 * 11))
        self.assertTrue(crypto.est_semi_premier(29 * 23))
    
    def test_est_semi_premier_limite(self):
        self.assertFalse(crypto.est_semi_premier(1))
        self.assertFalse(crypto.est_semi_premier(2))
        self.assertFalse(crypto.est_semi_premier(3))
        self.assertTrue(crypto.est_semi_premier(4))
    
    def test_est_semi_premier_simple_large(self):
        self.assertTrue(crypto.est_semi_premier(29_077 * 15_161))
        self.assertFalse(crypto.est_semi_premier(3_533 * 691 * 607))
    
    def test_est_semi_premier_Simple_encore_large(self):
        self.assertFalse(crypto.est_semi_premier(1_362_941_563))
        self.assertTrue(crypto.est_semi_premier(8_069 * 26_119))
    
    def test_est_semi_premier_outputs(self):
        reponses = crypto.facteurs_semi_premier(22)
        self.assertTrue(reponses[0])
        self.assertTrue(reponses[1]== 11 or reponses[2]== 11)
        self.assertTrue(reponses[1]== 2 or reponses[2]== 2)

    def test_est_semi_premier_output_large(self):
        reponses = crypto.facteurs_semi_premier(27_109 * 15_199)
        self.assertTrue(reponses[0])
        self.assertTrue(reponses[1]== 27_109 or reponses[2]== 27_109)
        self.assertTrue(reponses[1]== 15_199 or reponses[2]== 15_199)

        self.assertFalse(crypto.est_semi_premier(2_803 * 317 * 883))
        self.assertFalse(crypto.est_semi_premier(313_675_393))
    
    def test_est_semi_premier_output_moyen(self):
        reponses = crypto.facteurs_semi_premier(8_069 * 26_119)
        self.assertTrue(reponses[0])
        self.assertTrue(reponses[1]== 8_069 or reponses[2]== 8_069)
        self.assertTrue(reponses[1]== 26_119 or reponses[2]== 26_119)

    def test_est_semi_premier_output_petit(self):
        reponses = crypto.facteurs_semi_premier(4)
        self.assertTrue(reponses[0])
        self.assertEqual(2, reponses[1])
        self.assertEqual(2, reponses[2])

        
    def test_est_semi_premier_output_petit(self):
        reponses = crypto.facteurs_semi_premier(39_989**2)
        self.assertTrue(reponses[0])
        self.assertEqual(39_989, reponses[1])
        self.assertEqual(39_989, reponses[2])


    def test_est_semi_premier_output_petit_pareil(self):
        reponses = crypto.facteurs_semi_premier(29 * 23)
        self.assertTrue(reponses[0])
        self.assertTrue(reponses[1]== 29 or reponses[2]== 29)
        self.assertTrue(reponses[1]== 23 or reponses[2]== 23)