#!/usr/bin/env python3

#3blue1brown: pi and prime numbers
import matplotlib.pyplot as pl
import numpy as np

#1) create a function that returns the factors of any integer

#first, I'm making a circle... just for fun
'''
t=np.linspace(-5,5,300)

def circle(x,s):
    if s=="p":
        return np.sqrt(25-x**2)         #y^2 = r^2-x^2
    if s=="n":
        return -np.sqrt(25-x**2)

pl.plot(t,circle(t,"p"),"-b")
pl.plot(t,circle(t,"n"),"-b")
pl.show()
'''

'''
#Now, I'm gonna use simpy to obtain the factors. (factorint and primefactors)
import sympy as sp

n=125
factors = sp.primefactors(n)
factors1 = sp.factorint(n)
print(factors,type(factors))
print(factors1,type(factors1))
exponent=factors1[5]
print(exponent)

#I like the "sp.factorint" one because it gives you the prime numbers and the exponent separately
'''

'''
#2) investigate the issue of the primes 1 obove a multiple of 4 and 3
'''

'''
#3) chi function

def x(n):
    if :
        return 1
    if :
        return -1
'''
