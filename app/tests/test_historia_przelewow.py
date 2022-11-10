import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestHistoriaPrzelewow(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "65051188873"
    nazwa_firmy = "JanPol"
    nip = "6969839858"

    def test_historia_zwykly_przychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.zaksieguj_przelew_przychodzacy(200)
        self.assertEqual(konto.historia, [200], "Niepoprawna historia przelewów!")

    def test_historia_zwykly_wychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 20
        konto.zaksieguj_przelew_wychodzacy(20)
        self.assertEqual(konto.historia, [-20], "Niepoprawna historia przelewów!")

    def test_historia_ekspresowy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 50
        konto.zaksieguj_przelew_ekspresowy(50)
        self.assertEqual(konto.historia, [-50, -1], "Niepoprawna historia przelewów!")

    def test_historia_nieudany_wychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.zaksieguj_przelew_wychodzacy(20)
        self.assertEqual(konto.historia, [], "Niepoprawna historia przelewów!")

    def test_historia_firma_przychodzacy(self):
        konto_firmowe = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto_firmowe.zaksieguj_przelew_przychodzacy(200)
        self.assertEqual(konto_firmowe.historia, [200], "Niepoprawna historia przelewów!")

    def test_historia_firma_wychodzacy(self):
        konto_firmowe = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto_firmowe.saldo = 20
        konto_firmowe.zaksieguj_przelew_wychodzacy(20)
        self.assertEqual(konto_firmowe.historia, [-20], "Niepoprawna historia przelewów!")

    def test_historia_firma_ekspresowy(self):
        konto_firmowe = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto_firmowe.saldo = 50
        konto_firmowe.zaksieguj_przelew_ekspresowy(50)
        self.assertEqual(konto_firmowe.historia, [-50, -5], "Niepoprawna historia przelewów!")

    def test_historia_firma_nieudany_wychodzacy(self):
        konto_firmowe = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto_firmowe.zaksieguj_przelew_wychodzacy(20)
        self.assertEqual(konto_firmowe.historia, [], "Niepoprawna historia przelewów!")
      