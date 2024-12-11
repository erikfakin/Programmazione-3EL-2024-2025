# Liste
# Sono enetita' per organizzare un INSIEME di dati
lista = [1, 3, "cane", False, 321.23]

# Per accedere agli elementi della lista si usano gli index
# L'index indica la posizione dell'elemento nella lista
# Il primo elemento ha index 0
print(lista[0])

print(lista[2])

# Posso avere anche index negativi
# Index -1 rappresenta l'ultimo elemento
print(lista[-1])

# Il metodo append aggiunge un elemento alla fine della lista
lista.append("gatto")
print(lista)

# Il metodo insert ci permette di inserire un elemento in un determinato index
lista.insert(1, "topo")
print(lista)

# Il metodo pop si usa per elemininare e ritornare dalla lista un elemento
# in un determinato index. Se non viene scritto l'index, pop elimina
# e ritorna l'ultimo elemento

lista.pop()
print(lista)
elemento_eliminato = lista.pop(1)
print(lista)
print(elemento_eliminato)

# Il metodo remove elimina il primo elemento il cui valore e' uguale
# al parametro passato nella funzione
lista.remove("cane")
print(lista)

# Per sapere quanti elementi contiene la lista utilizziamo len
print(len(lista))

#Slice o fetta della lista dall'index 1 all'index 3 (non compreso)
sublist = lista[1:3]
print(sublist)








