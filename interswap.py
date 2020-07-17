import parser_functions as pf
import construction as con
import numpy as np
import random
import copy

#data = [np.array([1,2,3,4,5,1]),np.array([1,6,7,8,9,10,1]),np.array([1,11,12,1])]

def INTERSWAP(routes,best,rand,dm,demand,capacity):
    if rand:
        ispossible = False
        new = copy.deepcopy(routes)
        count = 0
        while not ispossible and count<100:
            ispossible=True
            c = random.sample(range(len(new)),2)
            #print(new[c[0]],new[c[1]])#
            b = random.randint(1, len(new[c[0]])-2)
            a = random.randint(1, len(new[c[1]])-2)
            new[c[0]][b],new[c[1]][a] = new[c[1]][a],new[c[0]][b]
            for route in new:
                if con.ROUTE_DEMAND(route,demand)>capacity:
                    ispossible = False
                    new = copy.deepcopy(routes)
            count = count+1
        if ispossible:
            #for x in new: print(x)
            return new
        else:
            return routes
    else:
        if best:
            bestinterswap = copy.deepcopy(routes)
            for i in range(len(routes)):
                for j in range(len(routes)):
                    if i!=j:
                        
                        for k in range(1,len(routes[i])-1):
                            for m in range(1,len(routes[j])-1):
                                ispossible = True
                                new = copy.deepcopy(routes)                            
                                new[i][k],new[j][m] = new[j][m],new[i][k]                            
                                for route in new:
                                    if con.ROUTE_DEMAND(route,demand)>capacity:
                                        ispossible = False
                                if ispossible and con.COST(routes,dm)>con.COST(new,dm):
                                    bestinterswap = copy.deepcopy(new)                            
            return bestinterswap
        else:
            for i in range(len(routes)):
                for j in range(len(routes)):
                    if i!=j:                        
                        for k in range(1,len(routes[i])-1):
                            for m in range(1,len(routes[j])-1):
                                ispossible = True
                                new = copy.deepcopy(routes)
                                new[i][k],new[j][m] = new[j][m],new[i][k]
                                for route in new:
                                    if con.ROUTE_DEMAND(route,demand)>capacity:
                                        ispossible = False
                                if ispossible and con.COST(routes,dm)>con.COST(new,dm):
                                    return new
            return routes


