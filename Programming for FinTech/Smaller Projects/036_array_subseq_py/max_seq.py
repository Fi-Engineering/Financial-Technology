# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 07:17:50 2022

@author: Alex I
      max_seq returns the longest increasing contiguous subsequence in the list.
   (as determined by length) If two or more subsequences have equal lengths,
   return the first subsequence found.
      If the l is empty, an empty list is returned.
      
      Raises:
   TypeError if the list contains an item that is not arithmetically 
   compatible with ints and floats



"""

import sys
from sys import argv

def typeError():
    raise TypeError ('list contains non-numeric values')
        


def max_seq(l):

    arrLen = len(l)
    if(arrLen==0):
        return []
    else: #
        i = 0  # 
        
        max = 1  # 
        
        start = 0  # 
        end = 0  # 
        
        beststart = 0  # 
        bestend = 0  # 
        
        while i<arrLen:
            if(not(isinstance(l[i], int) or isinstance(l[i], float))):
                typeError()
            elif i < arrLen -1 and (not(isinstance(l[i+1], int) or isinstance(l[i+1], float))):
                typeError()
            else:
                #print('i: ', i)
                if i+1 < arrLen and l[i+1]>l[i]:
                    end = end + 1  # 
                    if (end-start+1) > max:
                        max = (end - start + 1)  # 
                        beststart = start  # 
                        bestend = end  #
                else:
                    start = i+1  # re-initialize start
                    end = i+1  # re-initialize end
            
                i = i + 1
               
        return(l[beststart:bestend+1])
       
    
if __name__ == "__main__":
    if len(argv) < 2:  # check for correct number of args
        print("Usage: python3 max_seq.py l ...")
        sys.exit(1)
    max_seq(argv)


