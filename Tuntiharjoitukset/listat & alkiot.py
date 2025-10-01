# Muuttuja! arvon muuttuja voi olla esim. nimi
# esim. names = ["Viivi", "Ahmed", "Pekka", "Olga", "Mari"]
# V = 0, A = 1, P = 2, O = 3, M = 4 !!! Järjestysnumerot alkavat aina 0, eli 5kpl nimet 0-4

nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mari"]
# names = ["Pertti", "Matti", "Jonna", "Anne", "Tia"] eli voi olla lisäksi toinen lista

print(nimet[2])
# tulostaa siis Pekan nimen, koska hänen järjestysnumero on 2 listassa

print(nimet[-3])
# tulostaa taas Pekan nimen, koska listan lopussa ei ole numeroa 0

print(nimet[1:3])
# tulostaa siis vain järjestysnumero 1 ja koska 3 on lopetuspiste, sitä ei eli Olgaa tulosteta

# len-funktio - listan pituus saadaan haettua
print(len(nimet))

nimet.remove("Pekka")
print(nimet)
# nimet.remove("Pekka") poistaa sen listasta, huomaa että nimien arvoindeksit muuttuu

print(nimet[5])
# tulee virheviesti, koska lista on 0-4