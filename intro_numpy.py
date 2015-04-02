import numpy as np
print 'numpy version: ', np.__version__

## Basics

data  = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
rows,col = np.shape(data)

print "  Data : \n", data
print "  Rows : ", rows
print "  Col  : ", col
print "  Size : ", np.size(data) 
print "  Dim  : ", np.ndim(data)

print "  Zero's Array : \n",np.zeros((3,4))
print "  One's Array  : \n",np.ones((3,4))
print "  Empty Array  : \n",np.empty((2,1))
print "  Identity  : \n ", np.identity(3)

print np.random.rand(4,5) # uniform random numbers in [0,1]

data = np.array([1.7, 1.2, 1.6])
print data.astype(int)           # casting : truncates to integer

print np.eye(3, k=1) # Return a 2-D array with ones on the diagonal and zeros elsewhere.
print np.diag(np.arange(5)) # np.arange() : Return evenly spaced values within a given interval.
                            # np.diag() : Extract a diagonal or construct a diagonal array.

print np.tile(np.array([[6, 7], [8, 9]]), (2, 2)) # Construct an array by repeating A the number of times given by reps.
print np.arange(4).reshape(2,2) # Gives a new shape to an array without changing its data.

X, Y = np.mgrid[0:5, 0:5] # Returns : mesh-grid `ndarrays` all of the same dimensions 
print X
print Y

#  Basic Linear Algebra

X = np.array([[1, 2],[3, 4]])

print X.T # Transpose
print X.min()
print X.max()
print X*5 # Scalar expansion

print X*X.T       # Elementwise product
print np.dot(X,X.T)  # Dot (matrix) product
