#CONDIZIONALI

#il construtto if consente di eseguire blocchi
#di codice solo se una condizione e' vera

#con la funzione input chiediamo all'utente di inserire il numero
#la funzione int ci converte i valori in numeri interi
x = int(input("Inserisci il numero: "))

if x<10:
    print("Il numero e' minore di 10")


#if-else
#se la condizione non e' vera eseguisce il blocco di codice nel else

if x<0:
    print("il numero e' negativo")
else:
    print("il numero e' positivo")

