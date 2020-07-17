import math
import parser_functions as pf
import numpy as np
import construction as con
import copy
import twoopt

def getKey(item):
    return item[1]

#Yπολογισμός της γωνιας (σε ακτινια). Ποσο πρεπει να περιστραφει ο θετικος 
#ημιαξονας αριστεροστροφα για να συναντησει το σημειο x,y 
def ANGLE(x,y):
    if y==0:
        if x>=0: return 0.0
        else:    return 3.14159265
    elif y>0: return math.acos(x/(math.sqrt(x*x+y*y)))
    else:     return 6.2831853 - math.acos(x/(math.sqrt(x*x+y*y)))

def CLUSTER_FIRST(instance,demand,dimension,capacity,dm):  
#συναρτηση για τη δημιουργια των clusters ετσι ωστε να χρησιμοποιηθουν στην
#κατασκευη αρχικης λυσης με τη μεθοδο cluster first - route second

    #sba --> sorted by angle
    coord = pf.COORD(instance,dimension)
    sba = np.zeros((dimension,2))
    
    #για ευκολια κανουμε παραλληλη μετατοπιση ετσι ωστε το depot να ερθει στην
    #αρχη των αξονων
    for i in range (0,dimension):        
        sba[i][0] = coord[i][0]
        sba[i][1] = ANGLE(coord[i][1]-coord[0][1],coord[i][2]-coord[0][2])
        
    sba = sorted(sba, key=getKey)
    sba = np.delete(sba, 1, 1)
    sba = sba.flatten()
    sba = sba.astype(int)
    sba = np.delete(sba,0)

    # δημιουργια των clusters
    bestclustering = CLUSTERING(sba,demand,capacity)

    # δρομολογηση με 2opt    
    improvement = True
    while improvement:
        t = 0
        for i in range (len(bestclustering)):
            c = twoopt.TWOOPT(bestclustering[i],True,False,dm)
            if con.ROUTE_COST(bestclustering[i],dm)>con.ROUTE_COST(c,dm):
                bestclustering[i] = copy.deepcopy(c)
                t = t+1
                break
        if t>0:
            continue
        improvement = False    
    
    print ("CLUSTERING:")
    print ("number of clusters:", len(bestclustering))    
    for x in bestclustering: print(x," cost:",con.ROUTE_COST(x,dm),", demand:",con.ROUTE_DEMAND(x,demand))  
    print("total cost: ",con.COST(bestclustering,dm))
    print()
    return bestclustering   

    
def CLUSTERING(sba,demand,capacity):
    clusters = []
    while con.ROUTE_DEMAND(sba,demand)>capacity:        
        for i in range(1,len(sba)):            
            if con.ROUTE_DEMAND(sba[0:i+1],demand)>capacity:
                clusters.append(sba[0:i])                
                sba = np.delete(sba,range(i))
                break
    clusters.append(sba)
    for i in range(0,len(clusters)):
        clusters[i] = np.append(clusters[i],1)
        clusters[i] = np.insert(clusters[i],0,1)
    return clusters
    