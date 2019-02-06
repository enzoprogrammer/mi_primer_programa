lista_numeros= []
numero_usuario= ""

while len(lista_numeros) < 10:
    while not numero_usuario.isdigit():
        numero_usuario=input("Dime un numero: ")
    lista_numeros.append(int(numero_usuario))
    numero_usuario=""
    print("Numero Añadido!")

print(" ")
print(lista_numeros)


numero_grande= lista_numeros[0]

for numero in lista_numeros:
    if numero > numero_grande:
        numero_grande= numero

print(" ")
print("El numero mas grande es {}".format(numero_grande))




