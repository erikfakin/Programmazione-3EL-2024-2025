# Esercizio 1 - Trova il massimo di tre numeri
# Chiedi all'utente di inserire 3 numeri. Crea una
# funzione che ritorna il massimo di 3 numeri e scrivilo
# nella console
#a = int(input("Inserisci il primo numero"))
#b = int(input("Inserisci il secondo numero"))
#c = int(input("Inserisci il terzo numero"))

def trova_massimo(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    elif z >= x and z >= y:
        return z

#massimo = trova_massimo(a, b, c)
#print("Il massimo di", a, b, c, "e':", massimo)


# Esercizio 2 - Numeri dispari fino a N
# Chiedi all'utente di inserire un numero N.
# Crea una funzione che scrive nella console tutti
# i numeri dispari da 1 a N.

def numeri_dispari():
    n = int(input("Scrivi un numero intero positivo: "))
    lista = range(1, n+1, 2)
    for i in range(1, n + 1, 2):
        lista.append(i)
    print(lista)

numeri_dispari()



# Esercizio 3 - Conta vocali
# Chiedi all'utente di inserire una parola.
# Crea poi una funzione che ritorna il numero di vocali nella parola
# e scrivi nella console il risultato.







