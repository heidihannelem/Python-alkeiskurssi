kuha = float(input("Anna kuhan pituus senttimetreinä: "))

if kuha >= 37:
    print("Vau! Täysimittainen kuha.")

if kuha < 37:
    print(f"Kuhasi on alamittainen {37 - kuha} cm.")
