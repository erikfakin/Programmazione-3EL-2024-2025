# Ordinamento per selezione - selection sort

def selection_sort(lista):

    for i in range(0, len(lista)):
        min = i

        # Trovo l'index del valore minimo
        for j in range(i, len(lista)):
            if lista[min] > lista[j]:
                min = j


        # Scambio lista[i] con lista[min]
        temp = lista[i]
        lista[i] = lista[min]
        lista[min] = temp

lista = [5, 1, 23, 17, 99, -4, -909, 1000]
selection_sort(lista)
print(lista)
