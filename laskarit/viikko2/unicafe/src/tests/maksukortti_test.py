import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_luodun_kortin_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_rahan_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 11.0")
    
    def test_saldo_vahenee_jos_rahaa_riittaa(self):
        self.maksukortti.ota_rahaa(150)
        self.assertEqual(str(self.maksukortti), "saldo: 8.5")

    def test_saldo_ei_vahene_jos_otetaan_liikaa(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
    
    def test_ota_rahaa_palauttaa_true_jos_rahaa_riittaa(self):
        self.assertTrue(self.maksukortti.ota_rahaa(500))
    
    def test_ota_rahaa_palauttaa_false_jos_otetaan_liikaa(self):
        self.assertFalse(self.maksukortti.ota_rahaa(15000))
    
    #def test_ota_rahaa_palauttaa_false_jos_otetaan_negatiivinen(self):
     #   self.assertFalse(self.maksukortti.ota_rahaa(-200))