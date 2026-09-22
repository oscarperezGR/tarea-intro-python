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
                "id": 3,
                "name": "",
                "category": "",
                "price": 0,
                "status": "",
                "description": ""
        },
        "piezas5": {
                "id": 3,
                "name": "",
                "category": "",
                "price": 0,
                "status": "",
                "description": ""
        },
        "piezas6": {
        "id": 3,
        "name": "",
        "category": "",
        "price":0,
        "status": "",
        "description": ""
        },
        "piezas7": {
        "id": 3,
        "name": "",
        "category": "",
        "price": 0,
        "status": "",
        "description": ""
        },
        "piezas8": {
                "id": 3,
                "name": "",
                "category": "",
                "price": 0,
                "status": "",
                "description": ""

        },
        "piezas9": {
                "id": 3,
                "name": "",
                "category": "",
                "price": 0,
                "status": "",
                "description": ""

        },
        "piezas10": {
                "id": 3,
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
        nombre = input("ingreso el nombre de la pieza " + str(cont2) + " : ")
        catalog[f"piezas{cont2}"]["name"]=nombre
        categoria = input("ingreso la categoria")
        catalog[f"piezas{cont2}"]["category"]=categoria
        cont2+=1

print("Catalogo actualizado: ", catalog)


