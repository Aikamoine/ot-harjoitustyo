import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.koyhakortti = Maksukortti(200)

    def test_luodun_kassapaatteen_raha_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_luodun_kassapaatten_myynnit_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateismaksu_edullinen_riittava_summa_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)

    def test_kateismaksu_maukas_riittava_summa_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)

    def test_kateismaksu_edullinen_riittava_summa_myynnit_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateismaksu_maukas_riittava_summa_myynnit_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateismaksu_edullinen_riittamaton_summa_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_kateismaksu_maukas_riittamaton_summa_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

    def test_kateismaksu_edullinen_riittamaton_summa_myynnit_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateismaksu_maukas_riittamaton_summa_myynnit_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttimaksu_edullinen_riittava_summa_veloitus_onnistuu(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
        self.assertEqual(self.maksukortti.saldo, 760)

    def test_korttimaksu_maukas_riittava_summa_veloitus_onnistuu(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_korttimaksu_edullinen_riittava_summa_myynnit_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttimaksu_maukas_riittava_summa_myynnit_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttimaksu_edullinen_riittamaton_summa_veloitus_ei_onnistu(self):
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.koyhakortti))
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_korttimaksu_maukas_riittamaton_summa_veloitus_ei_onnistu(self):
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.koyhakortti))
        self.assertEqual(self.maksukortti.saldo, 1000)
    
    def test_korttimaksu_edullinen_riittamaton_summa_myynnit_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kortilla(self.koyhakortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttimaksu_maukas_riittamaton_summa_myynnit_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.koyhakortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttimaksu_edullinen_ei_muuta_kassaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttimaksu_maukas_ei_muuta_kassaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_rahan_lataaminen_kasvattaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo, 2000)

    def test_rahan_lataaminen_kasvattaa_kassan_rahoja(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
    
    def test_negatiivisen_summan_lataaminen_kortille_ei_kasvata_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_negatiivisen_summan_lataaminen_ei_kasvata_kassan_rahoja(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)