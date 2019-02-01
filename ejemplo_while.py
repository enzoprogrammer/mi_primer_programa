#Ejemplo de contador while

numero_inicial= int(input('Digite un numero: '))
print(" ")
print(" ")
print(numero_inicial)
print(" ")
print(" ")

while numero_inicial > 0:
    print(" ")
    numero_inicial -= 1
    print(numero_inicial)
    print(" ")
    print(" ")

    if numero_inicial % 2 == 0:
        print(" ")
        print('Este numero es par')
        print(" ")
    else:
        print(" ")
        print('Este numero es impar')
        print(" ")
