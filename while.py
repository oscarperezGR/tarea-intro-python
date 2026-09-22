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
print()
print("*"* 40)
print("Bienvenido o Bienvenida para al sistema de registro de pieza")
print("Usted esta ingresando al catálogo de piezas coleccionables")
print("*"* 40)
print("***Catalogo Actual***",catalog)

recorrido=0
recorrido = int
cont1=1
while True:
        if cont1 == 4:
                print("Cerrando programa")
                exit()
        else:
                recorrido= input("¿Cuantas piezas quieres añadir? *Maximo de 10 piezas*: ")
                recorrido=int(recorrido)
                if      recorrido <= 10:
                        break
                elif recorrido > 10 or recorrido < 0:
                        (print("Tiene que ser menor de 10 piezas a añadir"))
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

        while True:
                price = input("Ingrese el precio de la pieza " + str(cont2) + " : ")

                try:
                        price = int(price)
                        if price > 0:
                                catalog[f"piezas{cont2}"]["price"] = price
                                print()
                                break
                        else:
                                print("***El precio debe ser mayor a cero***")
                except:
                        print("***Ingrese un precio válido***")
        while True:
                print("Opciones de las piezas")
                print("1. disponible")
                print("2. reservada")
                print("3. vendida")
                status_piece = input("Solo ingrese una opcion del 1 al 3 de la pieza " + str(cont2) + " : ")
                if status_piece == "1":
                        status_piece = str(status_piece)
                        status_available = "disponible"
                        catalog[f"piezas{cont2}"]["status"] = status_available
                        break
                elif status_piece == "2":
                        status_piece = str(status_piece)
                        status_available = "reservada"
                        catalog[f"piezas{cont2}"]["status"] = status_available
                        break
                elif status_piece == "3":
                        status_piece = str(status_piece)
                        status_available = "vendida"
                        catalog[f"piezas{cont2}"]["status"] = status_available
                        break
                else:
                        print("Opcion invalida, ingrese opcion del 1 al 3")

        print("")
        while True:
                print("*¿Cual de los dos estados siguientes describe mejor su pieza?*")
                print("1. usada")
                print("2. certificada")
                description_piece = input("Seleccione un estado (1 - 2) y agregue algo mas de la pieza" + str(cont2) + " : ")

                if description_piece.startswith("1"):
                        description_piece = str(description_piece)
                        catalog[f"piezas{cont2}"]["description"] = "pieza usada " + description_piece
                        break

                if description_piece.startswith("2"):
                        description_piece = str(description_piece)
                        catalog[f"piezas{cont2}"]["description"] = "pieza certificada " + description_piece
                        break
                else:
                        print("Opcion invalida, ingrese opcion del 1 al 2")
        cont2+=1
print()
print("Catalogo actualizado: ", catalog)


