import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        
    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)
    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    def test_maukkaat_alussa_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    def test_edulliset_alussa_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_onnistunut_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)
    def test_onnistunut_edullinen2(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    def test_onnistunut_edullinen3(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    def test_epaonnistunut_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)
    def test_epaonnistunut_edullinen2(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    def test_epaonnistunut_edullinen3(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    
    def test_onnistunut_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)
    def test_onnistunut_maukas2(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    def test_onnistunut_maukas3(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    def test_epaonnistunut_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(230), 230)
    def test_epaonnistunut_maukas2(self):
        self.kassapaate.syo_maukkaasti_kateisella(230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    def test_epaonnistunut_maukas3(self):
        self.kassapaate.syo_maukkaasti_kateisella(230)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_onnistunut_edullinen_kortilla(self):
        maksukortti = Maksukortti(240)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), True)
    def test_onnistunut_edullinen_kortilla2(self):
        maksukortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    def test_epaonnistunut_edullinen_kortilla(self):
        maksukortti = Maksukortti(230)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)
    def test_epaonnistunut_edullinen_kortilla2(self):
        maksukortti = Maksukortti(230)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_onnistunut_maukas_kortilla(self):
        maksukortti = Maksukortti(400)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), True)
    def test_onnistunut_maukas_kortilla2(self):
        maksukortti = Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    def test_epaonnistunut_maukas_kortilla(self):
        maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)
    def test_epaonnistunut_maukas_kortilla2(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_lataa_kortti_fail(self):
        maksukortti = Maksukortti(0)
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(maksukortti,-10), None)
    def test_lataa_kortti_fail2(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti,-10)
        self.assertEqual(maksukortti.saldo,0)
    def test_lataa_kortti_ok2(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti,1)
        self.assertEqual(maksukortti.saldo,1)
    def test_lataa_kortti_ok(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti,1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100001)
    
    
    