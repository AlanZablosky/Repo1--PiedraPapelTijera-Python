import random

opcion = ["piedra","papel","tijera"]

pc = random.choice(opcion)

jugador = input("ingrese piedra, papel o tijeras: ")

while (jugador not in opcion):
    print("equivocado")
    jugador = input("ingrese piedra, papel o tijeras: ")

if jugador == pc:
    print("La pc elijio", pc, " y el jugador", jugador, " = Empate")
elif (jugador == "piedra" and pc == "tijera") or (jugador == "papel" and pc == "piedra") or (jugador == "tijera" and pc == "papel"):
    print("La pc elijio", pc, " y el jugador", jugador, " = Ganaste")
else:
    print("La pc elijio", pc, " y el jugador", jugador, " = Perdiste")