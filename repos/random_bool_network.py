import random
import numpy as np

def Random_bool_net (nodes, n , combs_num = 3):
    """
    Implemetation of the random boolean network concept:
        
    There are nodes * booleans that have 1 /0 (True/False) values, each node connects
    to 3 other nodes. Than it's value is reassigned (simulaniously) in coherence
    to Truth table that assigns random value to different combinations of n (preferably 3) bits: 000 - 111 -> 0,1,0,0,1...
    
    The process is than repeated N times.
    
    nodes = integer - number of initial bools
    n = number of repetition 
    combs_num = integer - number of digits/ connections of combinations 
    """
    bools = []
    cons = []

    
   # Intial bool values + nodes connections
   
    for node in range(nodes):
        con = []
        bools.append(np.random.randint(0,2))
        li = [i for i in range(nodes)]
        li = list(filter(lambda x: x != node, li))
        for j in range(combs_num):
            rnd = random.choice(li)
            con.append(rnd)
            li = list(filter(lambda x: x != rnd, li))
        cons.append(con)
    print(bools)
    
    
    # Setting Truth Table
    tt = []
        
    for i in range(2**combs_num):
        tt.append(np.random.randint(0,2))
        
        
    # calculating combination + rep
            
    for j in range(n):
        li = []
        for i, comb in enumerate(cons,start = 0):
            comb_bits = []
            for c in comb:
                comb_bits.append(bools[c])
            li.append(tt[from_bits(comb_bits)])
        bools = li
        print(bools)






def from_bits (bits):
    """
    convert number in base 2 to number in base 10
    Example: [1,0,1,1] ---> 1 * 2^0 + 1*2 ^1 + 0* 2^2 + 1* 2^3 = 11
    
    bits  = list describing number in bits ex([1,1,1,0])
    
    """
    res = 0
    for bit in range(len(bits) -1 ,-1,-1): 
        res += bits[bit] * 2**(len(bits)- bit -1)
    return res

    
    
Random_bool_net(20, 20)
    
    
    
    
    
    
    
        
    

    
