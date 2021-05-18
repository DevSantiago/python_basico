def main(texto):
    for letra in texto:
        if letra == "o":
            break
        print(letra)


if __name__ == "__main__":
    texto = input(str("Ingresa un texto: "))
    main(texto)