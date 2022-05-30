# Od kojeg broja početi i do kojeg doći, uključujući i taj broj
pocetiOd = int(input('? Početi Od: '))
dociDo = int(input('? Doći Do: '))
# Ovdje pratimo ako broj čiji je zbroj znamenaka 10 postoji, tako da možemo ispisati "Nema", ako ga nema
pronadenBroj = False

# For petlja koja ide od početnog do zadnjeg broja (uključujući i njega)
for i in range(pocetiOd, dociDo + 1):
    # Kopija broja kako možemo dobiti zbroj znamenaka
    broj = i
    # Varijabla za zbroj znamenaka
    zbrojZnam = 0

    # Idemo kroz zvaku znamenku i dodajemo na zbroj
    while broj > 0:
        zbrojZnam += broj % 10
        broj //= 10
    
    # Ako je zbroj znamenaka jednak 10, ispišemobroj sa razmakom i zabilježimo da smo našli broj
    if zbrojZnam == 10:
        print(i, end=" ")
        pronadenBroj = True
    
    # Ovaj proes ponavljamo svaki put kada vrtimo petlju
    
if pronadenBroj == False:
    print('Nema')