# koliko brojeva upisati
brojBrojeva = int(input('? Koliko Brojeva: '))
# Koliko brojeva sa prvim i zadnjim nepanim znamenaka ima
brojNeparnihZnam = 0

# For petlja za upisivanje "brojBrojeva" broja.
for i in range(brojBrojeva):
    # Upisujemo broj
    broj = int(input('? Upiši Broj: '))
    # Kopija broja da možemo dobiti broj znamenaka
    kopijaBroja = broj
    brojZnamenaka = 0

    # While petlja koja broji broj znamenaka
    while kopijaBroja > 0:
        brojZnamenaka += 1
        kopijaBroja //= 10
    
    # Broj znamenaka treba smanjiti za idući korak
    brojZnamenaka -= 1
    # Prvu znamenku dobijemo tako što broj podjelima sa 10 ^ brojZnamenaka bez ostatka, npr. 2345 // 10 ^ 3 = 2
    prvaZnamenka = broj // (10 ** brojZnamenaka)
    # Zadnju znamenku dobijemo tako štp broj podjelima sa 10 i uzmemo ostatak
    zadnjaZnamenka = broj % 10

    # Ako su i prva i zadnja znamenka ne prane, dodajemo na brojač brojeva sa prvim i zadnjim ne pranim brojevima
    if prvaZnamenka % 2 != 0 and zadnjaZnamenka % 2 != 0:
        brojNeparnihZnam += 1

print(brojNeparnihZnam)