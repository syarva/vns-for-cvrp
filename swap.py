import parser_functions as pf
import construction as con
import numpy as np
import random
import copy

#data=np.array([1,2,3,4,5,6,7,1])


def SWAP(data,best,rand,dm): 
    if rand:
        x,y = random.randint(1,len(data)-2),random.randint(1,len(data)-2)
        while x==y:
            x,y = random.randint(1,len(data)-2),random.randint(1,len(data)-2)
        new = copy.deepcopy(data)              
        new[x],new[y] = new[y],new[x]
        return new               
    else:                
        if best:        
            newdata = data
            for i in range (1,len(data)-1):
                for j in range (i+1,len(data)-1):
                    new = copy.deepcopy(data)
                    new[i],new[j] = new[j],new[i]
                    c, nc = con.ROUTE_COST(data,dm),con.ROUTE_COST(new,dm)
                    if nc<=c:
                        newdata = copy.deepcopy(new)                                        
            return newdata
        else:
            newdata = []
            for i in range (1,len(data)-1):
                for j in range (i+1,len(data)-1):
                    new = copy.deepcopy(data)
                    new[i],new[j] = new[j],new[i]
                    c, nc = con.ROUTE_COST(data,dm),con.ROUTE_COST(new,dm)
                    if nc<=c:                        
                        return new                    
            return data

#print(SWAP(data,False,True))
#print(data)
