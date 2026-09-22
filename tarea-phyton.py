print()
print("*"* 40)
print("Bienvenido o Bienvenida para al sistema de registro de pieza")
print("Usted esta ingresando al catálogo de piezas coleccionables")
print("*"* 40)


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

        }
}

for x, obj in catalog.items():
    print(x)

    for y in obj:
        input("Piezas")
        print(y+ ':', obj[y])
