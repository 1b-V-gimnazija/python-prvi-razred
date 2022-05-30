# Ovaj zadatak se vrti oko (nama poznate) ASCII tablice. Kako bi mogli ispisati sva velika slove engleske abecede moramo znati ASCII broj prvog velikog slova (A) i zadnjeg (Z)
# ASCII broj slova A je 65, a slova Z 90. Kada znamo to, fali nam još i char funckcija. Char funkcija će isprinatati slovo kojem pripdada ASCII broj koji mu damo.
# Ako napišemo char(65), on će ispisati A. Sa ovim znanjem možemo napraviti program koji riješava problem.

# For petlja koja se vrti od slova A do slova Z (Z je 90, ali python ne uključuje zadnji broj u petlji, tako da smo stavili 91), odnosno od 65 do 91
for i in range(65, 91):
    # Zatim, samo ispišmo solvo pomoću char() funkcije, u koju upisujemo "i", odnosno trenutačni broj u petlji.
    # Char funkcija će pomoću toga ispisati broj, a dva mjesta razmaka smo napravili pomoću end parametra.
    print(chr(i), end="  ")
