import parser_functions as pf
import construction as con
import numpy as np
import random

def THREEOPT(data,best,rand,dm):
    if rand:
        if len(data)<=5:
            return data
        possible = False
        while not possible:           
            r = random.sample(range(len(data)-1),  3)
            r.sort()
            if r[0]+2!=r[2] and r!=[0,1,len(data)-2] and r!=[0,len(data)-3,len(data)-2]:
                possible = True
        #if r[1]==r[0]+1 or r[2]==r[1]+1:
        mid1 = data[r[0]+1:r[1]+1]
        mid2 = data[r[1]+1:r[2]+1]
        new  = np.append(data[0:r[0]+1],mid2)
        new  = np.append(new,mid1)
        new  = np.append(new,data[r[2]+1:len(data)])            
        return new
        
            
    else:
        if best:
            if len(data)<=5:
                return data
            best3opt = data
            for i in range (0,len(data)-1):
                for j in range(i+1,len(data)-1):
                    for k in range (j+1,len(data)-1):
                        if k!=i+2 and (i,j,k)!=(0,1,len(data)-2) and (i,j,k)!=(0,len(data)-3,len(data)-2):
                            if j==i+1 or k==j+1:
                                #print (i," ",j," ",k)
                                mid1 = data[i+1:j+1]
                                mid2 = data[j+1:k+1]
                                new  = np.append(data[0:i+1],mid2)
                                new  = np.append(new,mid1)
                                new  = np.append(new,data[k+1:len(data)])
                            #print (new)
                                if con.ROUTE_COST(new,dm) < con.ROUTE_COST(best3opt,dm): 
                                    best3opt = new                                
                            else:
                                #print (i," ",j," ",k)
                                mid1 = data[i+1:j+1]
                                mid2 = data[j+1:k+1]
                                new  = np.append(data[0:i+1],mid2)
                                new  = np.append(new,mid1)
                                new  = np.append(new,data[k+1:len(data)])
                                if con.ROUTE_COST(new,dm) < con.ROUTE_COST(best3opt,dm): 
                                    best3opt = new
                                new  = np.append(data[0:i+1],mid2)
                                new  = np.append(new,mid1[::-1])
                                new  = np.append(new,data[k+1:len(data)])
                                if con.ROUTE_COST(new,dm) < con.ROUTE_COST(best3opt,dm): 
                                    best3opt = new
                                new  = np.append(data[0:i+1],mid2[::-1])
                                new  = np.append(new,mid1)
                                new  = np.append(new,data[k+1:len(data)])
                                if con.ROUTE_COST(new,dm) < con.ROUTE_COST(best3opt,dm): 
                                    best3opt = new
                                new  = np.append(data[0:i+1],mid1[::-1])
                                new  = np.append(new,mid2[::-1])
                                new  = np.append(new,data[k+1:len(data)])
                                if con.ROUTE_COST(new,dm) < con.ROUTE_COST(best3opt,dm): 
                                    best3opt = new
                            #print (i,"  ",j,"  ",k)
            return best3opt            
        else:
            if len(data)<=5:
                return data
            for i in range (0,len(data)-1):
                for j in range(i+1,len(data)-1):
                    for k in range (j+1,len(data)-1):
                        if k!=i+2 and (i,j,k)!=(0,1,len(data)-2) and (i,j,k)!=(0,len(data)-3,len(data)-2):
                            if j==i+1 or k==j+1:
                                mid1 = data[i+1:j+1]
                                mid2 = data[j+1:k+1]
                                new  = np.append(data[0:i+1],mid2)
                                new  = np.append(new,mid1)
                                new  = np.append(new,data[k+1:len(data)])
                             #print (new)
                                if con.ROUTE_COST(new,dm) < con.ROUTE_COST(data,dm): return new
                            else:
                                mid1 = data[i+1:j+1]
                                mid2 = data[j+1:k+1]
                                new  = np.append(data[0:i+1],mid2)
                                new  = np.append(new,mid1)
                                new  = np.append(new,data[k+1:len(data)])
                                if con.ROUTE_COST(new,dm) < con.ROUTE_COST(data,dm): return new
                                new  = np.append(data[0:i+1],mid2)
                                new  = np.append(new,mid1[::-1])
                                new  = np.append(new,data[k+1:len(data)])
                                if con.ROUTE_COST(new,dm) < con.ROUTE_COST(data,dm): return new
                                new  = np.append(data[0:i+1],mid2[::-1])
                                new  = np.append(new,mid1)
                                new  = np.append(new,data[k+1:len(data)])
                                if con.ROUTE_COST(new,dm) < con.ROUTE_COST(data,dm): return new
                                new  = np.append(data[0:i+1],mid1[::-1])
                                new  = np.append(new,mid2[::-1])
                                new  = np.append(new,data[k+1:len(data)])
                                if con.ROUTE_COST(new,dm) < con.ROUTE_COST(data,dm): return new
            return data
            

