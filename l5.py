# Hubert Jackowski
# Z1 -0,2p należało użyć modułu time
# Zadanie 1

import datetime
def dateInFormat(date):
    Year = 0
    for i in range(4):
        Year *= 10
        Year += int(date[i])
    Month = 0
    for i in range(5, 7):
        Month *= 10
        Month += int(date[i])
    Day = 0
    for i in range(8, 10):
        Day *= 10
        Day += int(date[i])
    return datetime.date(Year, Month, Day)
def przetworz_daty(str1, str2):
    date1 = dateInFormat(str1)
    date2 = dateInFormat(str2)

    dateDelta = (date2 - date1).days
    weekDay = (("Poniedziałek"), ("Wtorek"), ("Środa"), ("Czwartek"), ("Piątek"), ("Sobota"), ("Niedziela"))
    print(f"Dzień tygodnia dla {date1} to {weekDay[date1.weekday()]}, a dla {date2} to {weekDay[date2.weekday()]}. Między {date1} a {date2} upłynęło {dateDelta} dni.")

przetworz_daty("2023-10-02", "2023-11-08")

# Zadanie 2
import segno
from PIL import Image
qrcode = segno.make('Warto programować')
qrcode.save('qrpng.png', scale=4, dark='darkblue', data_dark='steelblue')
qrcode.save('qrpng.pdf')
qrcode.save('rotatedqrpng.png', scale=4, dark='darkblue', data_dark='steelblue')
im = Image.open('rotatedqrpng.png')
im = im.rotate(60, expand=True)
im.save('rotatedqrpng.png')