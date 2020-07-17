import math
import numpy as np
import parser_functions as pf
# για την ταξινομηση με βαση τη ζητηση του κομβου(η ζητηση δινεται απο τη δευτερη 
#στηλη του demand αρα το 1)  
def getKey(item):
    return item[1]

def getK(item):
    return item[2]
    

    
def SAVINGS(dm,dimension,demand,capacity):
#συναρτηση για τον υπολογισμο του συντελεστη savings για καθε πιθανη συνδεση 
#μεταξυ δυο κομβων ζητησης
    savings = np.zeros((math.floor(((dimension-2)*(dimension-1))/2),3), dtype=np.int)
    z=0
    for i in range (0,dimension):
        for j in range (0,dimension):
            if i>j and j!=0 and (demand[i][1]+demand[j][1]<=capacity):
                savings[z][0] = i
                savings[z][1] = j
                savings[z][2] = dm[i][0] + dm[j][0] - dm[i][j]
                z=z+1
    
    end1 = False
    j=0
    while end1 == False : #and len(savings)>0:
        if (savings[j][0]==0) and (savings[j][1]==0) and (savings[j][2]==0):
            savings = np.delete(savings, (j), axis=0)
            j=0
        else: 
           j=j+1
        if j==len(savings): 
           end1 = True

    savings = sorted(savings , key=getK , reverse= True) 
    #print (savings)    
    return savings
    
    
def CLARKE_WRIGHT (dm,dimension,demand,capacity):
    savings = SAVINGS(dm,dimension,demand,capacity)
    routes=[]
    
    while len(savings)>0:
        
    #κατασκευαζουμε την διαδρομη βαζοντας την πρωτη ακμη του πινακα savings
    #και στη συνεχεια τη διαγραφουμε    
        head=savings[0][0]
        tail=savings[0][1]
        middle=[]
        remaining_capacity = capacity - demand[head][1] - demand[tail][1]
        savings = np.delete(savings, (0), axis=0)        
        end = False
        i=0
        #print (len(savings))
        while end==False and len(savings)>0:
        #ξενικαμε απο την αρχη του πινακα savings. Αν καποια ακμη μπορει να
        #προστεθει στην υπαρχουσα διαδρομη χωρις να δημιουργειται κυκλος
        #και τηρώντας τους περιορισμους χωρητικοτητας, τοτε τη βαζουμε 
        #στη διαδρομη. Στη συνεχεια τη διαγραφουμε απο τον πινακα και ξεκιναμε 
        #απο την αρχη.
            if (savings[i][0]==head) and (not savings[i][1] in middle) and (savings[i][1]!=tail):
                if remaining_capacity>= demand[savings[i][1]][1]:     
                    remaining_capacity = remaining_capacity - demand[savings[i][1]][1]
                    middle.insert(0,head)
                    head = savings [i][1]
                    savings = np.delete(savings, (i), axis=0)
                    i=0
                else: 
                    i=i+1
            elif (savings[i][0]==tail) and (not savings[i][1] in middle) and (savings[i][1]!=head):
                if remaining_capacity>= demand[savings[i][1]][1]:
                    remaining_capacity = remaining_capacity - demand[savings[i][1]][1]                
                    middle.append(tail)
                    tail = savings [i][1]
                    savings = np.delete(savings, (i), axis=0)
                    i=0
                else: 
                    i=i+1
            elif (savings[i][1]==head) and (not savings[i][0] in middle) and (savings[i][0]!=tail):
                if remaining_capacity>= demand[savings[i][0]][1]:  
                    remaining_capacity = remaining_capacity - demand[savings[i][0]][1]
                    middle.insert(0,head)
                    head = savings [i][0]     
                    savings = np.delete(savings, (i), axis=0) 
                    i=0
                else: 
                    i=i+1
            elif (savings[i][1]==tail) and (not savings[i][0] in middle) and (savings[i][0]!=head):    
                if remaining_capacity >= demand[savings[i][0]][1]:
                    remaining_capacity = remaining_capacity - demand[savings[i][0]][1]                
                    middle.append(tail)
                    tail = savings [i][0]
                    savings = np.delete(savings, (i), axis=0)
                    i=0
                else: 
                    i=i+1
            else: 
                i=i+1        
            if i==len(savings) : 
                end = True
                      
        route = middle
        route.append(tail)
        route.insert(0,head)
        routes.append(route)   
        
    #διαγραφη απο τον πινακα savings ολων των ακμων του γραφου οι οποιες εχουν
    #εστω ενα ακρο που να ανηκει στη διαδρομη που δημιουργηθηκε.
        end1 = False
        j=0
        while end1 == False and len(savings)>0:
            if (savings[j][0] in route) or (savings[j][1] in route):
                savings = np.delete(savings, (j), axis=0)
                j=0
            else: 
                j=j+1
            if j==len(savings): 
                end1 = True
       
    left_out = []
    for i in range (1,dimension):
        found = False
        for j in range (0,len(routes)):
            if i in routes[j]:
                found = True
        if found == False :
            left_out.append(i)
    for i in left_out:
        routes.append([i])
    
    print (left_out)
    for i in range(0,len(routes)):
        for j in range (0,len(routes[i])): 
            routes[i][j] = routes[i][j] + 1
        routes[i].append(1)
        routes[i].insert(0,1)
        routes[i] = np.asarray(routes[i])
    print ("CLARKE WRIGHT SOLUTION")
    print ("number of vehicles: ", len(routes)) 
    customers = 0
    for x in routes: 
        print(x," cost:",ROUTE_COST(x,dm),", demand:",ROUTE_DEMAND(x,demand))
        customers = customers + len(x) - 2
    print("total cost: ",COST(routes,dm))
    print("customers: ",customers)
    print()
    return routes

#Συνάρτηση για τον υπολογισμό του κόστους μιας λύσης του προβλήματος
def COST(routes,dm):
    cost = 0
    for i in range (0,len(routes)):  cost = cost + ROUTE_COST(routes[i],dm)
    return cost    

#Συνάρτηση για τον υπολογισμό του κόστους μιας συγκεκριμένης διαδρομής μέσα σε
#μια λύση
def ROUTE_COST(route,dm):
    cost = 0
    for j in range (0,len(route)-1):
        if route[j]>route[j+1]:
            cost = cost + dm[route[j]-1][route[j+1]-1]
        else:
            cost = cost + dm[route[j+1]-1][route[j]-1]         
            
    return cost
    
#Συνάρτηση για τον υπολογισμό της συνολικής απαίτησης (demand) μιας διαδρομής        
def ROUTE_DEMAND(route,demand):
    route_demand=0
    for i in range (0,len(route)): route_demand = route_demand + demand[route[i]-1][1]
    return route_demand
    
    

        
    