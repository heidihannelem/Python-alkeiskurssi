# Tehtävä 2.1
nimi = input("Kerro etunimesi: ")
print("Tervehdys",nimi,)

# Tehtävä 2.2
import math
sade = float(input("Anna ympyrän säde: "))
ala = math.pi * sade ** 2
print(f"Ympyrän pinta-ala on: {ala:.2f}")

# Tehtävä 2.3
kanta = int(input("Anna suorakolmion kanta: "))
korkeus = int(input("Anna suorakolmion korkeus: "))
pintaala = kanta * korkeus
print(f"Suorakolmion pinta-ala on: {pintaala:.2f}")
piiri = 2 * (kanta + korkeus)
print(f"Suorakolmion piiri on: {piiri:.2f}")

# Tehtävä 2.4
luku1 = int(input("Anna kokonaisluku: "))
luku2 = int(input("Anna kokonaisluku: "))
luku3 = int(input("Anna kokonaisluku: "))
summa = luku1 + luku2 + luku3
print(f"Yhteissumma on: {summa}")

tulo = luku1 * luku2 * luku3
print(f"Tulo on: {tulo}")

keskiarvo = summa / 3
print(f"Keskiarvo on: {keskiarvo:.2f}")

# Tehtävä 2.5
leiviska = int(input("Anna leiviskät: "))
naulat = int(input("Anna naulat: "))
luodit = int(input("Anna luodit: "))
kokonaisnaulat = leiviska * 20
kokonaisluodit = kokonaisnaulat * 32 + luodit
luoditgrammoina = kokonaisluodit * 13.3
kg = luoditgrammoina // 1000
g = luoditgrammoina % 1000
print(f"Massa nykymittojen mukaan on: {kg} kilogrammaa ja {g:.2f} grammaa")

# Tehtävä 2.6
import random
print(f"Lukon 3-numeroinen koodi on: {random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}")
print(f"Lukon 4-numeroinen koodi on: {random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}")