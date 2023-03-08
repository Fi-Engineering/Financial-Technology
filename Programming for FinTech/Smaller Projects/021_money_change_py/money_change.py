

def make_change(amount):
    '''takes money amount as float, returns minimum bills/coins needed to represent input amount '''
    denoms = (10000, 5000, 2000, 1000, 500, 200, 100, 25, 10, 5, 1)
    amount = int(amount*100)
    chg = {}
    resid = amount
    d = 0
 
    while resid>0:
        val = resid // denoms[d]
       
        if(val>0):
          
            chg[denoms[d]/100] = val
          
            resid = resid % denoms[d]
            
        d += 1
        
        
    return chg
        
        
        
    
def print_change(change):
    '''takes dictionary of money amount in cents, displays change in dollars/cents format, one denomination per line '''
    
    keys = change.keys()
    vals = list(change.values())
   
    
    v = 0
    for d in keys:
        
        denom = d
        
        print('$%.2f:'%denom, end='')
        #print(' ', vals[v])
        print('', vals[v])
        v += 1
    














