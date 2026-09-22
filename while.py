catalog = {
                "piezas1":{
                "id":1,
                "name": "piedras",
                "category": "natural",
                "price": 100,
                "status": "disponible",
                "description": "hermosa pieza certificada disponible"
        },
                "piezas2":{
                "id":2,
                 "name": "coches",
                "category": "juguetes",
                "price": 200,
                "status": "reservada",
                "description": "hermosa pieza usada disponible"
        },
                "piezas3": {
                "id": 3,
                "name": "",
                "category": "",
                "price":0,
                "status": "",
                "description": ""
        },
        "piezas4": {
                "id":4,
                "name": "",
                "category": "",
                "price": 0,
                "status": "",
                "description": ""
        },
        "piezas5": {
                "id": 5,
                "name": "",
                "category": "",
                "price": 0,
                "status": "",
                "description": ""
        },
        "piezas6": {
                "id": 6,
                "name": "",
                "category": "",
                "price":0,
                "status": "",
                "description": ""
        },
        "piezas7": {
                "id": 7,
                "name": "",
                "category": "",
                "price": 0,
                "status": "",
                "description": ""
        },
        "piezas8": {
                "id": 8,
                "name": "",
                "category": "",
                "price": 0,
                "status": "",
                "description": ""

        },
        "piezas9": {
                "id": 9,
                "name": "",
                "category": "",
                "price": 0,
                "status": "",
                "description": ""

        },
        "piezas10": {
                "id": 10,
                "name": "",
                "category": "",
                "price": 0,
                "status": "",
                "description": ""

        }


}

print("***Viejo catalogo***",catalog)
"""
cont = 1
while cont <= recorrido:
    for x, obj in catalog.items():
        print(f"{x} : {catalog[x]}"  )
    cont+=1
"""
recorrido=0
recorrido = int
cont1=1

while cont1 < 3:
                
                recorrido= input("cuantas piezas quieres añadir? Maximo de 10 piezas: ")
                recorrido=int(recorrido)
                if recorrido < 10:
                        cont1= 3
                else:
                        print("Tiene que ser menor de 10 piezas a añadir")
                        cont1+=1

cont2 = 1
while cont2 <= recorrido:
        print("")
        id_piece = input("Ingreso el identificador de la pieza " + str(cont2) + " : ")
        catalog[f"piezas{cont2}"]["id"] = id_piece
        print("")
        nombre = input("ingreso el nombre de la pieza " + str(cont2) + " : ")
        catalog[f"piezas{cont2}"]["name"]=nombre
        print("")
        categot = input("ingreso la categoria " + str(cont2) + " : ")
        catalog[f"piezas{cont2}"]["category"]=categot
        print("")
        price = input("ingreso el precio de la pieza " + str(cont2) + " : ")
        catalog[f"piezas{cont2}"]["price"] = price
        print("")
        while True:
                print("Opciones de las piezas")
                print("1. disponible")
                print("2. reservada")
                print("3. vendida")
                status_piece = input("Solo ingrese una opcion del 1 al 3 de la pieza " + str(cont2) + " : ")
                if status_piece == "1":
                        status_piece = str(status_piece)
                        status_available = status_piece
                        catalog[f"piezas{cont2}"]["status"] = status_available
                        break
                elif status_piece == "2":
                        status_piece = str(status_piece)
                        status_available = status_piece
                        catalog[f"piezas{cont2}"]["status"] = status_available
                        break
                elif status_piece == "3":
                        status_piece = str(status_piece)
                        status_available = status_piece
                        catalog[f"piezas{cont2}"]["status"] = status_available
                        break
                else:
                        print("Opcion invalida, ingrese opcion del 1 al 3")

        print("")
        description_piece = input("ingreso la categoria " + str(cont2) + " : ")
        catalog[f"piezas{cont2}"]["description"] = description_piece
        cont2+=1
print()
print("Catalogo actualizado: ", catalog)


