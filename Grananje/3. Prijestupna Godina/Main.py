# Unosimo godinu i stavljamo je u varijablu
godina = int(input('? Godina: '))

# Provjeravamo ako je godina djeljiva s 4, ali nije djeljiva sa 100 ili ako je godina djeljiva sa 100
if godina % 4 == 0 and godina % 100 != 0 or godina % 400 == 0:
    print('Prijestupna') # Ispisujemo da je godina prijestupna
else:
    print('Nije prijestupna') # U svim ostalim slučajveima godina nije prijestupna