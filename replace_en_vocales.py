iteraciones= 0
while iteraciones < 5:
    string_usuario = input("Escriba una frase: ")
    string_usuario = string_usuario.replace("a", "i")
    string_usuario = string_usuario.replace("e", "i")
    string_usuario = string_usuario.replace("i", "i")
    string_usuario = string_usuario.replace("o", "i")
    string_usuario = string_usuario.replace("u", "i")
    print(string_usuario)
    iteraciones+=1
