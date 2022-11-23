import os
#Colores
def prRed(skk): print("\033[91m{}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m{}\033[00m".format(skk))
def prYellow(skk): print("\033[93m{}\033[00m".format(skk))
def prLightPurple(skk): print("\033[94m{}\033[00m".format(skk))
def prPurple(skk): print("\033[95m{}\033[00m".format(skk))
def prCyan(skk): print("\033[96m{}\033[00m".format(skk))
def prLightGray(skk): print("\033[97m{}\033[00m".format(skk))
def prBlack(skk): print("\033[98m{}\033[00m".format(skk))

######
os.system('cls')
pokestore = [
    {
    "Producto": "PokeBall",
    "Precio": 200
    },
    {
    "Producto": "SuperBall",
    "Precio": 600
    },
    {
    "Producto": "UltraBall",
    "Precio": 800
    },
    {
    "Producto": "Poción",
    "Precio": 300
    },
    {
    "Producto": "SuperPoción",
    "Precio": 700
    },
    {
    "Producto": "UltraPoción",
    "Precio": 1500
    },
    {
    "Producto": "Poción Máxima",
    "Precio": 2500
    },
    {
    "Producto": "Restaurar Todo",
    "Precio": 3000
    },
    {
    "Producto": "Antídoto",
    "Precio": 200
    },
    {
    "Producto": "Antiparalizante",
    "Precio": 200
    },
    {
    "Producto": "Despertar",
    "Precio": 200
    },
    {
    "Producto": "Antiquemaduras",
    "Precio": 200
    },
    {
    "Producto": "Antihielo",
    "Precio": 200
    },
    {
    "Producto": "Cura_Total",
    "Precio": 600
    }
]

prCyan('\n¡Bienvenid@ a la PokeTienda!')
prRed("----------------------------------------------------------")
print('Productos: ')
for element in pokestore:
    print(f'{element["Producto"]}: {element["Precio"]}')


prRed("----------------------------------------------------------")
productos_a_mostrar = []
precio_a_producto = []
print()
while True:
    usr_input = input("Seleccione un producto que desea comprar, si no quieres seguir comprando (exit): ")
    if usr_input == "exit":
        break
    usr_input_split = usr_input.split()

    for item in pokestore:
        if usr_input_split[1] == item["Producto"]:
            productos_a_mostrar.append("El precio de {} {} es {}$".format(usr_input_split[0],item["Producto"],item["Precio"] * int(usr_input_split[0])))
            precio_a_producto.append(item["Precio"] * int(usr_input_split[0]))

for producto in productos_a_mostrar:
    print(producto)

prGreen("El precio total es : {}$".format(sum(precio_a_producto)))