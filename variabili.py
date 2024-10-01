
#Definizione di variabili
nome = "Marco" # nome e' una stringa
eta = 18 #eta e' un numero

#Uso di variabili

print("Questo e' il nome", nome)

nome = "Mario"

print("Ho cambiato il nome:", nome)

#il nome delle variabili deve iniziare
#o con una lettera o con _
variabile1 = 1
_variabile = 2

#il nome della variabile non puo' 
#iniziare con un numero
#questo mi da un errore!
#1variabile = 0

#TIPI DI VARIABILI

#stringa
marca = "Ford"
print("Il tipo di variabile della marca e'",
      type(marca))

#integer (numeri interi)
anno_di_produzione = 2020
print("Il tipo di variabile della anno_di_produzione e'",
      type(anno_di_produzione))


#float (numeri decimali)
cilindrata = 1.9
print("Il tipo di variabile della cilindrata e'",
      type(cilindrata))


#boolean (booleani - True o false)
registrata = True
print("Il tipo di variabile della registrata e'",
      type(registrata))


#liste - possono contenere piu valori
propietari = ["Mario", "Giovanni", "Franco"]
print("Il tipo di variabile della proprietari e'",
      type(propietari))

#per accedere ai valori nelle liste usiamo gli index (indici)
#le liste iniziano con lo index 0
print("Il primo propietario era", propietari[0])
print("Il secondo propietario era", propietari[1])

#per accedere all'ultimo elemento uso l'index -1
print("L'ultimo propietario e'", propietari[-1])

#dizionari

persona = {"nome":"Marco",
           "eta": 17,
           "classe": "3a"}
print("Il tipo di variabile della persona e'", type(persona))

#per accedere alla proprieta' nome della persona
print("Il nome della persona e'",
      persona["nome"])

#tuple - come le liste ma immutabili, non possiamo
#cambiare i valori una volta definite
temperature = (28, 52, 88)

print("Il tipo di variabile delle temperature e'", type(temperature))

#per accedere ai valori delle tuple si usano gli index (come per le liste)
print("Temperatura al primo posto", temperature[0])















