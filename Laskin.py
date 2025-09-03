print("*---Tervetuloa käyttämään laskinta---*")

print("Valitse mitä toimintoa haluat käyttää:\n A: Yhteenlasku \n B: Vähennyslasku "
      "\n C: Kertolasku \n D: Jakolasku \n E: Kokonaislukujako")

Valinta = input("Valintasi (A - E): ")

if Valinta == "A":
    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))
    print("Yhteenlasku:" , a + b)
elif Valinta == "B":
    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))
    print("Vähennyslasku:" , a - b)
elif Valinta == "C":
    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))
    print("Kertolasku:" , a * b)
elif Valinta == "D":
    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))
    print("Desimaalijakolasku:" , a / b)
elif Valinta == "E":
    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))
    print("Kokonaislukujako:" , a // b)
else:
    print("Valintasi on virheellinen.")

