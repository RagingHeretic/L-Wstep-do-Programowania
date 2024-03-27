# Hubert Jackowski
# Zadanie 1

import os
import pathlib
import re
import zipfile

inputFile = "zad1pliki"

filePath = pathlib.Path.cwd() / "archiwa"
if(not(filePath.exists())):
    os.mkdir(filePath)

# filePath /= "moje_arch.zip"
with zipfile.ZipFile(filePath / "moje_arch.zip", "w") as ZipFile:
    for dirname, subdirs, files in os.walk(inputFile):
        ZipFile.write(dirname)
        for filename in files:
            ZipFile.write(os.path.join(dirname, filename))
with zipfile.ZipFile(filePath / "moje_arch_haslo.zip", "w") as ZipFile:
    for dirname, subdirs, files in os.walk(inputFile):
        ZipFile.write(dirname)
        for filename in files:
            ZipFile.write(os.path.join(dirname, filename))
    ZipFile.setpassword(bytes("ff_*_klucz_arch_ab", "utf-8"))

with zipfile.ZipFile(filePath / "moje_arch.zip", "r") as ZipFile:
    filePathExtractedEx1 = filePath / "po_ekstrakcji1"
    if (not (filePathExtractedEx1.exists())):
        os.mkdir(filePathExtractedEx1)
    ZipFile.extractall(filePathExtractedEx1)

with zipfile.ZipFile(filePath / "moje_arch_haslo.zip", "r") as ZipFile:
    filePathExtractedEx2 = filePath / "po_ekstrakcji2"
    if (not (filePathExtractedEx1.exists())):
        os.mkdir(filePathExtractedEx1)
    ZipFile.extractall(filePathExtractedEx2)

# Zadanie 2
path = pathlib.Path.cwd() / "przyklad_zad_2"
lst = []
for dirname, subdirs, files in os.walk(path):
    for filename in files:
        lst.append(filename)
for element in lst:
    if(not(re.search(".*praca.*", element) == None)):
        print(element)