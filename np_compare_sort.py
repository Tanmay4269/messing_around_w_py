import numpy as np
#from random import randint 

# py -> 6s
# np -> 0.37s

#lis = []

#for i in range(10**7): # 10_000_000
#    lis.append(randint(0, 100))

#lis.sort()

arr = np.random.randint(10**7, size=(20, 1), dtype='int32')
np.sort(arr)