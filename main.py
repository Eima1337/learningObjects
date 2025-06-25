from Book import Book
from Plant import Plant
from Student import Student

knyga1 = Book()
knyga2 = Book()
knyga3 = Book()
knyga4 = Book("Brisiaus galas", 200, 1992)
knyga5 = Book("Kliudziau", 250, 1993)
knyga6 = Book("Trys muskietininkai", 300, 1950)

books = [knyga1, knyga2, knyga3, knyga4, knyga5, knyga6]

for book in books:
    print(book)

plant1 = Plant()
plant2 = Plant()
plant3 = Plant("Vysnia", "Cerasus", False, "Eurazija",3, True)
plant4 = Plant("Azuolas", "Quercus", False, "Eurazija, Siaures Amerika, Afrika", 60, False)

plants = [plant1, plant2, plant3, plant4]

for plant in plants:
    print(plant)

