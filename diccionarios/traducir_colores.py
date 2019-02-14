colores= {"amarillo": "Yellow",
          "azul": "Blue",
          "rojo": "Red",
          "celeste": "Light Blue",
          "verde": "Green",
          "negro": "Black",
          "blanco": "White",
          "violeta": "Violet",
          "gris": "Grey"}

salida= False

while not salida:
    color= input("Que color desea ver su traduccion? :").lower()
    print("Traduccion: {}".format(colores[color]))
    operar= input("Desea seguir operando? [Si/ No]:").upper()
    if operar== "NO":
        salida= True
