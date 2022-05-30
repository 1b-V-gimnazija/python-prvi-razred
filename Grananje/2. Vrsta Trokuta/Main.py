# Upisujemo stranice trokuta
stranicaA = int(input('Stranica A: '))
stranicaB = int(input('Stranica B: '))
stranicaC = int(input('Stranica C: '))

# If statement u kojem provjeravamo vrstu trokuta
if stranicaA == stranicaB == stranicaC:
    print('Jednakostraničan')
elif stranicaA == stranicaB or stranicaC == stranicaB or stranicaA == stranicaC:
    print('Jednakokračan')
else:
    print('Raznostraničan')