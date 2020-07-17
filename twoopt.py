import parser_functions as pf
import construction as con
import numpy as np
import random
import copy

data=np.array([1,2,3,4,5,6,7,1])

def TWOOPT(data,best,rand,dm):
    if rand:
        if len(data)<=3:
            return data
        i = random.randint(1,len(data)-3)
        j = random.randint(i+2,len(data)-1)
        while  abs(i-j)==len(data)-2:
            print(1)
            i = random.randint(1,len(data)-3)
            j = random.randint(i+2,len(data)-1)
        mid = data[i:j]        
        new = np.append(data[0:i],np.append(mid[::-1],data[j:len(data)]))
        return new
    else:                
        if best: 
            if len(data)<=3:
                return data
            best2opt = data
            for i in range (1,len(data)):
                for j in range(i+2,len(data)):
                    if data[i-1]!=data[j]:                                            
                        mid = data[i:j]
                        new = np.append(data[0:i],np.append(mid[::-1],data[j:len(data)]))
                        if con.ROUTE_COST(new,dm) < con.ROUTE_COST(data,dm):
                            best2opt = copy.deepcopy(new)                    
            return best2opt
        else:   
            if len(data)<=3:
                return data
            for i in range (1,len(data)):
                for j in range(i+2,len(data)):
                    if data[i-1]!=data[j]:
                        mid = data[i:j]
                        new = np.append(data[0:i],np.append(mid[::-1],data[j:len(data)]))
                        if con.ROUTE_COST(new,dm) < con.ROUTE_COST(data,dm):
                            return new                    
            return data

def randtwoopt(data):
    if len(data)<=3:
        return data
    i = random.randint(1,len(data)-3)
    j = random.randint(i+2,len(data)-1)
    while  abs(i-j)==len(data)-2:
        i = random.randint(1,len(data)-3)
        j = random.randint(i+2,len(data)-1)
    mid = data[i:j]        
    new = np.append(data[0:i],np.append(mid[::-1],data[j:len(data)]))
    return new

        
print (data)
r = randtwoopt(data)
print (r)