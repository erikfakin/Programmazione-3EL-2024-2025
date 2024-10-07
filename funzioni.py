#FUNZIONI
#Le funzioni sono blocchi di codice che esegue un'attivita' specifica.
#Vengono utilizzate per rendere il codice piu' organizzato,
#riutiliozzabile e leggibile.

#Definiamo una funzione
def saluta():
    print("Ciao")

#Chiamiamo la funzione
saluta()

#Dichiarazione di una funzione con parameteri.
#I parametri sono gli input della funzione, ci permettono
#di passare informazioni
def saluta_nome(nome):
    print("Ciao", nome)
nome_utente = input("Scrivi il tuo nome: ")
saluta_nome(nome_utente)


def descrivi_persona(nome, eta, classe):
    print(nome, "ha", eta, "anni e va in", classe, "classe")

#parametri senza nome, seguiamo l'ordine dei parametri
#come definiti su
descrivi_persona("Massimo", 17, "3B")

#Parametri con nome, non centra l'ordine
descrivi_persona(eta=16, classe="3A", nome="Lara")


#Dichiarazione della funzione con valori predefiniti.
#Se non passo gli argomenti, il valore sara' uguale
#ai defaults che ho definito nella funzione
def calcola_volume(a=1, b=1, c=1):
    print("Il volume del parallelepipedo",a,b,c,"e'", a*b*c)

#Se non passo i parametri, il loro valore sara' uguale a 1
#come definito della funzione
calcola_volume()
 
