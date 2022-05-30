# Unosimo sve podatke 
prviBroj = int(input('? Prvi Broj: '))
drugiBroj = int(input('? Drugi Broj: '))
operator = input('? Operator: ')

# Po tome koji je operator korišten radimo tu matematičku radnju te ispisujemo rezultat
if operator == '+':
    print(prviBroj + drugiBroj)
elif operator == '-':
    print(prviBroj - drugiBroj)
elif operator == '/':
    print(prviBroj / drugiBroj)
elif operator == '*':
    print(prviBroj * drugiBroj)