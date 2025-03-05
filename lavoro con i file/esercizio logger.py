# Esercizio logger

import datetime
import random

import keyboard


file = open("log.txt", "a")

current_time = datetime.datetime.now()

file.write(f"{current_time} - programma aperto \n")

while True:

    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        file.write(f"{event.name}")
    


current_time = datetime.datetime.now()
file.write(f"{current_time} - programma chiuso \n")

file.close()
