# def imprimir_mesaje():
#     print('Mensaje especial: ')
#     print('Estoy aprendiendo a usar funciones')


# for i in range(3):
#     imprimir_mesaje()


def conversacion(opcion):
    print("Hola")
    print("Cómo estás")
    print(opcion)
    print("Adiós")


opcion = int(input("Ingresa la opción(1, 2, 3): "))

if opcion == 1:
    conversacion("Elegiste la opcion {}".format(str(opcion)))
elif opcion == 2:
    conversacion("Elegiste la opcion {}".format(str(opcion)))
elif opcion == 3:
    conversacion("Elegiste la opcion {}".format(str(opcion)))
else:
    print("Escoge una opción valida")