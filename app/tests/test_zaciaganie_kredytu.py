import unittest
from parameterized import parameterized

from ..Konto import Konto

class TestZaciaganieKredytu(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "65051188873"

    def setUp(self):
        self.konto = Konto(self.imie, self.nazwisko, self.pesel)

    @parameterized.expand([
        ([20, 20, 20], 100, True, 100),
        ([20, 20], 100, False, 0),
        ([-20, -20, -20], 100, False, 0),
        ([20, -20, 20], 100, False, 0),
        ([20, 20, 20, 20, 21], 100, True, 100),
        ([20, 20, 20, -10, 51], 100, True, 100),
        ([10, 10, 10, 10, -10], 100, False, 0)
    ])

    def test_zaciaganie_kredytu(self, historia, kwota, oczekiwany_wynik, saldo):
        self.konto.historia = historia
        self.assertEqual(self.konto.zaciagnij_kredyt(kwota), oczekiwany_wynik)
        self.assertEqual(self.konto.saldo, saldo)
