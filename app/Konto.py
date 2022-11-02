class Konto:
    def __init__(self, imie, nazwisko, pesel, promo=None):
        self.imie = imie
        self.nazwisko = nazwisko
        if len(pesel) > 11 or len(pesel) < 11:
            self.pesel = "Niepoprawny pesel!"
        else:
            self.pesel = pesel
        self.saldo = 0
        self.promo = promo
        
