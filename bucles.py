def run(numero, exponencial):
    contador = 1
    LIMITE = 10000

    operacion = numero ** exponencial
    while operacion < LIMITE:
        operacion = numero ** exponencial
        contador += 1
        numero += 1
        print(operacion)

    return ""
 

if __name__ == "__main__":
    exponencial = int(input("Ingresa la exponencia: "))
    numero = int(input("Ingrese el número donde se empezará a calcular la exponencia: "))

    run(numero, exponencial)