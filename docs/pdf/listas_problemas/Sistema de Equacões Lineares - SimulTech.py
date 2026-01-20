import numpy as np

A = np.array([[2,1,1], [-1,1,-1], [1,2,3]])
b = np.array([2,3,-10])

x = np.linalg.solve(A, b)

print(x)
