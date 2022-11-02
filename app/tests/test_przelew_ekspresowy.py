import unittest

from .test_ksiegowanie_przelewow import TestKsiegowanie, TestKsiegowanieFirmowe
from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestKsiegowanieEkspres(TestKsiegowanie):
    oplata_zwykla = 1

    def test_udany_przelew_ekspresowy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 1000
        konto.zaksieguj_przelew_ekspresowy(200)
        self.assertEqual(konto.saldo, 1000 - 200 - self.oplata_zwykla)

    def test_nieudany_przelew_ekspresowy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 100
        konto.zaksieguj_przelew_ekspresowy(200)
        self.assertEqual(konto.saldo, 100)

    def test_udany_przelew_ekspresowy_saldo_ponizej_0(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 200
        konto.zaksieguj_przelew_ekspresowy(200)
        self.assertEqual(konto.saldo, -self.oplata_zwykla)


class TestKsiegowanieEkspresFirmowe(TestKsiegowanieFirmowe):
    oplata_firma = 5

    def test_udany_przelew_ekspresowy_firmowy(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 1000
        konto.zaksieguj_przelew_ekspresowy(200)
        self.assertEqual(konto.saldo, 1000 - 200 - self.oplata_firma)

    def test_nieudany_przelew_ekspresowy_firmowy(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 200
        konto.zaksieguj_przelew_ekspresowy(300)
        self.assertEqual(konto.saldo, 200)
        
    def test_udany_przelew_ekspresowy_saldo_ponizej_0_firmowy(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 200
        konto.zaksieguj_przelew_ekspresowy(200)
        self.assertEqual(konto.saldo, -self.oplata_firma)
