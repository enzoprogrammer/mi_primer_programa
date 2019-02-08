numeros=[1, 2, 3, 4, 5, 6, 7, 8, 15, 87, 95, 99]

for indice in range(len(numeros)):
    if numeros[indice]%3== 0 or numeros[indice]%5==0:
        string_reemplazo=""
        if numeros[indice]%3==0:
            string_reemplazo+="Fizz"
        if numeros[indice]%5==0:
            string_reemplazo+="Buzz"

        string_reemplazo=string_reemplazo.replace("FizzBuzz", "Bazinga")

        numeros[indice]=string_reemplazo

print(numeros)

