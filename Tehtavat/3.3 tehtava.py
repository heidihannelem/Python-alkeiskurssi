sukupuoli = input("Kerro biologinen sukupuolesi (mies/nainen): ").lower()

if sukupuoli == "nainen":
    hb = int(input("Anna hemoglobiiniarvosi: "))
    if hb < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hb <= 175:
        print("Hemoglobiinisi on normaali.")
    else:
        print("Hemoglobiinisi on korkea.")


elif sukupuoli == "mies":
    hb = int(input("Anna hemoglobiiniarvosi: "))
    if hb < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hb <= 195:
        print("Hemoglobiinisi on normaali.")
    else:
        print("Hemoglobiinisi on korkea.")

else:
    print("Valintasi on virheellinen.")
