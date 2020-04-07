import numpy as np
a,b,c= map(int,input().split())
if a + b + 2*np.sqrt(a*b) < c :
    print('Yes')
else :
    print('No')
