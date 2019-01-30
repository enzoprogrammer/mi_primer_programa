#Ejemplo de contador while

numero_inicial= int(input('Digite un numero'))
print(numero_inicial)

while numero_inicial > 0:
    numero_inicial -= 1
    print(numero_inicial)

    if numero_inicial % 2 == 0:
        print('Este numero es par')
    else:
        print('Este numero es impar')