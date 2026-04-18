#Crea la función multiplica_por_dos(num)
def multiplica_por_2(numero):
    lista_resultado = []
    # Usamos range(numero + 1) para incluir el número del ejemplo
    for i in range(numero + 1):
        lista_resultado.append(i * 2)
    return lista_resultado

#Crea la función suma_y_resta(lista)

def suma_y_resta(lista):
    suma = lista[0] + lista[1]
    print(suma)  # Esto se muestra en pantalla
    
    resta = lista[0] - lista[1]
    return resta # Esto es lo que la función "vale"

#print(suma_y_resta([3,4]))

#Crea la función sumatoria_menos_longitud(lista)

def sumatoria_menos_longitud(lista):
    sumatoria = sum(lista)        # Suma todos los elementos: 1+2+3+4 = 10
    longitud = len(lista)         # Cuenta cuántos elementos hay: 4
    return sumatoria - longitud   # Regresa 10 - 4 = 6

# Prueba
resultado = sumatoria_menos_longitud([1, 2, 3, 4])
print(resultado)  # Salida: 6

#Crea la función valores_multiplicados_segundo(lista)

def valores_multiplicados_segundo(lista):
    # Primero imprimimos la longitud, pase lo que pase
    print(len(lista))
    
    # Validación: si tiene menos de 2 elementos, no hay "segundo número"
    if len(lista) < 2:
        return []
    
    # El segundo elemento está en el índice 1
    segundo_valor = lista[1]
    nueva_lista = []
    
    for num in lista:
        nueva_lista.append(num * segundo_valor)
    
    return nueva_lista

#Crea la función valor_multiplicado_longitud(valor, longitud)

def valor_multiplicado_longitud(valor, longitud):
    # Calculamos el número que irá dentro de la lista
    resultado = valor * longitud
    
    # Creamos una lista con ese resultado repetido "longitud" veces
    nueva_lista = [resultado] * longitud
    
    return nueva_lista