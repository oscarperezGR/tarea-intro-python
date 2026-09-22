myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

#hacer un while o for con rango de 5 (range)
for x, obj in myfamily.items():
    #nuevos childrens
    print(x)

    for y in obj:
        #nuevos elemtnpos de los childrens
        print(y + ':', obj[y])
