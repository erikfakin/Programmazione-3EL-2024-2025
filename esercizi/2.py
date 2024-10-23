# ESERCIZIO 1
# Chiedi all'utente di inserire tre numeri
# Se tutti i numeri sono iguali scrivi "uguali"
# Se due numeri sono uguali scrivi "due numeri uguali"
# altrimenti scrivi "diversi"
print("-----------------ESERCIZIO 1----------------")
a = input("Inserisci il primo numero: ")
b = input("Inserisci il secondo numero: ")
c = input("Inserisci il terzo numero: ")

if a == b == c:
    print("uguali")
elif a==b or a==c or b==c:
    print("due numeri uguali")
else:
    print("diversi")

# ESERCIZIO 2
# Chiedi all'utente di inserire un numero.
# Se il numero e' minore di 5 scrivi "basso"
# se il numero e' maggiore o uguale a 5 e minore di 10 scrivi "medio"
# se il numero e' maggiore o uguale a 10 scrivi "alto"

print("-----------------ESERCIZIO 2----------------")
s = int(input("Inserisci il numero: "))
if s < 5:
    print("basso")
elif s >= 5 and s<10:
    print("medio")
else:
    print("alto")





