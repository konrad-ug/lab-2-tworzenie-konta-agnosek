import unittest

from ..Konto import Konto
from ..RejestrKont import RejestrKont

class TestRejestrKont(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "65051188873"

    @classmethod
    def setUpClass(cls):
        cls.konto = Konto(cls.imie, cls.nazwisko, cls.pesel)
        RejestrKont.dodaj_konto(cls.konto)
    
    @classmethod
    def tearDownClass(cls):
        RejestrKont.lista = []

    def test_1_dodawanie_drugiego_konta(self):
        RejestrKont.dodaj_konto(self.konto)
        self.assertEqual(RejestrKont.ile_kont(), 2)

    def test_2_dodanie_trzeciego_konta(self):
        RejestrKont.dodaj_konto(self.konto)
        self.assertEqual(RejestrKont.ile_kont(), 3)

    def test_0_wyszukaj_konto(self):
        wyszukanie = RejestrKont.wyszukaj_konto(self.konto.pesel)
        self.assertEqual(wyszukanie.nazwisko, self.konto.nazwisko)

    def test_wyszukaj_nieistniejace_konto(self):
        wyszukanie = RejestrKont.wyszukaj_konto(1)
        self.assertEqual(wyszukanie, "Nie znaleziono osoby o tym peselu")
