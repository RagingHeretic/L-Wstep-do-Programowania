# Hubert Jackowski
# Zadanie 1
def wyświetl_grupę(*czlonkowie, opiekun = "Cezary"):
    '''Wyświetla opiekuna grupy i jej członków'''
    print("\n\nOto skład grupy:", end="\n\t")
    print(f"Opiekun: {opiekun}")
    size = len(czlonkowie)
    if(size == 0):
        print(f"\t\tGrupa nie posiada członków")
    else:
        print("\t\t Członkowie grupy:")
        for iterator in range(size):
            print(f"\t\t\t", czlonkowie[iterator])



wyświetl_grupę()
wyświetl_grupę("Anna")
wyświetl_grupę("Anna","Cecylia","Henryk")
wyświetl_grupę("Anna","Cecylia","Henryk", opiekun="Bogdan")

# Zdanie 2
def functionDekorator(function):
    '''Dodaje do udekorowanej funkcji nagłówek z nazwą tej funkcji oraz jej argumentami pozycyjnymi'''
    def innerFunction(*args, **kwargs):
        print("\n\n", "*"*20, f"funkcja {function.__name__}", "*"*20)
        print(f"\targumenty pozycyjne: {args}")
        print(f"\twynik: {function(*args, **kwargs)}")
    return innerFunction

@functionDekorator
def dodaj(a, b = 7):
    """Funkcja zwraca sumę dwóch parametrów a, b """
    return a + b

dodaj(5, 3)
dodaj(3)
