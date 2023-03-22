import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    def test_saldon_lisays_toimii(self):
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.00 euroa")
    def test_saldon_vahennus_toimii(self):
        
        self.assertEqual(self.maksukortti.ota_rahaa(200), True)
    def test_saldon_vahennus_toimii_saldo(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 8.00 euroa")
    def test_saldon_yli_vahennys(self):
        
        self.assertEqual(self.maksukortti.ota_rahaa(1200), False)
    def test_saldon_yli_vahennys_saldo(self):
        self.maksukortti.ota_rahaa(1200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    def test_str(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
