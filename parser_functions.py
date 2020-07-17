import math
import numpy as np

def OPENFILE(x):
    file = open(x+".txt","r") 
    lines = file.readlines()
    file.close
    for y in range (0,len(lines)):  
        lines[y]= lines[y].strip()
    return lines

def DATA(x):
    lines = OPENFILE("data")     
    found = False
    i = 1
    while found == False:
        if lines[i][0:len(x)]==x: 
            found = True
        else:
            i = i + 1
            
    #capacity  = CAPACITY(x)
    #trucks    = int(lines[i][7:12]) 
    value     = int(lines[i][24:len(lines[i])])    
    #data      = np.array([trucks,value,capacity])
    return value    
    
#διαβαζει το αρχειο και επιστρεφει μια λιστα με τη ζητηση του κάθε κομβου    
def DEMAND(x):
    lines = OPENFILE(x)
    i,j = 0,0
    #η ζητηση του καθε κομβου δινεται στο κομματι του αρχειου αναμεσα απο εκει
    #που γραφει demand section και depot section    
    for x in range (0,len(lines)):
        if lines[x]=="DEMAND_SECTION":
            i = x
        if lines[x]=="DEPOT_SECTION":
            j = x   
            
    demand = np.zeros((j-i-1,2), dtype=np.int)
    for z in range (i+1,j):
        columns = lines[z].split()
        demand[z-i-1,0] = columns[0]
        demand[z-i-1,1] = columns[1]        
    return demand
    
def CAPACITY(x):
     # γνωριζουμε οτι στην 6η γραμμη γραφει το capacity. Το βρισκω και το κανω int.
     lines = OPENFILE(x)
     for line in lines:
         if 'CAPACITY :' in line:
             capacity = int(line[10:len(line)])
     return capacity    
    
def COORD(instance,dim):
    #δημιουργια λιστας που θα περιεχει τις συντεταγμενες των κομβων
    coord= np.zeros((dim,3), dtype=np.int)                
    lines = OPENFILE(instance)
    #οι συντεταγμενες αρχιζουν απο την 8η γραμμη            
    for i in range (7,7+dim):
        columns = lines[i].split()
        coord[i-7,0] = columns[0]
        coord[i-7,1] = columns[1]
        coord[i-7,2] = columns[2]    
    return coord
    
#Calculates the Euclidean distance between 2 points (x1,y1) and (x2,y2)       
def EUCLIDEAN_DISTANCE(x1,y1,x2,y2):           
    (xdiff,ydiff) = (x1-x2, y1-y2)
    dist = math.sqrt(xdiff * xdiff + ydiff * ydiff) + 0.5
    return math.floor(dist) 
        
def DISTANCE_MATRIX(x,dimension):
    lines = OPENFILE(x)    
    dm = np.zeros((dimension,dimension), dtype=np.int)
    if "EXPLICIT" in lines[4]:
    #φτιαχνουμε τον πινακα αποστασεων. Έχει μονο τις τιμες κατω απο τη διαγωνιο και
    #ολες οι υπολοιπες ειναι 0. Σε αυτη τη συναρτηση δεν εχουμε συντεταγμενες αλλα 
    #δινονται οι αποστασεις στο txt αρχειο σε μορφη explicit low diagonal row
        
        n = math.floor((dimension*(dimension-1))/2)
        c = np.zeros((n,), dtype=np.int)        
        b = math.floor(n/10)   
        c=[]
        for x in range (9,9+b+1):
            columns = lines[x].split()
            c.extend(columns)

        m=0
        for i in range (0,dimension):
            for j in range (0,dimension):
                if i>j:                       
                    dm[i][j] = c[m]
                    m=m+1 
        print (dm)
        return dm
    
    elif "EUC_2D" in lines[4]:
    #φτιαχνουμε τον πινακα αποστασεων απο τις συντεταγμενες. Έχει μονο τις 
    #τιμες κατω απο τη διαγωνιο και ολες οι υπολοιπες ειναι 0  
        coord = COORD(x,dimension)    
        for i in range (0,dimension):
            for j in range (0,dimension):
                if i>j:                       
                    dm[i][j] = EUCLIDEAN_DISTANCE(coord[i][1],coord[i][2],coord[j][1],coord[j][2])
        print (dm)
        return dm        
    else: return
        
        