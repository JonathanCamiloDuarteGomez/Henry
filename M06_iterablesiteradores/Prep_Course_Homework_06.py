#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:
while True:
    lista = []
    for i in range(-15, 0):
        lista.append(i)
    print(lista)
    break




# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:
while True:
    lista = []
    for i in range(-15, 0):
        lista.append(i)
        lista = [i for i in lista if i % 2 == 0]
    print(lista)
    break
    




# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:

lista = []
for i in range(-15, 0):
    lista.append(i)
    lista = [i for i in lista if i % 2 == 0]
print(lista)



# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

# In[7]:
lista = []
for i in range(-15, 0):
    lista.append(i)
print(lista[0:3])



# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:

lista = []
for i in range(-15, 0):
    lista.append(i)
for i in enumerate(lista):
    print(i)


# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:
lista = [1,2,5,7,8,10,13,14,15,17,20]
complemento = []

for elemento in range(len(lista)-1):
    if lista[elemento+1] - lista[elemento] > 1:
        complemento.append(lista[elemento]+1)
        
lista.extend(complemento)
lista=sorted(lista)
print(lista)


# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:
def fibonacci(n):
    lista = []
    a = 0
    b = 1
    for i in range(n):
        lista.append(a)
        a, b = b, a + b
    return lista

fibonacci_sequence = fibonacci(30)
print(fibonacci_sequence)


# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:
def fibonacci(n):
    lista = []
    a = 0
    b = 1
    for i in range(n):
        lista.append(a)
        a, b = b, a + b
    return lista

fibonacci_sequence = fibonacci(30)
print(sum(fibonacci_sequence))



# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:
def fibonacci(n):
    lista = []
    a = 0
    b = 1
    for i in range(n):
        lista.append(a)
        a, b = b, a + b
    return lista

def cociente(lista):
    for i in range(len(lista)-1):
        print(lista[i+1]/lista[i])



fibonacci_sequence = fibonacci(30) 
aux=0
diez_Ultimos_Pares = []
while aux <=10:
    for x in fibonacci_sequence[-10:]:
        if x % 2 == 0:
            diez_Ultimos_Pares.append(x)
            aux+=1
cociente(diez_Ultimos_Pares)




# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
for i, c in enumerate(cadena):
    if c == 'n':
        print(i)




# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:

estudiante = {
    "Nombre": "Sara",
    "Materias": ["Matemáticas", "Física", "Química"],
    "Notas": [4.5, 3.5, 4.0],
    "Promedio": 4.0
}
for i in estudiante:
    print(i)


# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
lista = list(cadena)
for i in lista:
    print(i)




# In[45]:





# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:

lista1 = [1,2,3,4,5]
lista2 = ['uno','dos','tres','cuatro','cinco']
tupla = zip(lista1, lista2)
print(tuple(tupla))





# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# In[49]:

lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
lis2 = [i for i in lis if i % 7 == 0]
print(lis2)



# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# In[56]:
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
print(lis.__len__())



# In[51]:





# In[57]:





# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:
for indice, elemento in enumerate(lis):
    if (type(elemento) != list):
        lis[indice]=[elemento]
    print(type(elemento))
print(lis)


# %%
