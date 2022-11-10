import unittest

from ..Konto import Konto

class TestZaciaganieKredytu(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "65051188873"

    def test_udany_kredyt_trzy_wplaty(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [20, 20, 20]
        self.assertTrue(konto.zaciagnij_kredyt(100), "Niepoprawnie - brak udzielenia kredytu!")
        self.assertEqual(konto.saldo, 100, "Niepoprawne saldo po udzieleniu kredytu!")

    def test_nieudany_kredyt_za_krotka_historia(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [20, 20]
        self.assertFalse(konto.zaciagnij_kredyt(100), "Niepoprawnie - udzielenie kredytu!")
        self.assertEqual(konto.saldo, 0, "Niepoprawne saldo")

    def test_nieudany_kredyt_trzy_wyplaty(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [-20, -20, -20]
        self.assertFalse(konto.zaciagnij_kredyt(100), "Niepoprawnie - udzielenie kredytu!")
        self.assertEqual(konto.saldo, 0, "Niepoprawne saldo")

    def test_nieudany_kredyt_mieszane(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [20, -20, 20]
        self.assertFalse(konto.zaciagnij_kredyt(100), "Niepoprawnie - udzielenie kredytu!")
        self.assertEqual(konto.saldo, 0, "Niepoprawne saldo")

    def test_udany_kredyt_suma_piec(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [20, 20, 20, 20, 21]
        self.assertTrue(konto.zaciagnij_kredyt(100), "Niepoprawnie - brak udzielenia kredytu!")
        self.assertEqual(konto.saldo, 100, "Niepoprawne saldo po udzieleniu kredytu!")

    def test_nieudany_kredyt_za_mala_suma_piec(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [20, 20, 20, 20, -5]
        self.assertFalse(konto.zaciagnij_kredyt(100), "Niepoprawnie - udzielenie kredytu!")
        self.assertEqual(konto.saldo, 0, "Niepoprawne saldo")

    def test_udany_kredyt_suma_piec_trzy_wyplaty(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [100, 100, -10, -10, -10]
        self.assertTrue(konto.zaciagnij_kredyt(100), "Niepoprawnie - brak udzielenia kredytu!")
        self.assertEqual(konto.saldo, 100, "Niepoprawne saldo po udzieleniu kredytu!")