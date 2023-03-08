import sys
from sys import argv

def read_key_values(filename):
    """
    Reads a key-value delimited file (separated by first =) into a dictionary

    Args:
    filename(str): name of the file to read
    
    Returns:
    dictionary of the read items
    """
    with open(filename) as f:
        #fileDict = {int(k): v for line in f for (k, v) in [line.strip().split(None, 1)]}
        fileDict = {(k): v for line in f for (k, v) in [line.strip().split('=', 1)]}
    print(fileDict)
    return fileDict


def create_output_filename(name):
    """
    create the output file name.  Given an input filename such as "input.txt",
    return "input.txt.counts"
    """
    return name + '.counts'


#def process_key_file(filename, inDict):
def process_key_file(filename, key_values):    



    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    keyList = lines
      
   
    file.close()
    vals = key_values.values()    
    valList = list(vals)
    valList = [*set(valList)]    
    
    valDict = {}
    for k in valList:
        valDict[k] = 0
   
    
    for k in keyList:
            #print('k: ', k)
            for key, value in key_values.items():
                #print('key: ', key)
                #print('value: ', value)
                if (key == k):
                   valDict[value] += 1
    # check for unknowns in keyList:
    
    unknownFound = False
   
    keysList = list(key_values.keys())    
   
    for k in keyList:
        if(k not in keysList):
           
             if (not unknownFound):
                 valDict['<unknown>'] = 1
                 unknownFound = True
             else:
                valDict['<unknown>'] += 1
                    
    
    valDict = {key:val for key, val in valDict.items() if val!=0}           
                
    print(valDict)           
    return valDict
    
    
    

def write_output(filename,vd):
    """
    Sort the output value the highest count descending. If two values are
    equal, arbitrarily choose 1
    """

        
    with open(filename, 'w') as f: 
        for key, value in vd.items(): 
            f.write('%s: %s\n' % (key, value))
                
    
    
    
def value_getter(item):
    return item[1]



#def process(kvfilename, lFile ): 
def process(argv):     
    """
    Implement your algorithm in this function
    """
  
    inDict = read_key_values(argv[1])
    
    
   
    vals = inDict.values()  
    valList = list(vals) 
    valList = [*set(valList)]    
   
    for v in range(len(argv)-2):
        vd = process_key_file(argv[v+2], inDict)
    
   
        write_output(create_output_filename(argv[v+2]), vd)
    

# __name__ == "__main__" and argv explained in the "modules" notebook
if __name__ == "__main__":
    if len(argv) < 3:
        print("Usage: python3 key_value.py file1_name file2_name ...")
        sys.exit(-1)
    
    process(argv)
