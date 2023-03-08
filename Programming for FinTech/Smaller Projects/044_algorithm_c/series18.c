

# include <stdio.h>
# include <stdlib.h>

/* 
int series18(int N)
{
     int r = 3 * N;
	 int k = N * (-N);
	 printf(" %d",k);
	 //int x = 0;
	 for(int i=0; i<r-1; i++)
	 {
	     int m = 2*i + 1;
		 int y = k + m;
		 printf(" %d",y);
		 k = y;	 
	 }
    

}
*/

int series18(int n) {
	int next = -n*n;
	int offset = 0;
	for (int i = 0; i < n*3; i++) {
		if (i > 0) {
			offset = (i*2)-1;
		}
		next = next + offset;
		printf("%d ", next);
	}
	printf("\n");

return 0;
}

int main(int argc, char *argv[])
{
	
	
	if (argc < 2) {
        printf("N not specified\n");
        printf("usage: series18 N\n");
        return 1;
    }
    int n = atoi(argv[1]);
    series18(n);
	
    return 0;
	

}




