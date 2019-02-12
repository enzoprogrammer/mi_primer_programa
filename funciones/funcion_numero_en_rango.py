def numero_en_rango(numero_usuario, parametro1, parametro2):
    dentro_del_rango= False
    if numero_usuario >= parametro1 and numero_usuario <= parametro2:
        dentro_del_rango= True
    return dentro_del_rango

print(numero_en_rango(5, 2, 6))
print(numero_en_rango(1, 2, 6))



