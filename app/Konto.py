import re

class Konto:
    def __init__(self, imie, nazwisko, pesel, promo=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0

        if len(pesel) > 11 or len(pesel) < 11:
            self.pesel = "Niepoprawny pesel!"
        else:
            self.pesel = pesel

        if promo != None:
            if self.sprawdz_rok_urodzenia(pesel) > 1960:
                promo_match = re.match("PROM_[A-Z]{3}", promo)
                if promo_match == None:
                    self.promo = "Niepoprawny kod promocyjny!"
                else:
                    self.promo = promo
                    self.saldo = 50
            else:
                self.promo = "Niestety nie możesz skorzystać z tej promocji"
        
    def sprawdz_rok_urodzenia(self, pesel):
        cyfry_rok_urodzenia = int(pesel[:2])
        cyfry_miesiac_urodzenia = int(pesel[2:4])

        if (32 > cyfry_miesiac_urodzenia > 20):
            rok_urodzenia = 2000 + cyfry_rok_urodzenia
        elif (12 > cyfry_miesiac_urodzenia > 1):
            rok_urodzenia = 1900 + cyfry_rok_urodzenia
        
        return rok_urodzenia