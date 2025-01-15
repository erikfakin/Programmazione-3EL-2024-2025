# Ricerca binaria
# Algoritmo di ricerca
import time
import random

def ricerca_binaria(lista, valore):
    inizio = 0
    fine = len(lista) - 1
    while inizio <= fine:
        medio = (inizio + fine) // 2

        # Se trovo il valore cercato ritno il suo index
        if lista[medio] == valore:
            return medio
        elif lista[medio] < valore:
            inizio = medio + 1
        else:
            fine = medio - 1

            
    # Se non ho trovato il valore cercato ritnorno -1
    return -1


lista = [random.randint(1, 1000000000) for i in range(10000000)]
lista.sort()
elemento_da_cercare = 13
tempo_start = time.time()
index_elemento = ricerca_binaria(lista, elemento_da_cercare)
tempo_end = time.time()

print("Tempo", tempo_end - tempo_start)
print(index_elemento)
