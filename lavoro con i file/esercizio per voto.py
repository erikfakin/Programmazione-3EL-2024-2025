# Esercizio:

# Crea un file in python chiamato numeri.txt nel quale scrivi
# su ogni nuova riga tutti i numeri da 1 a 1000.
# Poi alla fine scrivi la somma di tutti i numeri.

# output aspettato:
# 1
# 2
# 3
# ...
# 1000
# somma = somma di tutti i numeri da 1 a 1000

# Leggi poi il file e scrivi sullo schermo il contenuto del file

file = open("numeri.txt", "w")

somma = 0

for i in range(1, 1001):
    file.write(f"{i} \n")
    somma = somma + i
    
file.write(f"somma = {somma}")
file.close()

file = open("numeri.txt","r")
contenuto = file.read()
print(contenuto)


