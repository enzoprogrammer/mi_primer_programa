def mayor_entre_3(numero_uno, numero_dos, numero_tres):
    mayor = 0
    if numero_uno > numero_dos and numero_uno > numero_tres:
        mayor = numero_uno
    elif numero_dos > numero_uno and numero_dos > numero_tres:
        mayor = numero_dos
    elif numero_tres > numero_uno and numero_tres > numero_dos:
        mayor = numero_tres

    return mayor

print (mayor_entre_3(1, 2, 3))
print(mayor_entre_3(8, 5, 4))
