import parser_functions as pf
import construction as con
import numpy as np
import random

data=np.array([1,2,3,4,5,6,7,1])


     

                
        
def THREE_OPT(data,dm,best):
    if best == False:
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
    else:
        best3opt = data
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
                            if con.ROUTE_COST(new,dm) < con.ROUTE_COST(best3opt,dm): 
                                best3opt = new
                                
                        else:
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
    


    
def INTER_SWAP(routes,dm,demand,best,capacity):
    if best:
        bswap = routes
        print (bswap)
        
        for i in range(0,len(routes)):
            new=routes
            for j in range(i+1,len(routes)):
                new=routes
                for k in range (1,len(routes[i])-1):
                    new=routes                            
                    for l in range (1,len(routes[j])-1):
                        new = routes
                        print (routes)
                        n = demand[routes[i][k]-1][1]
                        m = demand[routes[j][l]-1][1]

                        print (routes[i][k]," ",n,"    ",routes[j][l]," ",m)
                        
                        print ()
                        if con.ROUTE_DEMAND(routes[i],demand)-n+m<=capacity and con.ROUTE_DEMAND(routes[j],demand)-m+n<=capacity:                            
                            
                            
                            new[i][k],new[j][l] = new[j][l],new[i][k]
                            #new[i][k] = routes[j][l]
                            #new[j][l] = routes[i][k]
                            if con.COST(new,dm)<con.COST(bswap,dm) and con.COST(new,dm)<con.COST(bswap,dm):
                                bswap = new
        return bswap
    else:
        for i in range(0,len(routes)):
            for j in range(i+1,len(routes)):
                for k in range (1,len(routes[i])-1):
                    n = demand[routes[i][k]-1][1]
                    for l in range (1,len(routes[j])-1):                        
                        m = demand[routes[j][l]-1][1]
                        if con.ROUTE_DEMAND(routes[i],demand)-n+m<=capacity and con.ROUTE_DEMAND(routes[j],demand)-m+n<=capacity:
                            g = routes[i][k]
                            h = routes[j][l]
                            new = routes
                            print (new)
                            new[i][k] = h
                            new[j][l] = g
                            print()
                            print(new)
                            """
                            for y in new: 
                                print (y)
                            print ()
                            """
                            if con.COST(new,dm)<con.COST(routes,dm) and con.COST(new,dm)<con.COST(routes,dm):
                                return new
        return routes
        
                            
                        
            
                

 
#RANDOM_2OPT(data) 
#RANDOM_RELOCATE(data) 
#print (RANDOM_SWAP(data))
#THREE_OPT(data)
#for i in TWOOPT(data,True): print (i)