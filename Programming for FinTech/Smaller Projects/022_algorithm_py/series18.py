def series18(N):
    r = 3*N
    k = N * (-N)
    print(k, end = " ")
    x = 0
    for i in range(0,r-1):
        m = 2*i + 1
        y = k + m
        print(y, end = ' ')
        k =y
        i = i + 1
        
series18(1)
        