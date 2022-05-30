# Unosimo sve varijable
objekti = int(input('Broj Objekata (N): ')) # Primjer: 39, ovaj broj je N
brojRazlicitih = int(input('Broj Različitih Objekta (K): ')) # Primjer: 7, ovaj broj je K

# Nadalje ćemo koristiti algoritam iz 2. zadataka kako bi dobili dijelove formule. Formulu ćemo razdvojiti na tri dijela i onda ukupan rezultat ispisati.
# Prvi dio forumle je množenje svih brojeva do N, odnsno objekata. U slučaju primjera: 1 * 2 * 3 ... * 39 (N). Kako ovaj algoritam radi možete vidjeti u 2. zadatku (https://github.com/GrifTheDev/peta-python-rijesenja/blob/main/For%20Petlje/2.%20MNo%C5%BEenje%20do%20N/Main.py)

# Petlja koja izvršava gornji zadatak
prviDioFormule = 1

for i in range (1, objekti + 1):
    # Finalni rezultat ovog dijela forumle bit će u varijabli "prviDioFormule"
    prviDioFormule = prviDioFormule * i

# U drugm dijelu formule moramo pomnožiti sve brojeve do K, odnsono broj različitih. U slučaju primjera: 1 * 2 * 3 ... * 7 (K)

drugiDioFormule = 1

# Petlja koja izvršava gornji zadatak
for i in range (1, brojRazlicitih + 1):
    # Finalni rezultat ovog dijela forumle bit će u varijabli "drugiDioFormule"
    drugiDioFormule = drugiDioFormule * i

# U zadnjem djelu formule ćemo pomnožiti sve brojeve do "objekti (N) - brojRazličitih (K)" broja. U ovom slučaju to će biti svi brojevi do 39 - 7, odnsono 32.
# 1 * 2 * 3 ... * 32 (N - K)

treciDioFormule = 1

# Petlja koja izvršava gornji zadatak
for i in range(1, (objekti - brojRazlicitih) + 1):
    # Finalni rezultat ovog dijela forumle bit će u varijabli "treciDioFormule"
    treciDioFormule = treciDioFormule * i

# Sada kada imamo sve djelove formule, moramo ispisati konačan rezultat tj. prvi dio forumle koji je podjeljen sa umnoškom drugog i trećeg dijela formule.
# Kako bi broj izgledao lijepše, cijelu formulu stavljamo u "round()" funckiju kako bi ga zaokružili.
print(round(prviDioFormule / (drugiDioFormule *  treciDioFormule)))

