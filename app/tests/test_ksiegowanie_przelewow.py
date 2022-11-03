import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestKsiegowanie(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "65051188873"

    def test_udany_przelew_wychodzacy(self):
        udany_wychodzacy_konto = Konto(self.imie, self.nazwisko, self.pesel)
        udany_wychodzacy_konto.saldo = 1000
        udany_wychodzacy_konto.zaksieguj_przelew_wychodzacy(800)
        self.assertEqual(udany_wychodzacy_konto.saldo, 1000-800)

    def test_nieudany_przelew_wychodzacy(self):
        nieudany_wychodzacy_konto = Konto(self.imie, self.nazwisko, self.pesel)
        nieudany_wychodzacy_konto.saldo = 200
        nieudany_wychodzacy_konto.zaksieguj_przelew_wychodzacy(300)
        self.assertEqual(nieudany_wychodzacy_konto.saldo, 200)

    def test_udany_przelew_przychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 200
        konto.zaksieguj_przelew_przychodzacy(300)
        self.assertEqual(konto.saldo, 200 + 300)
      

class TestKsiegowanieFirmowe(TestKsiegowanie):
    nazwa_firmy = "JanPol"
    nip = "6969839858"

    def test_udany_przelew_wychodzacy(self):
        konto_firmowe = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto_firmowe.saldo = 1000
        konto_firmowe.zaksieguj_przelew_wychodzacy(800)
        self.assertEqual(konto_firmowe.saldo, 1000-800)

    def test_nieudany_przelew_wychodzacy(self):
        konto_firmowe = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto_firmowe.saldo = 200
        konto_firmowe.zaksieguj_przelew_wychodzacy(300)
        self.assertEqual(konto_firmowe.saldo, 200)

    def test_udany_przelew_przychodzacy(self):
        konto_firmowe = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto_firmowe.saldo = 200
        konto_firmowe.zaksieguj_przelew_przychodzacy(300)
        self.assertEqual(konto_firmowe.saldo, 200 + 300)