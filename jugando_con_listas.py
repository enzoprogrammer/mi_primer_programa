lista_compra= []
productos_a_comprar= input("Que producto desea añadir a la lista de compras? (Si desea finalizar escriba FIN ) ")

while productos_a_comprar != "FIN":
    lista_compra.append(productos_a_comprar)
    productos_a_comprar= input("Que producto desea añadir a la lista de compras? (Si desea finalizar escriba FIN ) ")

for item in lista_compra:
    print("Debes comprar {}" .format(item))

