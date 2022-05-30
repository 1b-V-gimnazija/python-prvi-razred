# Unosimo kolicinu brojeva za upisati
kolicinaBrojeva = int(input('? Koliko brojeva treba upisati: ')) # Primjer: 5

# Varijble koje će sadržavati najveći i najmanji broj
najveci = 0
najmanji = 0

# Petlja koja se vrti "kolicinaBrojeva" puta
for i in range(kolicinaBrojeva):

     # Svaki put kada odvrtimo petlju, unosimo novi broj
    trenutacniBroj = int(input('? Upišite broj: '))
    
    # Kada prvi put vrtimo petlju, najmanji broj je trenutačni te onda uspoređujemo brojeve
    if najmanji == 0:
        najmanji = trenutacniBroj

    # Ako je trenutačni broj veći od najvećeg, onda ga stavljamo u varijablu
    if trenutacniBroj > najveci:
        najveci = trenutacniBroj

    # Ako je trenutačni broj manji od najmanjeg, onda ga stavljamo u varijablu
    elif trenutacniBroj < najmanji:
        najmanji = trenutacniBroj

# Ispisujemo najveći i najmanji broj
print('Najveći:', najveci)
print('Najmanji:', najmanji)