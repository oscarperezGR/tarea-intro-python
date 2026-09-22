print()
print("*"* 40)
print()
print("Bienvenido o Bienvenida para al sistema de registro de piezas")
print()
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
