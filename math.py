# Modulo math

import math

# Esercizio 1
print("______Esercizio 1________")


# Calcolo della potenza reale in un circuito AC

# P = U x I x cos(phi)

U = 230     # in volt
I = 10      # in ampere
phi = 45    # in gradi

# math.radians ci da l'angolo in radiani da un angolo in gradi
phi_rad = math.radians(phi)
# la funzione coseno prende l'angolo in radiani
P = U * I * math.cos(phi_rad)

print("Potenza reale:", P)

# Esercizio 2
print("______Esercizio 2________")
# Calcolo della frequenza di risonanza in un circuito RLC

# f = 1 / (2 * pi * radice(L * C))

# L - induttanza in Fenry
# C - capacita di Farad

L = 0.1     # induttanza in Henry
C = 1e-6    # capacita in Farad

f = 1 / (2 * math.pi * math.sqrt(L * C))
print("Frequenza di risonanza", f)











