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
      

def make_change(amount):
     """takes amount of money returns dictionary of minimum denominations to make change for that amount """
     denoms = (10000, 5000, 2000, 1000, 500, 200, 100, 25, 10, 5, 1)
 

     amount = int(amount * 100)
     cxList = make_change_helper(amount, denoms)
     #print('cxList: \n', cxList, '\n')
     
     for i in range(len(cxList)):
         cxList[i] = list(cxList[i])
     for i in range(len(cxList)):   
         cxList[i][1] = cxList[i][1]/100
         
     #print('cxList: \n', cxList, '\n') 
     # convert to dict:
     change = {key: value for value, key in cxList} 
     
    # change = dict(cxList)
     return  change   
    


def make_change_helper(amount, denoms):
    for c in (denoms) :
        if amount >= c :
            return [(amount // c, c),] + make_change_helper( amount % c, denoms )
    return []





