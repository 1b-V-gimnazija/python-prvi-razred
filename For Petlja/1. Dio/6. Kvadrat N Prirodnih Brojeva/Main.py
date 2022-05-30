broj = int(input('Unesite Broj: ')) # Unosimo broj
ukupanZbrojKvadrata = 0 # Varijabla koja sadrži naš zbroj

# For petlja koja radi dva puta više nego varijabla "broj" te "+1" kako bi uključili dobiveni broj
# To radimo kako bi dobili prvih "broj" parnih brojeva, jer je njih dva puta originalni broj te u nekim slučajevima orignalni broj
for i in range((broj * 2) + 1):
    # Ne želimo da kontrolni broj "i" bude 0
    if i != 0:
        # Provjera djeljivosti kontrolnog broja sa 2 tj. je li kontrolni broj paran
        if i % 2 == 0:
            # Stavljanje kvadrata broja u varijablu zbroja
            ukupanZbrojKvadrata += i * i

# Ispišemo traženi rezultat
print(ukupanZbrojKvadrata)