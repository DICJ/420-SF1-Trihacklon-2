import unittest
from CalculatriceCrypto import CalculatriceCrypto as crypto

class TailleTest(unittest.TestCase): 
    def test_entropie(self):    
        self.assertEqual(23, crypto.nb_de_bits(7_352_837)) # 111 0000 0011 0010 0000 0101
    
    def test_entropie_limite(self):
        self.assertEqual(1, crypto.nb_de_bits(1))

    def test_entropie_petit(self):    
        self.assertEqual(8, crypto.nb_de_bits(255))
        self.assertEqual(9, crypto.nb_de_bits(256))

    def test_nb_octets(self):
        self.assertEqual(3, crypto.nb_octets(7_352_837))
    
    def test_nb_octets_limite(self):
        self.assertEqual(1, crypto.nb_octets(1))
    
    def test_nb_octets_petit(self): 
        self.assertEqual(1, crypto.nb_octets(255))
        self.assertEqual(2, crypto.nb_octets(256))
    
    def test_somme_des_chiffres(self):
        self.assertEqual(35, crypto.somme_des_chiffres(7_352_837))
        self.assertEqual(10, crypto.somme_des_chiffres(1_333))
    
    def test_somme_des_chiffres_encore(self):
        self.assertEqual(1, crypto.somme_des_chiffres(1))
        self.assertEqual(1, crypto.somme_des_chiffres(10000))
    
    def test_somme_des_chiffres_jusqu_a_un_chiffre(self):
        self.assertEqual(8, crypto.somme_des_chiffres_jusqua_un_chiffre(7_352_837))
    
    def test_somme_des_chiffres_jusqu_a_un_chiffre_encore(self):
        self.assertEqual(1, crypto.somme_des_chiffres_jusqua_un_chiffre(1_333))
    
    def test_mode(self):
        self.assertEqual(9, crypto.mode(39_999_138))
    
    def test_mode_encore(self):    
        self.assertEqual(0, crypto.mode(1_902_938_000))
    
    def test_mode_limite(self):
        self.assertEqual(1, crypto.mode(1))
    
    def test_mode_choix_multiple(self):
        mode = crypto.mode(1_334_569_694)
        self.assertTrue(mode == 3 or mode == 4 or mode == 6 or mode == 9)
    
    def test_nombre_de_chiffre(self):
        self.assertEqual(0, crypto.nb_de_chiffres(1_234_567_895, 0))
        self.assertEqual(0, crypto.nb_de_chiffres(2_034_567_890, 1))
        self.assertEqual(1, crypto.nb_de_chiffres(1_234_567_890, 2))
        self.assertEqual(2, crypto.nb_de_chiffres(1_233_567_890, 3))
        self.assertEqual(2, crypto.nb_de_chiffres(1_434_567_890, 4))
        self.assertEqual(0, crypto.nb_de_chiffres(1_234_067_890, 5))
        self.assertEqual(2, crypto.nb_de_chiffres(1_234_567_896, 6))
        self.assertEqual(1, crypto.nb_de_chiffres(1_234_567_890, 7))
        self.assertEqual(1, crypto.nb_de_chiffres(1_234_567_890, 8))
        self.assertEqual(2, crypto.nb_de_chiffres(1_234_569_890, 9))
    
    def test_nombre_de_chiffre_limite(self):     
        self.assertEqual(1, crypto.nb_de_chiffres(1, 1))
        self.assertEqual(0, crypto.nb_de_chiffres(1, 3))
    