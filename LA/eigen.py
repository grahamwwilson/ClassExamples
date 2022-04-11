# Solve eigenvalue problem
#
#   A x = lambda x
# 
import numpy as np

#A = np.mat("1 2 3; 1 3 4; 3 2 1")

A = np.mat("1 2; 1 3")
#A = np.array([[1,2],[1,3]])
  
# Original matrix
print("A",A.shape)
print(A)
print("")
evalue, evect = np.linalg.eig(A)

print("Eigenvalue type",type(evalue))
print("Eigenvector type",type(evect))
  
# Eigenvalues of the matrix"
print("evalue",evalue.shape)
print(evalue)
lambda0 = evalue[0]
lambda1 = evalue[1]
print("Eigenvalues:",lambda0,lambda1)
print("")
  
# Eigenvectors of the matrix
print("evect",evect.shape)
print(evect)

# Check these make sense as the right eigenvectors for eigenvalues lambda0, lambda1
vr0 = evect[:,0]
vr1 = evect[:,1]

print("vr0",vr0.shape)
print(vr0)
print()

print("vr1",vr1.shape)
print(vr1)
print()

# Test A vri  = lambdai v for i=0,1
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



 
