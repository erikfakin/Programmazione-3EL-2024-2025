# Bubble sort
# Algoritmo di ordinamento piu' semplice

def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                # scambio di posto
                # lista[j] e lista[j+1]
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp


l = [3, 1, 7, -4, 542, 0, 92 , -98]

bubble_sort(l)
print(l)
