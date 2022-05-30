# Unos broja
broj = int(input('? Broj: '))

# Varijabla koja drži broj znamenka nekog broja
brojZnamenaka = 0
# Kopija broja potrebna da izbrojimo broj znamenaka
kopijaBroja = broj

# While petlja koja nam daje broj znamenaka, svaki put kada se izvrti znamo da ima +1 znamenku
while kopijaBroja > 0:
    kopijaBroja //= 10
    brojZnamenaka += 1

# Provjeravanje ima li broj paran broj znamenaka ili ne
if brojZnamenaka % 2 == 0:
    # Koliko brojeva sa desno na lijevo moramo čuvati, ako je broj 2345, maknuti će biti 3 zato što nam treba samo 345, odnsono
    # miče prvih X brojeva do sredine
    maknuti = int(brojZnamenaka / 2 - 1) + 2
    # Dobit ćemo srednju znamenku tako da maknemo prvih "maknuti" brojeva (to radimo tako što djelima broj sa 10 na "maknuti"),
    # dakle od 2345, dobijemo 345 zatim tom broju maknemo zadnjih X znamenaka gdje je X = broju znamenaka podjeljeno 2
    # i minus jedan. U ovom slučaju 4 podjeleno 2 minus 1. Finalna formula će biti: 345 // 10 ^ 1 = 34
    print(broj % (10 ** maknuti) // (10 ** (int(brojZnamenaka / 2 - 1))))
elif brojZnamenaka % 2 != 0:
    #Koliko brojeva sa desno na lijevo moramo čuvati, akoje broj 34567, maknuti će 3 zato što nam treba 567, odnsno miče prvih
    # X brojeva do sredine
    maknuti = int(brojZnamenaka // 2) + 1
    # Dobit ćemo srednju znamenku tko da sa lijeve strane na desnu maknemo "maknuti" brojeva, 
    # odnosno podjelimo broj sa: 10 na "maknuti" da dobijemo ostatak, odnosno broj bez prvih "maknuti" brojeva, 
    # ako je broj 34567, dobit ćemo 567, zatim moramo maknuti zadnjih "maknuti" brojeva, 
    # odnsono podjeliti broj sa 10 na brojZnamenaka podjeljeno sa 2 bez ostatka. Finalni račun bit će: 567 // 10 ^ 2 = 5
    print(broj % (10 ** maknuti) // (10 ** (int(brojZnamenaka // 2))))