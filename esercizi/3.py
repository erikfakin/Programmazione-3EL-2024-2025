# Esercizio 1 - Trova il massimo di tre numeri
# Chiedi all'utente di inserire 3 numeri. Crea una
# funzione che ritorna il massimo di 3 numeri e scrivilo
# nella console
a = int(input("Inserisci il primo numero"))
b = int(input("Inserisci il secondo numero"))
c = int(input("Inserisci il terzo numero"))

def trova_massimo(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    elif z >= x and z >= y:
        return z

massimo = trova_massimo(a, b, c)
print("Il massimo di", a, b, c, "e':", massimo)


# Esercizio 2 - Numeri dispari fino a N
# Chiedi all'utente di inserire un numero N.
#Crea una funzione che scrive nella console tutti
# i numeri dispari da 1 a N. L'utente deve inserire N.


# Esercizio 3 - COnta vocalo
# Chiedi all'utente di inserire una parola.
# Crea poi una funzione che ritorna il nuermo di vocali nella parola
# e scrivi nella console il risultato.
