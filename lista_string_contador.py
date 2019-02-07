lista_usuario= []
lista_conteo= []
operar= "SI"

while operar != "NO":
    string_usuario= input("Dime un frase para agregar a mi lista: ")
    lista_usuario.append(string_usuario)
    operar= input("Desea seguir agregando frases? Si/No :").upper()
    if operar != "SI" and operar != "NO":
        operar=input("Por favor escriba si o no! :").upper()

for dato in lista_usuario:
    lista_conteo.append(len(dato))

print(lista_conteo)