#!/usr/bin/env python
# coding: utf-8

# ## Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor

# In[1]:
from enum import Enum
class tipoVehiculo(Enum):
    moto = "moto"
    auto = "auto"
    camion = "camion"

class Vehiculo:
    def __init__(self, color, tipo, cilindrada):  
        self.color = color
        self.tipo =  tipoVehiculo(tipo)
        self.cilindrada = cilindrada



# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>

# In[5]:
from enum import Enum
class tipoVehiculo(Enum):
    moto = "moto"
    auto = "auto"
    camion = "camion"

class Vehiculo:
    def __init__(self, color, tipo, cilindrada):  
        self.color = color
        self.tipo =  tipoVehiculo(tipo)
        self.cilindrada = cilindrada
    def acelerar(self):
        print("Acelerando")
    def frenar(self):   
        print("Frenando")
    def doblar(self):
        print("Doblando")



# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

# In[6]:
moto1 = Vehiculo("rojo", "moto", 250)
auto1 = Vehiculo("blanco", "auto", 1500)
camion1 = Vehiculo("azul", "camion", 5000)
    
moto1.acelerar()
auto1.frenar()
camion1.doblar()
    




# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

# In[12]:

from enum import Enum
class tipoVehiculo(Enum):
    moto = "moto"
    auto = "auto"
    camion = "camion"

class Vehiculo:
    def __init__(self, color, tipo, cilindrada, velocidad, direccion):  
        self.color = color
        self.tipo =  tipoVehiculo(tipo)
        self.cilindrada = cilindrada
        self.velocidad = velocidad
        self.direccion = direccion
        
    def acelerar(self):
        print("Acelerando")
    def frenar(self):   
        print("Frenando")
    def doblar(self):
        print("Doblando")
    def Estado(self):
            print('Velocidad:', self.velocidad, '- Dirección:', self.direccion)
    def Detalle(self):
            print('Soy', self.tipo, 'de color', self.color, 'y mi cilindrada es de', self.cilindrada, 'litros')




# In[13]:

camion1 = Vehiculo("azul", "camion", 5000, 100, 90)
camion1.Estado()
camion1.Detalle()





# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 7<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>

# In[33]:
class Funciones:

    def primo(n):
        aux = 0
        for i in range(n+1):
            if i != 0 and n % i == 0:
                if i != 1:
                    aux += 1
        return aux == 1


    def moda(nP):
        numero = 0
        cantidadDeVecesQueSeRepite = 0
        repetidos = map(lambda x: (x, nP.count(x)), nP)
        for i in repetidos:
            if i[1] > cantidadDeVecesQueSeRepite:
                cantidadDeVecesQueSeRepite = i[1]
                numero = i[0]
        return numero, cantidadDeVecesQueSeRepite


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


    def factorial(numero):
        if type(numero) != int:
            return 'El número debe ser un entero'
    
        if numero < 0:
            return 'El número debe ser positivo'
    
        if numero <= 1:
            return 1
    
        return numero * Funciones.factorial(numero - 1)




# 6) Probar las funciones incorporadas en la clase del punto 5

# In[28]:
print(primo = Funciones.primo(5))
listado = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,15]
print(moda = Funciones.moda(listado))
print(convertir = Funciones.convertir(100,1,2))
print(factorial = Funciones.factorial(5))




# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

# In[55]:




# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones

# In[1]:




