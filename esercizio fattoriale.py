#Esercizio 1
#Scrivi una funzione chiamata fattoriale che mi ritorna il fattoriale
#del numero passato come parametro

#Ad es.
#   risultato = fattoriale(5)
#   print("Fattoriale di 5 e'", risultato)
#   mi scrivera "Fattoriale di 5 e' 120

#Il fattoriale di un numero e il prodotto dei numeri
#interi minori e uguali al numero.
#Ad esempio il fattoriale di 5 e' 5 * 4 * 3 * 2 * 1

def fattoriale(num):
    risultato = 1
    for i in range(1, num + 1):
        risultato = risultato * i
    return risultato

risultato = fattoriale(5)
print("Fattoriale di 5 e'", risultato)

risultato2 = fattoriale(10)
print("Fattoriale di 10 e'", risultato2)

risultato3 = fattoriale(52)
print("Le combinazioni in mazzo di carte sono", risultato3)


