tabla_multiplicar= int(input("Que tabla de multiplicar deseas? : "))

for multiplo in range(1,11):
    print("{} x {} = {}".format(tabla_multiplicar, multiplo, tabla_multiplicar * multiplo))
