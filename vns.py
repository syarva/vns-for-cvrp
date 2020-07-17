import twoopt
import swap
import relocate
import threeopt
import interswap as isw
import interrelocate as ir
import construction as con
import copy
import vnd
import shake
import time

def VNS(routes,duration,cost,dm,demand,capacity,kmax):
    
    start = time.time()
    cost1 = cost
    routing = copy.deepcopy(routes)
    newroutes = vnd.VND(routing,cost,dm,demand,capacity)
    i=1
    
    while time.time() < start + duration:
        shaked = shake.SHAKE(i%kmax,newroutes,dm,demand,capacity) 
        
        optshaked = vnd.VND(shaked,cost,dm,demand,capacity)
        cost2 = con.COST(optshaked,dm)
        if cost2<cost1:
            cost1 = cost2
            newroutes = copy.deepcopy(optshaked)
            i=1
            
        else: i=i+1
    return newroutes
