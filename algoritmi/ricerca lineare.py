# Ricerca lineare - O(n)

# Ritorna l'index del valore cercato.
# Se il valore cercato non si trova nella lista ritorna -1.

import time
import random


def ricerca_lineare(lista, valore):
    for i in range(len(lista)):
        if lista[i] == valore:
            return i

    return -1



lista = [random.randint(1, 10000000000) for i in range(1000000)]

elemento_da_cercare = 13

tempo_start = time.time()
index_elemento = ricerca_lineare(lista, elemento_da_cercare)
tempo_end = time.time()

print("Tempo", tempo_end - tempo_start)
print(index_elemento)
