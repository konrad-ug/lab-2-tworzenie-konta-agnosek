import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678901"
    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imię nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertNotEqual(pierwsze_konto.pesel, "Niepoprawny pesel!", "Niepoprawny pesel!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
    
    def test_zbyt_dlugi_pesel(self):
        pesel = "1234567890112123"
        pierwsze_konto = Konto(self.imie, self.nazwisko, pesel)
        self.assertEqual(pierwsze_konto.pesel, "Niepoprawny pesel!", "Niepoprawny pesel!")

    def test_zbyt_krotki_pesel(self):
        pesel = "12345"
        pierwsze_konto = Konto(self.imie, self.nazwisko, pesel)
        self.assertEqual(pierwsze_konto.pesel, "Niepoprawny pesel!", "Niepoprawny pesel!")

    def test_kod_promo(self):
        promo = "PROM_XYZ"
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel, promo)
        self.assertEqual(pierwsze_konto.promo, "PROM_XYZ", "Kod promo nie został zapisany!")

    #tutaj proszę dodawać nowe testy
