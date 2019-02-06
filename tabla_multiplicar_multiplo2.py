#Programa tabla de multiplicar que solo imprime multiplos de 2

tabla_multiplicar= int(input("Que tabla de multiplicar desea? : "))
print(" ")

for multiplo in range(1, 11):
    resultado= tabla_multiplicar*multiplo
    if resultado%2 ==0:
        print("{} x {} = {}".format(tabla_multiplicar, multiplo, resultado))

