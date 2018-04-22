# for radek in range(4):
#     print ("a")

# for radek in range (5):
#     print (5*"X ", sep = " ", end = " \n")

# for radek in range (5):
#     print (radek * 0, radek * 1, radek * 2, radek * 3, radek * 4)

# for radek in range (5):
#     print (radek * "x", sep = " ", end = " \n")

# for radek in range (4):
#     if radek == 0:
#         print("První řádek")
#     elif radek > 0:
#         print ("není první")

# for radek in range (6):
#     if radek == 0 or radek == 5:
#         print (6*"X ", sep = " ", end = " \n")
#     else:
#         print ("X ", "X", sep = " "*8)

# úkol 14
# cislo = int(input("Zadej range: "))
# for radek in range (cislo):
#         print (cislo * "X ", sep = " ", end = " \n")

# for c in "Ahoj světe!":
#     print (c)

# for c in 38:
#     print (c)

# a = int(input("Zadej číslo a: "))
# b = int(input("Zadej číslo b: "))
# c = int(input("Zadej číslo c: "))
# soucet = a + b + c
# print ("Součet je: ", soucet)
#
# if soucet >= 10:
#     print ("Součet je větší než 10")
# else:
#     print ("Součet je menší než 10")

# cislo = int(input("Zadej číslo: "))
# sude_cislo = cislo % 2
# if sude_cislo == 0:
#     print ("číslo je sudé:")
# else:
#     print ("číslo je liché")

for radek in range(101):
    bum = radek % 3
    bac = radek % 5

    if bum == 0:
        print ("bum")
    if bac == 0:
        print ("bác")
    if bac == 0 and bum == 0:
        print ("bum bác")
    else:
        print (radek)
