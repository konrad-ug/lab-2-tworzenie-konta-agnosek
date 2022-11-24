import unittest
from parameterized import parameterized

from ..KontoFirmowe import KontoFirmowe

class TestZaciaganieKredytuFirmowego(unittest.TestCase):
    nazwa_firmy = "JanPol"
    nip = "6969839858"

    def setUp(self):
        self.konto_firmowe = KontoFirmowe(self.nazwa_firmy, self.nip)

    @parameterized.expand([
        (200, [-20, -1775], 100, True, 300),
        (100, [100], 100, False, 100),
        (200, [], 100, False, 200),
        (0, [-1775, 20], 100, False, 0)
    ])

    def test_zaciaganie_kredytu_firmowego(self, saldo, historia, kwota, oczekiwany_wynik, oczekiwane_saldo):
        self.konto_firmowe.saldo = saldo
        self.konto_firmowe.historia = historia
        self.assertEqual(self.konto_firmowe.zaciagnij_kredyt_firmowy(kwota), oczekiwany_wynik)
        self.assertEqual(self.konto_firmowe.saldo, oczekiwane_saldo)
