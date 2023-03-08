def series18(n):
    
#include <stdio.h>

int series18(int N)
{
     int r = 3 * N;
     int k = N * (-N);
     printf(" %d",k);
     int x = 0;
     for(int i=0; i<r-1; i++)
     {
         int m = 2*i + 1;
         int y = k + m;
         printf(" %d",y);
         k = y;  
     }
    

}


    pass

series18(1)
series18(5)
series18(7)
series18(12)
