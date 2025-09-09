print("Anna hyttiluokkasi seuraavista vaihtoehdoista \n A: A-hytti \n B: B-Hytti "
      "\n C: C-hytti \n D: LUX-hytti")

Valinta = input("Valintasi (A - D): ").upper()

if Valinta == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")

elif Valinta == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")

elif Valinta == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")

elif Valinta == "D":
    print("LUX on parvekkeellinen hytti yläkannella.")

else:
    print("Virheellinen hyttiluokka.")