
matriz = [ [10, 15, 20],[3, 7, 14] ]

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

matriz[1][0] = 6
print(matriz)

cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes)

ciudades["México"][2]="Monterrey"
print(ciudades)

coordenadas[0]["latitud"]= 9.9355431

print(coordenadas)

#2

def iterarDiccionario(lista):
    for diccionario in lista:
        for llave, valor in diccionario.items():
            print(f"{llave}, - {valor}")

iterarDiccionario(cantantes)

#3 

def iterarDiccionario2(key,list):
    for dicc in list:
        if key in dicc:
            dato= dicc[key]
            print(dato)
        else:
            print("No existe llave")
        
iterarDiccionario2("pais",cantantes)

#4
def imprimirInformacion(diccionario):
    for i in diccionario:
        valores = diccionario[i]
        print(len(diccionario[i]), i)
        for x in valores:
            print(x)

imprimirInformacion(ciudades)

