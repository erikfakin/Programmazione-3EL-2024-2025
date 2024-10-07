import random

#I CICLI
#Ci permettono di eseguire ripetutamente un blocco
#di codice finche' una condizione e' soddisfatta.

#while

i = 0
while i<=5:
    print("Ciclo while", i)
    i +=2

numero = random.randint(1, 10)
trovato = False
while not trovato:
    num = int(input("Indovina il numero da 1 a 10: "))
    if num == numero:
        trovato = True

print("Hai indovinato il numero. Il numero era", numero)

    
#for in range
for r in range(0, 5):
    print("Ciclo for", r)


#for con le liste
persone = ["Alberto", "Boris", "Claudio", "Denis", "Encrico"]
for persona in persone:
    print("Ciclo for", persona)
