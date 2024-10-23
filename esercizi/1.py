# Esercizio 1
# Chiedi all'utente di inserire due numeri.
# Se i numeri sono uguali scrivi UGUALI
# altrimenti DIVERSI
print("--------------ESERCIZIO 1-------------")
a = input("Inserisci il primo numero")
b = input("Inserisci il secondo numero")
if a == b:
    print("UGUALI")
else:
    print("DIVERSI")



# Esercizio 2
# Chiedi all'utente di inserire due numeri.
# I due numeri sono i lati di un rettangolo.
# Scrivi all'utente il perimetro e l'area del rettangolo.
# Nota: perimetro = 2*a + 2*b
#       area = a*b
print("--------------ESERCIZIO 2-------------")
a = float(input("Inserisci il primo numero"))
b = float(input("Inserisci il secondo numero"))

perimetro = 2*a + 2*b
area = a*b

print("Perimetro=", perimetro, " Area=", area)


# Esercizio 3
# Chiedi all'utente di inserire un numero.
# Se il numero e' negativo scrivi "negativo"
# altrimenti "positivo".
print("--------------ESERCIZIO 3-------------")
n = int(input("Inserisci un numero:"))
if n < 0:
    print("negativo")
else:
    print("positivo")

