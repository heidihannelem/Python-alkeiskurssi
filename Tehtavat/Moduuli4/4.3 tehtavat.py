luvut = []
numero = input("Syötä mikä tahansa luku (Enter lopettaa): ")
while numero != "":
    luku = float(numero)
    luvut.append(luku)
    numero = input("Syötä mikä tahansa luku (Enter lopettaa): ")

print("Pienin luku:" , min(luvut))
print("Isoin luku:" , max(luvut))