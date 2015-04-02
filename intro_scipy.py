
import numpy as np
from scipy import sparse,linalg
data = np.random.random((5, 6))
data[data < 0.85] = 0  # array with zeros
print data
sparse_data = sparse.csr_matrix(data) # turn data into a csr (Compressed-Sparse-Row) matrix
print sparse_data
print sparse_data.toarray()       # convert back to a dense array


#  Basic Linear Algebra

arr = np.array([[1, 2],[3, 4]])
print linalg.det(arr) # Determinant
print linalg.inv(arr) # Inverse

# SVD
arr = np.arange(9).reshape((3, 3)) + np.diag([1, 0, 1])
uarr, spec, vharr = linalg.svd(arr)
print spec
