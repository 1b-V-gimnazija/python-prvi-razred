# !!! OVAJ ZADATAK MOŽE SE RIJEŠITI I SA LISTAMA !!!

broj = int(input('Unesite Broj: ')) # Unosimo broj
zbrojDjeljitelja = 0 # U ovu varijablu ćemo zbrajati sve djeljitelje

# For petlja koja se vrti onliko puta koliki nam je broj
for i in range(broj):
    # "i" je jednak trenutačnom broju, ne može biti viši od varijable "broj"

    # Provjeravamo da i nije 0
    if i != 0:
        # Ako naš broj, podjeljen sa i ima 0 ostatka onda mu je to dijeljitelj.
        if broj % i == 0:
            # Dodavamo djeljitelj, odnsno "i" u varijablu "zbrojDjeljitelja"
            zbrojDjeljitelja += i
    
# Provjeravam ako je naš broj i zbroj djeljitelja isti te po tome ispisujemo rečenice.
if zbrojDjeljitelja == broj:
    print('Broj je savršen')
else:
    print('Broj nije savršen')
