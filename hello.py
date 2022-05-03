"""
Tento modul ukazuje použití data classu k zjednodušení vytvoření třídy

Není pak potřeba vytvářet konstruktor a jiné metody tříd (fuck OOP zápis)
"""

from dataclasses import dataclass

@dataclass
class Osoba:
    jmeno: str
    prijmeni: str
    vek: int

    # Ukázka konstruktoru, který není potřeba
    # def __init__(self, jmeno, prijmeni, vek):
    #     self.jmeno = jmeno
    #     self.prijmeni = prijmeni
    #     self.vek = vek

osoba = Osoba("John", "Doe", "36")
print(osoba)