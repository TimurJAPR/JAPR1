import numpy as np
rng = np.random.RandomState(100)

A = np.zeros((10,10))
A[5,7] = 1
print (np.nonzero(A))


