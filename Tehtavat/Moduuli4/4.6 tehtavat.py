import math

# 1m2 = 10 000cm2
# Säde = halk. / 2
halkaisija1 = int(input("Anna ensimmäisen pizzan halkaisija (cm): "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta (€): "))

halkaisija2 = int(input("Anna toisen pizzan halkaisija (cm): "))
hinta2 = float(input("Anna toisen pizzan hinta (€): "))

sade1 = halkaisija1 / 2
sade2 = halkaisija2 / 2
pinta_ala1 = math.pi * sade1**2
pinta_ala2 = math.pi * sade2**2

neliometri1 = pinta_ala1 / 10000
neliometri2 = pinta_ala2 / 10000

yksikkohinta1 = hinta1 / neliometri1
yksikkohinta2 = hinta2 / neliometri2

print("1. pizzan hinta €/m² on:", yksikkohinta1)
print("2. pizzan hinta €/m² on:", yksikkohinta2)

if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäinen pizza on edullisempi.")
elif yksikkohinta1 > yksikkohinta2:
    print("Toinen pizza on edullisempi.")
else:
    print("Pizzat ovat yhtä edullisia.")
