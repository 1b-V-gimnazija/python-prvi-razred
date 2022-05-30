prviBrojNiza = int(input('Prvi Broj Niza: ')) # Unosimo prvi broj u nizu
drugiBrojNiza = int(input('Drugi Broj Niza: ')) # Unosimo drugi broj u nizu
velicinaNiza = int(input('Veličina Niza: ')) # Unosimo velicinu niza
brojUNizu = prviBrojNiza # Na ovu varijablu nadodajemo razliku niza kako bi dobili slijedeći broj za ispis, na početku je jednaka prvom broju niza

# Za koliko treba povećati brojeve u nizu
razlikaNiza = drugiBrojNiza - prviBrojNiza

# For petlja vrti se onliko puta koliko želimo ispisati niz
for i in range(velicinaNiza):
    # Ako je i 0, to znači da počnijemo sa nizom pa možemo ispisati prvi broj
    if i == 0:
        print(prviBrojNiza)
        # Nadodajemo razliku niza u varijablu za ispis pri sljedećem vrćenju petlje
        brojUNizu += razlikaNiza
    else:
        # U svim ostalim slučajevima ispisujemo sljedeći broj u nizu i nadodajemo razliku varijabli u kojoj pratimo brojeve u nizu
        print(brojUNizu)
        brojUNizu += razlikaNiza
