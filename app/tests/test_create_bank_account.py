import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "65051188873"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imię nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.pesel, "65051188873", "Pesel nie został zapisany!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
    
    def test_zbyt_dlugi_pesel(self):
        za_dlugi_pesel = "1234567890112123"
        dlugi_pesel_konto = Konto(self.imie, self.nazwisko, za_dlugi_pesel)
        self.assertEqual(dlugi_pesel_konto.pesel, "Niepoprawny pesel!", "Pesel powinien być niepoprawny")

    def test_zbyt_krotki_pesel(self):
        za_krotki_pesel = "12345"
        krotki_pesel_konto = Konto(self.imie, self.nazwisko, za_krotki_pesel)
        self.assertEqual(krotki_pesel_konto.pesel, "Niepoprawny pesel!", "Pesel powinien być niepoprawny")

    def test_kod_promo(self):
        popr_promo = "PROM_XYZ"
        promo_konto = Konto(self.imie, self.nazwisko, self.pesel, popr_promo)
        self.assertEqual(promo_konto.promo, "PROM_XYZ", "Kod promo nie został zapisany!")
        self.assertEqual(promo_konto.saldo, 50, "Niedodany rabat!")
    
    def test_niepoprawny_kod_promo(self):
        niepop_promo = "PROM_XY"
        niepop_promo_konto = Konto(self.imie, self.nazwisko, self.pesel, niepop_promo)
        self.assertEqual(niepop_promo_konto.promo, "Niepoprawny kod promocyjny!", "Kod promocyjny powinien być niepoprawny")
        self.assertEqual(niepop_promo_konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_kod_promo_przed_1960(self):
        popr_promo = "PROM_ABC"
        przed_1960_pesel = "56111521491"
        promo_przed_1960_konto = Konto(self.imie, self.nazwisko, przed_1960_pesel, popr_promo)
        self.assertEqual(promo_przed_1960_konto.promo, "Niestety nie możesz skorzystać z tej promocji", "Promocja niepoprawnie dodana")

    def test_tworzenie_konta_po_2000(self):
        konto_po_2000 = Konto(self.imie, self.nazwisko, "04300199987")
        self.assertEqual(konto_po_2000.sprawdz_rok_urodzenia(), 2004, "Niepoprawne obliczenie roku urodzenia!")
        