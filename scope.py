#SCOPE
#Lo scope e' la visibilita' delle variabili, cioe' la parte del programma
#in cui possiamo fare riferimento a una variabile.
#Le variabili possono essere "locali" se sono dichiarate all'interno
#di una funzione oppure "globali" se sono dichiarate fuori da una funzione.


#Questa variabile globale sara' accessibile in tutto in modulo.
globale = "Ford"

print("Variabile globale", globale)

def descrivi():
    #Questa variabile locale esiste solo dentro alla funzione stessa
    #non posso accedere alla variabile fuori da questa funzione.
    locale = "FIAT"
    print("Variabile globale in una funzione", globale)
    print("Variabile locale nella funzione", locale)

descrivi()

print("Variabile locale fuori dalla funzione non esiste", locale)

