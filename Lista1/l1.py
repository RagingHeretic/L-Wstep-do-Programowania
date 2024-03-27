# Hubert Jackowski

# Zadanie 1
print("Nazywam", "się", "Monty", "Python", sep="-", end=".")

# Zadanie 2
print ('Witaj "świecie" Pythona')
print ("Witaj", '"świecie"', "Pythona")

# Zadanie 3
str = """pierwszy wiersz
 drugi wiersz
  trzeci wiersz"""
print(str)

# Zadanie 4
print("Jan"*12)

# Zadanie 5
x = int(input("Podaj pierwszy składnik dodawania: "))
y = int(input("Podaj drugi składnik dodawania: "))
print(f"Wynik dodawania {x} + {y} to {x+y}")

# Zadanie 6
liczba1 = 3.14159
liczba2 = 3
liczba3 = 7.12
liczba4 = "5"
print(type(liczba1))
print(type(liczba2))
print(type(liczba3))
print(type(liczba4))

print(f"{round(float(liczba1), 3)}")
print(f"{round(float(liczba2), 3)}")
print(f"{round(float(liczba3), 3)}")
print(f"{round(float(liczba4), 3)}")

# Zadanie 7
osoba1 = "Anna Cis"
osoba2 = "Konstanty Mączyński"
stanowisko1 = "kierowniczka działu HR"
stanowisko2 = "kierowca"
pensja1 = 7500
pensja2 = 12000
print("{:20} {:22} {}".format("Osoba", "Stanowisko", "Pensja"))
print(f"{osoba1:20} {stanowisko1:22} {pensja1}")
print(f"{osoba2:20} {stanowisko2:22} {pensja2}")

# Zadanie 8
print("Programowanie jest", "\x1b[38;2;255;0;0m\033[1m\033[4m" + "fajne" + "\033[0m")