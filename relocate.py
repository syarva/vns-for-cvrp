import parser_functions as pf
import construction as con
import numpy as np
import random
import copy

#data=np.array([1,2,3,4,5,6,7,8,9,10,11,12,1])

def RELOCATE(data,best,rand,dm):
    if rand:
        x,y = random.randint(1,len(data)-2),random.randint(1,len(data)-2)
        while x==y:
            x,y = random.randint(1,len(data)-2),random.randint(1,len(data)-2)
        new = copy.deepcopy(data)
        if x<y:            
            new = np.insert(new,y+1,data[x])
            new = np.delete(new,x)            
        else:            
            new = np.delete(new,x)
            new = np.insert(new,y,data[x])        
        return new 
    else:                        
        if best:
            newdata = data
            for i in range (1,len(data)-1):
                for j in range (1,len(data)-1):
                    if i<j:
                        new = copy.deepcopy(data)                        
                        new = np.insert(new,j+1,data[i])                    
                        new = np.delete(new,i)
                        c, nc = con.ROUTE_COST(data,dm),con.ROUTE_COST(new,dm)
                        if nc<=c:
                            newdata = copy.deepcopy(new)                        
                    elif i>j:
                        new = copy.deepcopy(data)                        
                        new = np.delete(new,i)                   
                        new = np.insert(new,j,data[i])
                        c, nc = con.ROUTE_COST(data,dm),con.ROUTE_COST(new,dm)
                        if nc<=c:
                            newdata = copy.deepcopy(new)
            return newdata
        else:                                    
            for i in range (1,len(data)-1):
                for j in range (1,len(data)-1):
                    if i<j:
                        new = copy.deepcopy(data)                        
                        new = np.insert(new,j+1,data[i])                    
                        new = np.delete(new,i)
                        c, nc = con.ROUTE_COST(data,dm),con.ROUTE_COST(new,dm)                     
                        if nc<=c:
                            return new
                    elif i>j:
                        new = copy.deepcopy(data)                        
                        new = np.delete(new,i)                   
                        new = np.insert(new,j,data[i])
                        c, nc = con.ROUTE_COST(data,dm),con.ROUTE_COST(new,dm)                       
                        if nc<=c:
                            return new
            return data  
            
#print(RELOCATE(data,False,True))
#print(data)