# Solve eigenvalue problem
#
#   A x = lambda x
# 
import numpy as np

# Explicit stuff
A = np.zeros( (2,2) )   # Set up 2*2 matrix (numpy array) with elements initialized to zero
A[0,0] = 1
A[0,1] = 2
A[1,0] = 1
A[1,1] = 3
  
# Original matrix
print("A",A.shape)
print(A)
print("")
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalue type",type(eigenvalues))
print("Eigenvector type",type(eigenvectors))
  
# Eigenvalues of the matrix"
print("Eigenvalue shape",eigenvalues.shape)
print(eigenvalues)
lambda0 = eigenvalues[0]
lambda1 = eigenvalues[1]
print("Eigenvalues:",lambda0,lambda1)
print("")
  
# Eigenvectors of the matrix
print("Eigenvectors shape",eigenvectors.shape)
print(eigenvectors)

# Check these make sense as the right eigenvectors for eigenvalues lambda0, lambda1
vr0 = eigenvectors[:,0]
vr1 = eigenvectors[:,1]

print("vr0",vr0.shape)
print(vr0)
print()

print("vr1",vr1.shape)
print(vr1)
print()

# Test A vri  = lambdai vri for i=0,1    (Is A x = lamba x for each solution (lambda_i and x_i))
#
#
lhs0 = np.dot(A,vr0)
rhs0 = np.dot(lambda0,vr0)
print("lhs0:")
print(lhs0)
print("rhs0:")
print(rhs0)
print("lhs0-rhs0:")
print(lhs0-rhs0)

print()
lhs1 = np.dot(A,vr1)
rhs1 = np.dot(lambda1,vr1)
print("lhs1:")
print(lhs1)
print("rhs1:")
print(rhs1)
print("lhs1-rhs1:")
print(lhs1-rhs1)
