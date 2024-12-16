# Ricerca lineare - O(n)

# Ritorna l'index del valore cercato.
# Se il valore cercato non si trova nella lista ritorna -1.
def ricerca_lineare(lista, valore):
    for i in range(len(lista)):
        if lista[i] == valore:
            return i

    return -1


numeri = [2, 4, 43, 5, 53, 654, 431]

index_5 =ricerca_lineare(numeri, 5)
if index_5 > -1:
    print("Nella lista c'e' il valore 5 in posizione", index_5)
else:
    print("Nella lista non c'e' il valore 5")


index_9 =ricerca_lineare(numeri, 9)
if index_9 > -1:
    print("Nella lista c'e' il valore 9 in posizione", index_9)
else:
    print("Nella lista non c'e' il valore 9")
