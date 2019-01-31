print("Bienvenido al juego de Combate Pokemon")
print(" ")
print(" ")

pokemon_enemigo_elegido= input("Debes elegir al pokemon contra el cual tu quieres batallar (Charmander / Bulbasaur / Squirtle) :").upper()
danio_enemigo= 0
vida_enemigo= 0
pikachu_vida= 100

if pokemon_enemigo_elegido == "CHARMANDER":
    danio_enemigo= 10
    vida_enemigo= 95
elif pokemon_enemigo_elegido == "BULBASAUR":
    danio_enemigo= 8
    vida_enemigo= 80
elif pokemon_enemigo_elegido == "SQUIRTLE":
    danio_enemigo= 7
    vida_enemigo= 90

while pikachu_vida > 0 and vida_enemigo > 0:
    poder_elegido= input("Que poder quieres usar para atacar? (Chispazo/ Rayo):").upper()
    print(" ")

    if poder_elegido== "CHISPAZO":
        vida_enemigo -=10
        print("~~~~~~ATAQUE CHISPAZO~~~~~~")
    elif poder_elegido== "RAYO":
        vida_enemigo -= 12
        print("~~~~~~ATAQUE RAYO~~~~~~")
    else:
        print("Pierdes un turno por haber escrito mal el poder")

    print(" ")
    print("Se aproxima un ataque de {}" .format(pokemon_enemigo_elegido))
    print(" ")
    pikachu_vida -= danio_enemigo

    print("La vida de Pikachu es de {}" .format(pikachu_vida))
    print(" ")
    print("La vida de {} es de {}" .format(pokemon_enemigo_elegido , vida_enemigo))
    print(" ")

if vida_enemigo <= 0 and pikachu_vida > 0:
    print("Has ganado el combate pokemon")
elif vida_enemigo > 0 and pikachu_vida <=0:
    print("Has perdido el combate pokemon")
else:
    print("Empate")

print(" ")
print("Fin Combate")
