# Esercizio numero pari o dispari
# Scrivi una funzione che prende in input un numero
# e ritorna "pari" se il numero e' pari, altrimenti "dispari"

# se un numero e' pari non ha resto nella divisione col 2.
# in python abbiamo un operatore che ci da il resto %

def pari_o_dispari(numero):
    if numero%2 == 0:
        return "pari"
    else:
        return "dispari"
        
#Test
print("TEST")   
print("Il numero 4 e'", pari_o_dispari(4))
print("Il numero 9 e'",pari_o_dispari(9))



# Esercizio calcolatrice
# Scrivi una funzione che chiede all'utente due numeri e
# un simbolo che descrive l'operazione da fare.
# La funzione ci scrivera' il risultato dell'operazione.

def calcolatrice():
    primo = int(input("Scrivi il primo numero: "))
    secondo = int(input("Scrivi il secondo numero: "))
    operazione = input("Scrivi l'operazione desiderata (+, -, *, /): ")

    if operazione == "+":
        print("La somma dei numeri", primo, secondo, "e'", primo + secondo)
    elif operazione == "-":
        print("La differenza dei numeri", primo, secondo, "e'", primo - secondo)
    elif operazione == "*":
        print("Il prodotto dei numeri", primo, secondo, "e'", primo * secondo)
    elif operazione == "/":
        print("Il quoziente dei numeri", primo, secondo,"e'", primo / secondo)

calcolatrice()


# Esercizio media aritmetica
# Scrivi una funzione che chiede all'utente di inserire numeri.
# Quando l'utente inserisce la parola "fine" voglio ritornare
# la media aritmetica dei numeri.

def media_aritmetica():
    finito = False
    totale = 0
    quantita = 0
    while finito == False:
        utente = input("Inserisci un numero o la parola fine: ")
        if utente == "fine":
            finito = True
        #isnumeric mi ritorna True se l'utente ha inserito un numero
        elif utente.isnumeric():
            totale = totale + int(utente)
            quantita = quantita + 1

    if quantita == 0:
        return 0
    else:
        return totale / quantita

media = media_aritmetica()
print("Media aritmetica = ", media)












