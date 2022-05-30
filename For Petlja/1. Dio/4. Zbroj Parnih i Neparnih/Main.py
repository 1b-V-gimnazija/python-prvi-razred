# Unosimo kolicinu brojeva za upisati
kolicinaBrojeva = int(input('? Koliko brojeva treba upisati: ')) # Primjer: 5

# Varijble koje će sadržavati zbroj svih parnih i neparnih brojeva
zbrojParnih = 0
zbrojNeParnih = 0

# Petlja koja se vrti "kolicinaBrojeva" puta
for i in range(kolicinaBrojeva):

    # Svaki put kada odvrtimo petlju, unosimo novi broj
    trenutacniBroj = int(input('? Upišite broj: '))

    # Provjeravamo je li broj dijeliv sa 2, odnsno je li paran ili nije.
    if trenutacniBroj % 2 == 0:
        # Ako je broj paran, upisujemo ga u varijablu zbroja parnih brojeva
        zbrojParnih += trenutacniBroj
    elif trenutacniBroj % 2 != 0: # ovdje sam odličio koristiti "elif", umjesto "else" zato što je moguće da korištenje else-a dovede do bugova.
        # Ako je broj neparan, upisujemo ga u varijablu zbroja neparnih brojeva
        zbrojNeParnih += trenutacniBroj

# Na kraju, ispisujemo zbroj parnih i neparnih brojeva
print('Zbroj parnih:', zbrojParnih)
print('Zbroj neparnih:', zbrojNeParnih)