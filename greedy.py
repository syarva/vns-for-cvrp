import numpy as np
import construction as con

"""
Απληστη μέθοδος για την κατασκευή μιας αρχικής λύσης:
Καλείται η συνάρτηση GREEDY η οποία αρχικά κατασκευάζει μια λίστα
με τους διαθέσιμους κόμβους. Στη συνέχεια καλείται η συνάρτηση 
BUILDROUTE η οποια φτιάχνει μια διαδρομή με τους διαθέσιμους κόμβους
ως εξής: επισκέπτεται κάθε φόρα τον κοντινότερο κόμβο που μπορεί να
εξυπηρετήσει καλώντας τη συνάρτηση FINDNEXT και στη συνέχεια τον 
διαγράφει από τη λίστα των διαθέσιμων κόμβων.

"""
def FINDNEXT(available,cap,dm,demand,current):
    minimum = 100000000000
    nexts = -1
    for i in available:
        if demand[i-1][1]<=cap and dm[i-1][current-1]+dm[current-1][i-1]<minimum:
            minimum = max(dm[i-1][current-1],dm[current-1][i-1])
            nexts = i
    return nexts

def BUILDROUTE(available,capacity,dm,demand):
    current = 1
    route = [1]
    cap = capacity
    nextstep = FINDNEXT(available,cap,dm,demand,current)
    while nextstep != -1:        
        route.append(nextstep)
        current = nextstep
        cap = cap - demand[nextstep-1][1]
        for i in available:
            if i == nextstep:
                available.remove(i)
        nextstep = FINDNEXT(available,cap,dm,demand,current)
    route.append(1)
    route = np.asarray(route)
    return route
            
def GREEDY(capacity,dm,demand,dimension):
    routes = []
    available = list(range(2, dimension+1))
    while len(available)>0:
        route = BUILDROUTE(available,capacity,dm,demand)
        routes.append(route)
    print ("GREEDY SOLUTION")
    print ("number of vehicles: ", len(routes)) 
    for x in routes: print(x," cost:",con.ROUTE_COST(x,dm),", demand:",con.ROUTE_DEMAND(x,demand))  
    print("total cost: ",con.COST(routes,dm))
    print()
    return routes
    
            