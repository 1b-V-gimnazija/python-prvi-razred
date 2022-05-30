n = int(input())
a = 1
b = 0
for i in range(0, n): #petlja se izvršava n puta
    print(a, end = " ") #ispisuje se vrijednost varijable a
    c = a #c je jednak a
    a += b #a se povećava za b
    b = c #varijabla b postaje jednaka c, odnosno, varijabli a prije nego što joj se dodala varijabla b
