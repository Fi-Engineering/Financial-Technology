#include <stdio.h>
#include <stdlib.h>
#include <limits.h>



size_t maxSeq(int * array, size_t n)
{
	size_t maxLen = 1;
	size_t currentMaxLen =  1;
	size_t fail = -1;
	if(n==0 || array==NULL)
	{
		//return NULL;
		return fail;
	}	
	for(int i=1; i<n; i++)
	{
		if(array[i] > array[i-1])
		{
			currentMaxLen++;
		}
		else
		{
			if(maxLen < currentMaxLen)
			{
				maxLen = currentMaxLen;
			}	
			currentMaxLen = 1;
		}
		
	}
	
	if(maxLen < currentMaxLen)
		{
			maxLen = currentMaxLen;
		}	
	
    return maxLen;	
	
	
}
