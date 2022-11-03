import unittest
from ..KontoFirmowe import KontoFirmowe

class TestTworzenieKontaFirmowego(unittest.TestCase):
    nazwa_firmy = "JanPol"
    nip = "6969839858"

    def test_tworzenie_konta(self):
        konto_firmowe = KontoFirmowe(self.nazwa_firmy, self.nip)
        self.assertEqual(konto_firmowe.nazwa_firmy, self.nazwa_firmy, "Nazwa firmy nie została zapisana!")
        self.assertEqual(konto_firmowe.nip, self.nip, "NIP nie został zapisany!")
        self.assertEqual(konto_firmowe.saldo, 0, "Saldo nie jest zerowe!")

    def test_zbyt_dlugi_nip(self):
        konto_za_dlugi_nip = KontoFirmowe(self.nazwa_firmy, "69698398581")
        self.assertEqual(konto_za_dlugi_nip.nip, "Niepoprawny NIP!", "NIP powinien być niepoprawny")
    
    def test_zbyt_krotki_nip(self):
        konto_za_krotki_nip = KontoFirmowe(self.nazwa_firmy, "696983985")
        self.assertEqual(konto_za_krotki_nip.nip, "Niepoprawny NIP!", "NIP powinien być niepoprawny")
