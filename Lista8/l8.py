# Hubert Jackowski
import pakiet_pracownik
import json
import inspect
import pathlib
import csv

# Zadanie 1
class CustomJsonEncoder(json.JSONEncoder):
    def default(self, object):
        result = object.__dict__
        metods = {}
        for method in [method for method in dir(object) if method.startswith('__') is False and callable(getattr(object, method))]:
            metods[f"{method}"] = inspect.getsource(getattr(object, method))
        # Instrukcja poda kody źródłowe wszystkich funkcji bez dundera (niespecjalnych)
        result["metody"] = metods
        return result


o = pakiet_pracownik.Osoba("Karol", "Mackiewicz", "600 100 300")
p = pakiet_pracownik.Pracownik("Anna", "Kowalska", "603 500 400", "Kowal Inwest", "specjalista ds. kadr")

with open(pathlib.Path.cwd() / "os_prac_zserial" / "o.json", "w", encoding="utf-8") as writer:
    json.dump(o, writer, indent=4, cls=CustomJsonEncoder)
with open(pathlib.Path.cwd() / "os_prac_zserial" / "p.json", "w", encoding="utf-8") as writer:
    json.dump(p, writer, indent=4, cls=CustomJsonEncoder)


# Zadanie 2 a)
print("\n2 a)\n")
with open(pathlib.Path.cwd() / "zakupione_produkty.csv", encoding="utf-8") as reader:
    text = csv.reader(reader, delimiter=',')
    listOfPrices = []
    listOfNames = []
    for row in text:
        if(row[4] != "CENA"):
            listOfPrices.append(float(row[4].replace(',', '.')))
            listOfNames.append(row[0])
            print(row[0])
    print("-"*20)
    for i in range(len(listOfPrices)):
        if(listOfPrices[i] == min(listOfPrices)):
            print("najtańszy produkt: ", listOfNames[i])
            break
    for i in range(len(listOfPrices)):
        if(listOfPrices[i] == max(listOfPrices)):
            print("najdroższy produkt: ", listOfNames[i])


# Zadanie 2 b)
print("\n2 b)\n")
with open(pathlib.Path.cwd() / "zakupione_produkty.csv", "r", encoding="utf-8") as reader, open(pathlib.Path.cwd() / "zakupione_produkty-modyfikowane.csv", 'w', newline="", encoding="utf-8") as writer:
    text = csv.reader(reader, delimiter=',')
    textwriter = csv.writer(writer, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
    textwriter.writerows(text)

with open(pathlib.Path.cwd() / "zakupione_produkty-modyfikowane.csv", encoding="utf-8") as reader:
    text = csv.reader(reader, delimiter=';')
    listOfPrices = []
    listOfNames = []
    for row in text:
        if(row[4] != "CENA"):
            listOfPrices.append(float(row[4].replace(',', '.')))
            listOfNames.append(row[0])
            print(row[0])
    print("-"*20)
    for i in range(len(listOfPrices)):
        if(listOfPrices[i] == min(listOfPrices)):
            print("najtańszy produkt: ", listOfNames[i])
            break
    for i in range(len(listOfPrices)):
        if(listOfPrices[i] == max(listOfPrices)):
            print("najdroższy produkt: ", listOfNames[i])