import numpy as np

# numpy version and the configuration
def q2():
    print(np.__version__)
    np.show_config()

# create a null vector of size 10
def q3():
    zeroVector = np.zeros(10)
    print(zeroVector)

# memory size of any array
def q4():
    Z = np.zeros((10,10))
    print("%d bytes" % (Z.size * Z.itemsize))

# documentation of the numpy add function from the command line
def q5():
    print('''numpy.info(numpy.add)
add(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])

Add arguments element-wise.

Parameters
----------
x1, x2 : array_like
    The arrays to be added.
    If ``x1.shape != x2.shape``, they must be broadcastable to a common
    shape (which becomes the shape of the output).
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which the result is stored. If provided, it must have
    a shape that the inputs broadcast to. If not provided or None,
    a freshly-allocated array is returned. A tuple (possible only as a
    keyword argument) must have length equal to the number of outputs.
where : array_like, optional
    This condition is broadcast over the input. At locations where the
    condition is True, the `out` array will be set to the ufunc result.
    Elsewhere, the `out` array will retain its original value.
    Note that if an uninitialized `out` array is created via the default
    ``out=None``, locations within it where the condition is False will
    remain uninitialized.
**kwargs
    For other keyword-only arguments, see the
    :ref:`ufunc docs <ufuncs.kwargs>`.

Returns
-------
add : ndarray or scalar
    The sum of `x1` and `x2`, element-wise.
    This is a scalar if both `x1` and `x2` are scalars.

Notes
-----
Equivalent to `x1` + `x2` in terms of array broadcasting.

Examples
--------
np.add(1.0, 4.0)
5.0
x1 = np.arange(9.0).reshape((3, 3))
x2 = np.arange(3.0)
np.add(x1, x2)
array([[  0.,   2.,   4.],
       [  3.,   5.,   7.],
       [  6.,   8.,  10.]])

The ``+`` operator can be used as a shorthand for ``np.add`` on ndarrays.

x1 = np.arange(9.0).reshape((3, 3))
x2 = np.arange(3.0)
x1 + x2
array([[ 0.,  2.,  4.],
       [ 3.,  5.,  7.],
       [ 6.,  8., 10.]])''')

# null vector of size 10 but the fifth value which is 1
def q6():
    zeroVector = np.zeros(10)
    zeroVector[4] = 1
    print(zeroVector)

# vector with values ranging from 10 to 49
def q7():
    zeroVector = np.arange(10,50)
    print(zeroVector)

# Reverse a vector
def q8():
    zeroVector = np.arange(10,50)
    reverseZeroVector = zeroVector[::-1]
    print(reverseZeroVector)

# 3x3 matrix with values ranging from 0 to 8
def q9():
    vector = np.arange(9).reshape(3, 3)
    print(vector)

# indices of non-zero element
def q10():
    nz = np.nonzero([1,2,0,0,4,0])
    print(nz)

# 3x3 identity matrix
def q11():
    E = np.eye(3)
    print(E)

# 3x3x3 array with random values
def q12():
    random3dArray = np.random.random((3,3,3))
    print(random3dArray)

# 10x10 array with random values and find the minimum and maximum values
def q13():
    random2dArray = np.random.random((10,10))
    print(random2dArray)
    print(random2dArray.min(), random2dArray.max())

# random vector of size 30 and find the mean value
def q14():
    randomArray = np.random.random(30)
    print(randomArray)
    print(randomArray.mean())

# 2d array with 1 on the border and 0 inside
def q15():
    randomArray = np.ones((10,10))
    randomArray[1:-1,1:-1] = 0
    print(randomArray)
#
def q16():
    pass
#
def q17():
    pass

q15()
print('END')