nombre = "Santiago"

print("Slice con incio y final de captura")
slice_uno = nombre[0:3]
print("La cadena es: {} y el slice es {} ".format(nombre, slice_uno))

print("")

print("Slice con incio, final de captura y saltos en la cadena")
slice_dos = nombre[0:7:2]
print("La cadena es: {} y el slice es {} ".format(nombre, slice_dos))

print("")

print("Slice con incio sin valor y final ")
slice_tres = nombre[:6]
print("La cadena es: {} y el slice es {} ".format(nombre, slice_tres))

print("")

print("Slice con incio y sin valor final ")
slice_cuatro = nombre[0:]
print("La cadena es: {} y el slice es {} ".format(nombre, slice_cuatro))

print("")

print("Slice con incio, sin valor final y con valor de saltos en la cadena ")
slice_cinco = nombre[1::3]
print("La cadena es: {} y el slice es {} ".format(nombre, slice_cinco))

print("")

print("Slice que retorna la cadena al revés")
slice_seis = nombre[::-1]
print("La cadena es: {} y el slice es {} ".format(nombre, slice_seis))