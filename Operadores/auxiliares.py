# import time                         # time                  NO SE USA
import matplotlib.pyplot as plt     # plot                  EN PINTAR___
# import numpy as np                  #                       NO SE USA
# import math as m                    #                       NO SE USA
import random as rd                 #                       EN PICCOLORE
import re                           # regular expression    EN PINTAR4, ... para buscar p o %


def norma1(v):          # suma elemento a elemento del vector (float)
    s = 0                 #    si norma1=0 devuelve 1
    for i in v:
        s += abs(i)
    if s != 0:
        return float(s)
    else:
        return 1


def normmax(v):         # máximo de los elementos del vector (float)
    s = 0                 #    si normm=0 devuelve 1
    for i in v:
        if abs(i) > s:
            s = abs(i)
    if s != 0:
        return float(s)
    else:
        return 1


def piccolore(t, blue=False):      # paleta de colores
    if t <= 6 and not blue:
        colores = ['red', 'green', 'yellow', 'magenta', 'cyan', 'black']
    elif t <= 7 and blue:
        colores = ['blue', 'red', 'green', 'yellow', 'magenta', 'cyan', 'black']
    else:
        colores = [(rd.random(), rd.random(), rd.random()) for k in range(t)]
    while (1):
        for co in colores:
            yield co

# QUEDA AÚN POR DESARROLLAR DICCIONARIODECOLOR