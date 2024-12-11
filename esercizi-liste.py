# Facciamo un programma che chiede all'utente
# di inserire le temperature misurate in 10 giorni

temperature = []

for i in range(10):
    temp = float(input("Inserisci la temperatura " + str(i + 1) + ": "))
    temperature.append(temp)

print(temperature)

# Adesso scriviamo la minima
# temperatura registrata

print("La temperatura minima e'",min(temperature))

# Adesso scriviamo la massima
# temperatura registrata
print("La temperatura massima e'",max(temperature))

# Adesso scriviamo la media delle 
# temperature registrate
print("La temperatura media e'", sum(temperature) / len(temperature))

# Ho un sensore in classe che mi misura le temperature.
# Come posso controllare se il sensore funziona bene?
# Posso controllare il valore letto dal sensore circa tra 10 e 30 gradi
# Se la temperatura e' sotto i 10 o spra i 30 probabilmente c'e' un problema.

if max(temperature) > 30:
    print("PROBLEMA COL SENSORE")
elif min(temperature) < 10:
    print("PROBLEMA COL SENSORE")







    
