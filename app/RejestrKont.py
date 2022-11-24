from app.Konto import Konto

class RejestrKont:
    lista_kont = []

    @classmethod
    def dodaj_konto(cls, konto):
        cls.lista_kont.append(konto)

    @classmethod
    def wyszukaj_konto(cls, pesel):
        result = "Nie znaleziono osoby o tym peselu"
        for konto in cls.lista_kont:
            if konto.pesel == pesel:
                result = konto
        return result

    @classmethod
    def ile_kont(cls):
        return len(cls.lista_kont)