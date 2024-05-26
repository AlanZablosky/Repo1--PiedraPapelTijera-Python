import random

opcion = ["piedra","papel","tijera"]

# Puntuacion
puntuacionPC = 0
puntuacionJugador = 0
def ganadorEs(puntuacionPC, puntuacionJugador):
    if puntuacionPC == 3:
        print("PC Gana")
    if (puntuacionJugador == 3):
        print("Jugador Gana")


# ---Comiendo---
print(" ---Iniciaste el juego --- ")
"""
# Pc elije una papel-tijeras-piedra
pc = random.choice(opcion)

# Jugador ingresa algo
jugador = input("ingrese piedra, papel o tijera: ")

# Si jugador no ingresa una opcion posible, vuelve a preguntar
while (jugador not in opcion):
    print("equivocado")
    jugador = input("ingrese piedra, papel o tijera: ")
"""

# Funciones / Mecanica de juego
while (puntuacionPC != 3 and puntuacionJugador != 3):
    #jugador vuelve a elegir 
        jugador = input("ingrese de nuevo piedra, papel o tijeras: ").lower()
        pc = random.choice(opcion)
        if jugador == pc:
            print("La pc elijio", pc, " y el jugador", jugador, " = Empate")
            
            # Nadie gana puntos
            print(puntuacionJugador, puntuacionPC) 
            
            # Si te equivocas, vuelve a poner
            if (jugador not in opcion):
                print("equivocado")
                jugador = input("ingrese piedra, papel o tijera: ").lower()
        elif (jugador == "piedra" and pc == "tijera") or (jugador == "papel" and pc == "piedra") or (jugador == "tijera" and pc == "papel"):
            print("La pc elijio", pc, " y el jugador", jugador, " = Ganaste")
            
            # Gana jugador
            puntuacionJugador = puntuacionJugador + 1
            print(puntuacionJugador, puntuacionPC)
            ganadorEs(puntuacionPC, puntuacionJugador)
            
            # Si te equivocas, vuelve a poner
            if (jugador not in opcion):
                print("equivocado")
                jugador = input("ingrese piedra, papel o tijera: ").lower()   
        else:
            print("La pc elijio", pc, " y el jugador", jugador, " = Perdiste")
            
            # Gana Pc
            puntuacionPC = puntuacionPC + 1
            print(puntuacionJugador, puntuacionPC)
            ganadorEs(puntuacionPC, puntuacionJugador)
            
            # Si te equivocas, vuelve a poner
            if (jugador not in opcion):
                print("equivocado")
                jugador = input("ingrese piedra, papel o tijera: ").lower() 
print("---Fin del juego---")