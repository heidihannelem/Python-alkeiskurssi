luku = int(input("Anna kokonaisluku: "))

if luku % 3 == 0 and luku % 5 == 0:
    print("BoomBuzz")

elif luku % 3 == 0:
    print("Boom")

elif luku % 5 == 0:
    print("Buzz")

else:
    print(luku)

#Tässä tehtävässä tulee huomioida, että ensimmäiseksi tulee laittaa tuo 3 ja 5 yhteinen testaus!