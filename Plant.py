class Plant():

    def __init__(self, pavadinimas="", lotyniskas_pavadinimas="", vienmetis=True, zemynas="", aukstis=0, valgomas=True):
        self.pavadinimas = pavadinimas
        self.lotyniskas_pavadinimas = lotyniskas_pavadinimas
        self.vienmetis = vienmetis
        self.zemynas = zemynas
        self.aukstis = aukstis
        self.valgomas = valgomas

    def __str__(self):
       return f"Pavadinimas {self.pavadinimas}, lotyniskas pavadinimas {self.lotyniskas_pavadinimas}, vienmetis {"Taip" if self.vienmetis else "Ne"}, zemynas {self.zemynas}, aukstis {self.aukstis}, valgomas {"Taip" if self.valgomas else "Ne"}"