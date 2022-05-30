# Varijabla broj je do kojeg broja želimo možiti
broj = int(input("Broj: "))
rezultat = 1 # U varijabli rezultat ćemo držati rezultat množenja, sama po sebi je 1.

# For petlja koja se vrti od 1, do broja (odnosno broj+1). Dakle 1, 2, 3, 4, 5 ako je varijabla broj jednaka 5.
for i in range (1, broj +1):
    # Svako vrćenje petlje rezultat je jednak trenutačnom rezultatu puta i, odnosno broju do kojeg smo došli.
    # Ako je broj 5 onda je to, 1 * 1, 1 * 2, 2 * 3, 6 * 4, 24 * 5 = 120
    rezultat = rezultat * i

# Ispisujemo rezultat
print(rezultat)
