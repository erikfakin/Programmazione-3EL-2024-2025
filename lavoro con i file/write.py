# Per scrivere

# Aprire il file

# con il modo "w" sovrascriviamo tutto il file perdendo i contenuti di prima
# con il modo "a" aggiungiamo alla fine di un file esistente, senza perdere
# i contenuti del file
file = open("modri.txt", "a")

# Scrivo nel file
file.write("\n L'auto rossa mi piace!")


for i in range(10):
    file.write(f"\nQuesta e' la riga numero {i}")

lista = [1, 2, 3]
file.write(str(lista))


# Chuido il file
file.close()


