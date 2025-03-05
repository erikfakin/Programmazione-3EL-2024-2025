# Apertura di un file
file = open("testo.txt")

# Leggiamo il contenuto
# readlines mi ritorna una lista di righe
# contenuto = file.readlines()

# per leggere riga per riga usiamo
# file.readline()


contenuto = file.read()
print(contenuto)
