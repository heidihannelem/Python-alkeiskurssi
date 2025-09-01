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
print(f"Suorakolmion inta-ala on: {pintaala:.2f}")
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
