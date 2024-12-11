# Scriviamo un programma che chiede all'utente
# di inserire 5 voti di un alunno.
# Bisogna calcolare e scrivere la media dei voti
# e valutare l'alunno con i voti insufficiente,
# sufficiente, buono, molto buono e ottimo a seconda
# della media.

voti = []

for i in range(5):
    voti.append(int(input("Inserisci il voto")))

media = sum(voti)/len(voti)

print("La media dei voti e'", media)

if media >=4.5:
    print("Valutazione: ottimo")
elif media >= 3.5:
    print("Valutazione: molto buono")
elif media >= 2.5:    
    print("Valutazione: buono")
elif media >= 1.5:
    print("Valutazione: sufficiente")
else:
    print("Valutazione: insufficiente")
    
