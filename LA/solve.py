# Solution of A x = b
import numpy as np
from scipy import linalg

A = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])  # 3*3 array of 3 row vectors
b = np.array([[2], [4], [-1]])                    # column vector b

x = linalg.solve(A, b)                            # solution column vector x

print()
print("Check scipy.linalg.solve for solving a set of linear equations")
print()

print("A:", A.shape)
print(A)
print()
print("b:", b.shape)
print(b)
print()

print("Solution vector x:",x.shape)
print(x)
print()

# Double-check that x is indeed a solution of A x = b
#c = np.dot(A,x)
#c = A@x
c = np.matmul(A,x)
print("c:",c.shape)
print(c)
print()
diff = c - b
print("Difference vector:",diff.shape)
print(diff)
