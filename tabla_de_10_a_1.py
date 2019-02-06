tabla_multiplicar= int(input("Que tabla de multiplicar desea? : "))
lista_multiplos= [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for multiplos in lista_multiplos:
    print("{} x {} = {}".format(tabla_multiplicar, multiplos, tabla_multiplicar*multiplos))
