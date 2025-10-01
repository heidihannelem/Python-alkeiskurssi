summa = 0
# tämä laskee yhteen syöttämäsi summat
while True:
    num = int(input("Anna kokonaisluku tai -1 lopettaaksesi: "))

    if num == -1:
        break
    if num >= 10:
        continue
        # Eli jos numero on isompi kuin 10, ei sitä lisätä mukaan
    summa += num

print(f"Summa on {summa}.")

