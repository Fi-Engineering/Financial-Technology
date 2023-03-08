def compute_average(l):
    """
    Computes the average of list, ignoring any entries that 
    are not numbers (floats or ints)

    Args:
    l(list): list of items to compute the average
 
    returns:
    average of the numbers in the list
    
    raises:
    ValueError if the argument is not a list or if the list does not contain any numbers
    """

 
    if  not isinstance(l, list):
        raise ValueError('input is not list')
        
    elif(len(l)==0):
            raise ValueError('list is empty')      
    else:
        
        ttl = 0
        numCount = 0
        for i in range(len(l)):
            
            if isinstance(l[i], int) or isinstance(l[i], float):
                ttl += l[i]
                numCount += 1
        if(numCount>0):
            avg = ttl/numCount
            return avg
        else:
            raise ValueError('list contains no numbers')      
                
                

