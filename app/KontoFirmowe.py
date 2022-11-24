from app.Konto import Konto

class KontoFirmowe(Konto):

    def __init__(self, nazwa_firmy, nip):
        self.nazwa_firmy = nazwa_firmy
        self.nip = nip if self.czy_poprawny_nip(nip) else "Niepoprawny NIP!"
        self.saldo = 0
        self.oplata_ekspres = 5
        self.historia = []

    def czy_poprawny_nip(self, nip):
        return len(nip) == 10

    def zaciagnij_kredyt_firmowy(self, kwota):
        if self.saldo >= 2*kwota and -1775 in self.historia:
            self.saldo += kwota
            return True
        return False