import re

class Konto:
    def __init__(self, imie, nazwisko, pesel, promo=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.oplata_ekspres = 1
        self.historia = []

        if len(pesel) > 11 or len(pesel) < 11:
            self.pesel = "Niepoprawny pesel!"
        else:
            self.pesel = pesel

        if promo != None:
            if self.sprawdz_rok_urodzenia() > 1960:
                promo_match = re.match("PROM_[A-Z]{3}", promo)
                if promo_match == None:
                    self.promo = "Niepoprawny kod promocyjny!"
                else:
                    self.promo = promo
                    self.saldo = 50
            else:
                self.promo = "Niestety nie możesz skorzystać z tej promocji"
        
    def sprawdz_rok_urodzenia(self):
        cyfry_rok_urodzenia = int(self.pesel[:2])
        cyfry_miesiac_urodzenia = int(self.pesel[2:4])

        if (32 > cyfry_miesiac_urodzenia > 20):
            rok_urodzenia = 2000 + cyfry_rok_urodzenia
        elif (12 > cyfry_miesiac_urodzenia > 1):
            rok_urodzenia = 1900 + cyfry_rok_urodzenia
        
        return rok_urodzenia

    def zaksieguj_przelew_wychodzacy(self, kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota
            self.historia.append(-kwota)

    def zaksieguj_przelew_przychodzacy(self, kwota):
        self.saldo += kwota
        self.historia.append(kwota)

    def zaksieguj_przelew_ekspresowy(self, kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota + self.oplata_ekspres  
            self.historia.append(-kwota)
            self.historia.append(-self.oplata_ekspres)

    def zaciagnij_kredyt(self, kwota):
        warunki_spelnione = self.sprawdz_trzy_ostatnie_dodatnie(self.historia) or self.sprawdz_suma_pieciu(self.historia, kwota)

        if warunki_spelnione:
            self.saldo += kwota

        return warunki_spelnione

    def sprawdz_trzy_ostatnie_dodatnie(self, historia):
        if len(historia) >= 3:
            if all(elem > 0 for elem in historia[-3:]):
                return True
        return False
        
    def sprawdz_suma_pieciu(self, historia, kwota):
        if len(historia) >= 5:
            if sum(historia[-5:]) > kwota:
                return True
        return False
