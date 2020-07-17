# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 18:51:24 2018

@author: Simos
"""
import random
import copy
import twoopt
import interswap as isw
import interrelocate as ir
import swap
import relocate
import construction as con


def SHAKE(kmax,routes,dm,demand,capacity):
    shaked = copy.deepcopy(routes)
    for i in range(kmax):
        j = random.randint(1,2)
        if j==1:
            #print("isw")
            shaked = isw.INTERSWAP(shaked,False,True,dm,demand,capacity)
        elif j==2:
            #print("ir")
            shaked = ir.INTERRELOCATE(shaked,False,True,dm,demand,capacity)
    return shaked
        