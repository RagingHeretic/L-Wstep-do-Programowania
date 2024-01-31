# Zadanie 1
# print((6+5)*3)
# print((6.893 + 5.74)*3)
# print(6 + 5 * 3)
# print(41/6)
# print(41%6)
# print(41-(41%6)*6)

# Zadanie 2
# print(8**21)
# print(pow(8, 21))

# Zadanie 3
# A = ""
# B = ""
# if(A==B):
#         print("1 true")
# A = ""
# B = ''
# if(A==B):
#         print("2 true")
# A = ""
# B = " "
# if(A==B):
#         print("3 true")
# A = ""
# B = " ".strip()
# if(A==B):
#         print("4 true")
# A = ""
# B = " ".lstrip()
# if(A==B):
#         print("5 true")
# A = ""
# B = " ".rstrip()
# if(A==B):
#         print("6 true")
# A = "2"
# B = 2
# if(A==B):
#         print("7 true")
# A = 61-23
# B = 38
# if(A==B):
#         print("8 true")
# A = 5 > 7
# B = 5 > -7
# if(A==B):
#         print("9 true")
# A = 5 > 7
# B = -5 > -7
# if(A==B):
#         print("10 true")
# A = 5 > 7
# B = -7 > -5
# if(A==B):
#         print("11 true")
# A = 1278394
# B = 1_278_394
# if(A==B):
#         print("12 true")

# Zadanie 4
# num = float(input("Podaj liczbę "))
# print(f"wpisano liczbę {num}, a jeśli podzielimy ją przez 6 to otrzymamy {round(num/6, 2)}")

# Zadanie 5
# wyr1 = (3 + 1.0 == 4 and not 5 > 7)
# print("1", type(wyr1), " wartość:", wyr1)
# wyr2 = (3 + 1.0 == 4 and 5 > 7)
# print("2", type(wyr2), " wartość:", wyr2)
# wyr3 = (3 + 1.0 == 4 or 5 > 7)
# print("3", type(wyr3), " wartość:", wyr3)
# wyr4 = (3 + 1.0 == 4 or not 5 > 7)
# print("4", type(wyr4), " wartość:", wyr4)

# Zadanie 6
# num = float(input("Podaj liczbę: "))
# if(num == round(num)):
#     print(f"liczba {num} jest całkowita")
# else:
#     print(f"liczba {num} nie jest całkowita")
# if((num*10)//10 == num):
#     print(f"liczba {num} jest całkowita")
# else:
#     print(f"liczba {num} nie jest całkowita")

# Zadanie 7
# num = float(input("Podaj liczbę: "))
# if(num <= 6):
#     print(f"Podana liczba {num} jest za mała")
# elif(num == 24):
#     print("Podana liczba nie może wynosić 24")
# elif(num == 43):
#     print("Podana liczba nie może wynosić 43")
# else:
#     print(f"Podana liczba {num} jest prawidłowa")

# Zadanie 8
# num = float(input("Podaj liczbę: "))
# iterator = 0
# while num-7 >= 2:
#     if(num == 13):
#         print("Z powodu otrzymania liczby 13 przerwano operacje")
#         break
#     print("Odjęto 7")
#     num -= 7
#     iterator += 1
# print(f"Wynik końcowy to {num}, wykonano {iterator} operacji/ę")

# Zadanie 9
# iterator = 6
# while iterator <= 51:
#     print(iterator)
#     iterator += 1

# Zadanie 10
# iterator = 6
# while iterator <= 51:
#     if(iterator%2 == 1):
#         print(iterator)
#     iterator += 1

# Zadanie 11
# iterator = 6
# sum = 0
# while iterator <= 51:
#     sum += iterator
#     iterator += 1
# print(sum)