#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:
def primo(n):
    aux=0
    for i in range(n+1):
        if(i!=0):
            if n%i==0:
                if(i!=1):
                    aux +=1
    if aux!=1: return False
    else: return True
print(primo(997))




# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:
def primo(n):
    aux=0
    for i in range(n+1):
        if(i!=0):
            if n%i==0:
                if(i!=1):
                    aux +=1
    if aux!=1: return False
    else: return True
#print(primo(2))

def seleccionPrimos(nLista):
    listaPrimos = []
    for i in range(len(nLista)):
        regreso = False
        regreso = primo(nLista[i])
        if regreso == True:
            listaPrimos.append(i+1)
    return listaPrimos

nP = list(range(1, 1001))
print(seleccionPrimos(nP))


# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:
def moda(np):
    numero = 0
    cantidadDeVecesQueSeRepite = 0
    repetidos =  map ( lambda x: (x, nP.count(x)), nP)
    for i in repetidos:
        if i[1] > cantidadDeVecesQueSeRepite:
            cantidadDeVecesQueSeRepite = i[1]
            numero = i[0]
    return numero, cantidadDeVecesQueSeRepite
            
nP= [1,1,1,2,3,4,5,5,5,5]
print(moda(nP))



# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:
# Solicitar al usuario que ingrese el valor a convertir
# print("Ingrese el valor a Convertir: ")
# valor = float(input())  # Convertir la entrada a tipo float para permitir decimales

# Solicitar la medida de origen
# print("Seleccione la medida de origen:\n 1) Celsius\n 2) Farenheit\n 3) Kelvin")
# medidaOrigen = int(input())  # Convertir la entrada a tipo int para facilitar la comparación

# Solicitar la medida de destino
# print("Seleccione la medida de destino:\n 1) Celsius\n 2) Farenheit\n 3) Kelvin")
# medidaDestino = int(input())  # Convertir la entrada a tipo int para facilitar la comparación

# Definir la función para realizar la conversión
def convertir(valor, medidaOrigen, medidaDestino):
    if medidaOrigen == 1:
        if medidaDestino == 1:
            return valor
        elif medidaDestino == 2:
            return (valor * 9/5) + 32
        else:
            return valor + 273.15
    elif medidaOrigen == 2:
        if medidaDestino == 1:
            return (valor - 32) * 5/9
        elif medidaDestino == 2:
            return valor
        else:
            return (valor - 32) * 5/9 + 273.15
    else:
        if medidaDestino == 1:
            return valor - 273.15
        elif medidaDestino == 2:
            return (valor - 273.15) * 9/5 + 32
        else:
            return valor

# Imprimir el resultado de la conversión
print("Resultado de la conversión:", convertir(150, 2, 3))


# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:
metricas = {"celsius": 1, "kelvin": 2, "farenheit": 3}

for i in range(0, 3):
    for j in range(0, 3):
        print('1 grado', list(metricas.keys())[i], 'a', list(metricas.keys())[j], ':', convertir(1, metricas[list(metricas.keys())[i]], metricas[list(metricas.keys())[j]]))



# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:
def factorial(numero):
    # Verifica si el número no es entero y devuelve un mensaje de error
    if type(numero) != int:
        return 'El número debe ser un entero'
    
    # Verifica si el número es negativo y devuelve un mensaje de error
    if numero < 0:
        return 'El número debe ser positivo'
    
    # Caso base: si el número es 0 o 1, el factorial es 1
    if numero <= 1:
        return 1
    
    # Recursión: calcula el factorial del número multiplicándolo por el factorial del número anterior
    numero = numero * factorial(numero - 1)
    
    return numero

print(factorial(5))



