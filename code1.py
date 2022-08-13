#!/usr/bin/env python3
import matplotlib.pyplot as pl
import numpy as np

#La función Prime, toma un número y revulve True si es primo y Falso en caso contrario
def Prime(x):
    if x<=1:
        return False
    if x==2:
        return True

    for i in range(2,x//2+1):
        if x%i ==0:
            return False
    return True

'''
#for i in range(1,18):
#    print(i,Prime(i))

#la función Scale_Prime entrega el eje y para graficar la cantidad de números primos que hay hasta cierto número x
def Scale_Prime(x_range):
    j=0 ; x_axis=[]
    for x in x_range:
        if Prime(x):
            j+=np.log(x)
        x_axis.append(j)
    return x_axis

#t=range(100000,100100)      #en este intervalo hay solo 2 primos
t=range(1000000,1000100)

pl.plot(t, Scale_Prime(t),"o") ; pl.grid()
#pl.plot(t,t)
pl.show()


print("n","#") ; j=0
for k in t:
    print(k,Scale_Prime(t)[j])
    j+=1
'''

'''
# Prime Counting Function: a funciton that counts the amount of primes less than or equal to N
def PCF(N):
    c=0
    for i in range(N):
        if Prime(i):
            c+=1
    return c

N=100
#print(PCF(N))
#print(round(N/np.log(N)))

lista_PCF=[] ; N_array = np.arange(2,N) ; lista_log=[]
for i in range(2,N):
    lista_PCF.append(PCF(i))
    lista_log.append(i/np.log(i))

pl.plot(N_array,lista_PCF) ; pl.xlabel("N") ; pl.ylabel("PCF(N)") ; pl.grid()
#pl.plot(N_array, lista_log)
pl.show()
'''

'''
#Sieve of Eratosthenes method
## La idea:
'''


#Función Zeta de Riemman para s>1
from math import pi

def zeta(s):
    sum=0
    for i in range(1,10000):          #creo que con 100.000 está bien
        sum+= 1 / i**s
    return sum

#print("Z(2)=",zeta(2))
#print("error=",abs(pi**2/6-zeta(2)))



#### Producto de Euler

def Euler_product(s):
    prime_list=[]
    for i in range(10000):
        if Prime(i):
            prime_list.append(i)

    product=1
    for p in prime_list:
        product *= 1 / (1-p**(-s))          #dado que p se hace más grande, la expresión se va acercando a 1 y los términos dejan de aportar mucho a la productoria
    return product

print(Euler_product(2))
print(zeta(2))
print("Real value=",pi**2/6)

#Conclusiones: al parecer, Euler me está dando mejores resultados, pero aún debo comprobarlo y medir cuanto mejores son respecto
#a la función zeta
