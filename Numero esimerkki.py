#Kokonaisluku: Integer eli INT
eka = -9

#Kokonaisluku: pitkä eli Long, isot luvut voi jakaa alaviivoilla
toka = 12_456_123_180

#Desimaaliluku: float
kolmas = 7.28

#Kompleksiluku
neljas = 3-2j

print(eka)
print(toka)
print(kolmas)
print(neljas)

muuttuja1 = 100
muuttuja2 = "100"

print(muuttuja1 + muuttuja1)
print(muuttuja2 + muuttuja2)


name = input("Anna nimesi: ")
age = int(input("Anna ikäsi: "))
#Numeerinen ikä castatty eli muutettu int(input-komennolla lausekkeeseen
print("Tervehdys,", name, age, "vuotta.")