# Esercizio
# Scriviamo un programma che chiede all'untente
# di inserire 5 numeri e scrive il minimo, il massimo e la differenza
# tra il minimo e il massimo

numeri = []

for i in range(5):
    numeri.append(float(input("Inserisci il numero")))

print("Il massimo e'", max(numeri))
print("Il minimo e'", min(numeri))

print("La differenza tra min e max", max(numeri)-min(numeri))
