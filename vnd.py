# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 14:13:18 2018

@author: Simos
"""
import twoopt
import swap
import relocate
import threeopt
import interswap as isw
import swap as sw
import interrelocate as ir
import relocate as r
import construction as con
import copy

def VND(routing,cost,dm,demand,capacity):
    improvement = True
    routes = copy.deepcopy(routing)
    while improvement:
        t = 0
        for i in range (len(routes)):
            c = twoopt.TWOOPT(routes[i],False,False,dm)
            if con.ROUTE_COST(routes[i],dm)>con.ROUTE_COST(c,dm):
                routes[i] = copy.deepcopy(c)
                t = t+1
                #print ("2opt")
                break
        if t>0:            
            continue
        
        g = ir.INTERRELOCATE(routes,False,False,dm,demand,capacity)#or interrel +demand,capacity
        if con.COST(routes,dm)>con.COST(g,dm):
            routes = copy.deepcopy(g)
            #print("interrelocate")
            continue
        
        f = isw.INTERSWAP(routes,False,False,dm,demand,capacity)#or inteswap +demand,capacity
        if con.COST(routes,dm)>con.COST(f,dm):
            routes = copy.deepcopy(f)
            #print("interswap")
            continue

        improvement = False
        
        
        
    return routes
    
                
        
    
    
