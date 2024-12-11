#Esercizio

# Scriviamo un programma che chiede all'untente di inserire
# un numero a 2 cifre. Il programma deve scrivere se il numero
# e' divisibile per 3. Se lo e' deve anche scrivere quante
# volte il 3 sta nel numero.

numero = 0

while (numero < 10 and numero > -10) or numero > 99 or numero < -99:
    numero = int(input("Inserisci un numero a due cifre"))

if numero % 3 == 0:
    print("Il numero e' divisibile per 3")
    print("Il 3 sta", numero / 3, "volte nel" numero)
else:
    print("Il numero non e' divisibile per 3")
