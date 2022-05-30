brojOcjena = int(input('Broj Ocjena: ')) # Unosimo broj ocjena koje treba upisati
ukupanZbrojOcjena = 0 # Ukupan zbroj svih ocjena

# For petlja koja se vrti "brojOcjena" puta
for i in range(brojOcjena):
    # Uzimamo ocjenu
    ocjena = int(input('Upišite Ocjenu: '))
    # Ako je ocjena 1, završavamo program
    if ocjena == 1:
        print('nedovoljan')
        break
    else:
        # Ako je ocjena veća od 1 dodajemo je u ukupan zbroj ocjena
        ukupanZbrojOcjena += ocjena

# Računamo aritmetičku sredinu tako što od ukupnog zbroja djelimo broj ocjena te onda zaorkužujemo broj
aritmetckaSredina = round(ukupanZbrojOcjena / brojOcjena)

# Logika koju koristimo za detektiranje i ispis ocjene
# Napravio bi ovo sa switchevima jel bi bilo puno, puno, puno bolje, ali to još nismo učili tako da se držim na poznatom
if aritmetckaSredina == 2:
    print('dovoljan')
elif aritmetckaSredina == 3:
    print('dobar')
elif aritmetckaSredina == 4:
    print('vrlo dobar')
elif aritmetckaSredina == 5:
    print('odlican')