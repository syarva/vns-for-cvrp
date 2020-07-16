import parser_functions as pf
import construction as con
import clusterfirst
#import improvement as imp
import numpy as np
import greedy
import swap
import relocate
import twoopt
import threeopt
import interswap as isw
import interrelocate as ir
import vnd
import shake
import vns
import time
# λιστα με τα διαθεσιμα instances
instances = ["att48","eil13","eil22","eil23","eil30","eil31","eil33","eil51",
             "eil7","eila101","eila76","eilb101","eilb76","eilc76","eild76"]
             
print ("Choose an instance")  # options menu
for x in range (0,len(instances)): print (x+1,"-",instances[x])

instance = input()
if (instance=="eil13") or (instance=="eil31") or (instance=="eil7"):
    Type = "expl"
else:
    Type = "2d"

bestv = pf.DATA(instance)
#(min_trucks,best_value,capacity) = (data[0],data[1],data[2])
capacity = pf.CAPACITY(instance)
demand = pf.DEMAND(instance)
dimension = len(demand)
print ("Capacity:",capacity)
print ("Demand:")
print(demand)
print("Distance matrix:")
distance_matrix = pf.DISTANCE_MATRIX(instance,dimension)
print()
print("optimal:  ",bestv)



start=time.time()
gvr = greedy.GREEDY(capacity,distance_matrix,demand,dimension)
dnn=time.time()-start
start=time.time()
clustersnew = clusterfirst.CLUSTER_FIRST(instance,demand,dimension,capacity,distance_matrix)
dsw=time.time()-start
start=time.time()
cw = con.CLARKE_WRIGHT(distance_matrix,dimension,demand,capacity)
dcw = time.time()-start
print("nn   : ",dnn)
print("sweep: ",dsw)
print("cw   : ",dcw)


"""
print ("Choose a construction method: nn for nearest neighbor, sw for sweep, cw for clarke-wright ")
constr = input()
if constr=="nn":
    


# gvr --> greedy vehicle routing
    gvr = greedy.GREEDY(capacity,distance_matrix,demand,dimension)
    costgvr = con.COST(gvr,distance_matrix)

    sumnn=0
    print("set time limit")
    time=int(input())
    for i in range (0,10):
        newnn = vns.VNS(gvr,time,costgvr,distance_matrix,demand,capacity,10)
                
        for x in newnn: 
            #x= x - np.ones((len(x),), dtype=int)
            print(x - np.ones((len(x),), dtype=int)," cost:",con.ROUTE_COST(x,distance_matrix),", demand:",con.ROUTE_DEMAND(x,demand))
        
        costnewnn = con.COST(newnn,distance_matrix)
        print(costnewnn,len (newnn))
        print()
        sumnn = sumnn + costnewnn
    print (sumnn/10)
    print()
elif constr=="sw":
    
    clustersnew = clusterfirst.CLUSTER_FIRST(instance,demand,dimension,capacity,distance_matrix)
    costcl = con.COST(clustersnew,distance_matrix)
    sumc = 0
    print("set time limit")
    time=int(input())
    for i in range(0,10):
        
        newc = vns.VNS(clustersnew,time,costcl,distance_matrix,demand,capacity,10)
                
        for x in newc: 
            #x= x - np.ones((len(x),), dtype=int)
            print(x - np.ones((len(x),), dtype=int)," cost:",con.ROUTE_COST(x,distance_matrix),", demand:",con.ROUTE_DEMAND(x,demand))
        costnewc = con.COST(newc,distance_matrix)    
        print (costnewc,len (newc))
        print()
        sumc = sumc + costnewc
    print (sumc/10)
    
else:
    
    
#cw --> clarke_wright
    cw = con.CLARKE_WRIGHT(distance_matrix,dimension,demand,capacity)
    
    costcw = con.COST(cw,distance_matrix)
    
    sumcw = 0
    print("set time limit")
    time=int(input())
    for i in range(0,10):
        newcw = vns.VNS(cw,time,costcw,distance_matrix,demand,capacity,10)
                
        for x in newcw: 
            #x= x - np.ones((len(x),), dtype=int)
            print(x - np.ones((len(x),), dtype=int)," cost:",con.ROUTE_COST(x,distance_matrix),", demand:",con.ROUTE_DEMAND(x,demand))
        costnewcw = con.COST(newcw,distance_matrix)
        print (costnewcw, len (newcw))
        print()
        sumcw = sumcw + costnewcw
    print (sumcw/10)
    
#file = open("test.txt","a") 
 
#file.write("\\"+"textlatin{"+instance+"} & -  &  " +str(len(gvr))+"-"+str(costgvr)+"  & -  &  "+str(len(clustersnew))+"-"+str(costcl) +"  & - &  "+str(len(cw))+"-"+str(costcw)+ "  & - \\"+"\n") 
 
#file.close() 
#print("\\"+"textlatin{"+instance+"} & -  &  " +str(len(gvr))+"-"+str(costgvr)+"  & -  &  "+str(len(clustersnew))+"-"+str(costcl) +"  & - &  "+str(len(cw))+"-"+str(costcw)+ "  & - \\")

"""
