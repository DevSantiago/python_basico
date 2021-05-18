import random

def run(numero_elegido):
    numero_elegido =  numero_elegido
    numero_aleatorio = random.randint(1, 100)
    contador = 1

    while numero_elegido != numero_aleatorio and contador <= 5:
        if numero_elegido < numero_aleatorio: 
          print("Vas en el intento " + str(contador))
          print("")
          print("Escoge un número más grande")
          contador += 1
        elif contador == 5:
            print("Perdiste :(")
        else:
            print("Vas en el intento " + str(contador))
            print("")
            print("Escoge un número más pequeño")
            contador += 1

        numero_elegido = int(input("Elige otro número: "))

    print("¡Ganaste!")          


if __name__ == "__main__":
    bienvenida = """Tienes 5 intentos para ganar """
    numero_elegido = int(input("Ingresa el número: "))
    print("")
    run(numero_elegido)