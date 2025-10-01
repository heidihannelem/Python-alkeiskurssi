nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mari"]
nimet2 = ["Allu", "Ninni"]
names = []

nimi = input("Anna ensimmäinen nimi tai lopeta Enterillä: ")

while nimi!= "":
    names.append(nimi)
    nimi = input("Anna seuraava nimi tai lopeta Enterillä: ")

print(names)

# remove poistaa ensimmäisen listasta esim. nimet.remove("Pekka)

# instert lisää esim.
nimet.insert(4, "Teppo")
print(nimet)

# extend liittää listat toisiinsa
nimet.extend(nimet2)
print(nimet2)

print(nimet.index("Olga"))
# voidaan kysyä mikä arvon järjestysluku on

#in voidaan testata onko listassa esim. Onko Matti meidän listassa
if "Matti" in nimet:
    print("Matti löytyy")
else:
    print("Matti hukassa!")

# sort voidaan lajitella lista esim. luvut.sort() aakkos- tai suuruusjärjestykseen
nimet.sort()
print(nimet)
# toiseen suuntaan lista, ä-a HUOM! indeksit ei muutu
nimet.sort(reverse=True)
print(nimet)

