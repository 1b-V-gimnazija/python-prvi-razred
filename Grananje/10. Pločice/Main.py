horizonatlno = int(input('? Horizontalno: '))
vertikalno = int(input('? Vertikalno: '))
velicina = horizonatlno * vertikalno

brojCrvenih = velicina / 2

if brojCrvenih % 2 != 0:
    brojCrvenih += 0.5

brojSivih = velicina - brojCrvenih

print('Broj Crvenih:', round(brojCrvenih))
print('Broj Sivih:', round(brojSivih))