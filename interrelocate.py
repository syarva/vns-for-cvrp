import parser_functions as pf
import construction as con
import numpy as np
import random
import copy

#data = [np.array([1,2,3,4,5,1]),np.array([1,6,7,8,9,10,1]),np.array([1,11,12,1])]

def INTERRELOCATE(routes,best,rand,dm,demand,capacity):
    if rand:
        new = copy.deepcopy(routes)
        ispossible = False
        count = 0
        while not ispossible and count<100:
            from1 = random.randint(0,len(new)-1)
            to    = random.randint(0,len(new)-1)
            
            while from1==to:
                from1 = random.randint(0,len(new)-1)
                to    = random.randint(0,len(new)-1)
            #print ("from",from1,"  to",to)
            if len(new[from1])-2 == 1:
                ran = 1
            else:
                #print(len(new[from1])-2)
                ran  = random.randint(1, len(new[from1])-2)
            count = count +1
            if con.ROUTE_DEMAND(new[to],demand)+demand[new[from1][ran]-1][1]<=capacity:
                ispossible = True
                if len(new[to])-2 == 1:
                    ranspot =1
                else:
                    ranspot = random.randint(1, len(new[to])-2)
                new[to] = np.insert(new[to],ranspot,new[from1][ran])
                new[from1] = np.delete(new[from1],ran)

        if ispossible:
            #for l in new:print(l)
            new = [x for x in new if len(x)>2]
            return new
        else:
            #for l in routes:print(routes)
            return routes
    else:
        if best:
            bir = copy.deepcopy(routes)
            for i in range(len(routes)):
                for j in range(len(routes)):
                    if i!=j:
                        for k in range(1,len(routes[i])-1):
                            if con.ROUTE_DEMAND(routes[j],demand)+demand[routes[i][k]-1][1]<=capacity:
                                
                                for m in range(1,len(routes[j])):
                                    new = copy.deepcopy(routes)
                                    new[j] = np.insert(new[j],m,new[i][k])
                                    new[i] = np.delete(new[i],k)
                                 
                                    if con.COST(new,dm)<con.COST(bir,dm):
                                        bir = copy.deepcopy(new)                                    
            return bir
        else:
            for i in range(len(routes)):
                for j in range(len(routes)):
                    if i!=j:
                        for k in range(1,len(routes[i])-1):
                            if con.ROUTE_DEMAND(routes[j],demand)+demand[routes[i][k]-1][1]<=capacity:
                                
                                for m in range(1,len(routes[j])):
                                    new = copy.deepcopy(routes)
                                    new[j] = np.insert(new[j],m,new[i][k])
                                    new[i] = np.delete(new[i],k)
                                    if con.COST(new,dm)<con.COST(routes,dm):
                                        return new                                    
            return routes
  
