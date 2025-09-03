raha = float(input("Anna käytettävissä oleva rahamääräsi: "))

if raha >= 5:
    print("Voit ostaa kahvin.")

if raha < 5:
    print("Ei riitä kahviin.")

print("Kiitos ja hei!")


pituus = int(input("Kuinka pitkä olet? "))

if 170 <= pituus < 180:
    print("Oletpa pitkä!")

koira = input("Mikä koiran nimi on? ").lower()
kissa = input("Mikä kissan nimi on? ").lower()
#lower muuttaa kaikki kirjaimet pieniksi vaikka käyttäjä kirjoittaisi isolla (esim. MUSTI tai muSTI)
if koira == kissa:
    print("Oho, sama nimi!")


a = True
b = False

if a and b:
    print("Molemmat on totta")

if a or b:
    print("Molemmat tai toinen on totta")

if not a and b:
    print("Kumpikaan ei ole totta")