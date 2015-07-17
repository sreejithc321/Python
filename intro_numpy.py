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



## Ref : http://www.labri.fr/perso/nrougier/teaching/numpy.100/index.html

# Import the numpy package under the name np
import numpy as np

# Print the numpy version and the configuration.
print np.__version__
print np.__config__.show()

# Create a null vector of size 10
Z = np.zeros(10)
print Z

# Create a null vector of size 10 but the fifth value which is 1
Z = np.zeros(10)
Z[4] = 1
print Z

# Create a vector with values ranging from 10 to 49
Z = np.arange(10,50)
print Z

# Create a 3x3 matrix with values ranging from 0 to 8

Z = np.arange(9).reshape(3,3)
print Z

# Find indices of non-zero elements from [1,2,0,0,4,0]
nz = np.nonzero([1,2,0,0,4,0])
print nz

# Create a 3x3 identity matrix
Z = np.eye(3)
print Z

# Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
Z = np.diag(1+np.arange(4),k=-1)
print Z

# Create a 3x3x3 array with random values
Z = np.random.random((3,3,3))
print Z


