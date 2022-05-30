# Unos broja
broj = int(input('? Broj: '))

# Broj je potpuno paran (True), dok god ne nađemo snamenku koja nije parna (False)
potpunoParan = True

# While petlja kako bi dobili svaku znamenku broja
while broj > 0:
    # Zadnja Znamenka broja će biti ostatak pri djeljenju sa 10. 23 % 10 = 3
    znamenka = broj % 10
    
    # Ako je znamenka neparna, broj nije potpuno paran
    if znamenka % 2 != 0:
        potpunoParan = False

    # Broju mičemo zadnju znamenku. 234 // 10 = 23
    broj //= 10

# Provjeravamo je li broj potpuno paran ili ne
if potpunoParan == True:
    print('Broj je potpuno paran')
elif potpunoParan == False:
    print('Broj nije potpuno paran')