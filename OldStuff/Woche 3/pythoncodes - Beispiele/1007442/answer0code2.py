from numpy import *

a = array([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9])
b = ones((25, 18))

# xb = a: solve b.T x.T = a.T instead 
x2 = linalg.lstsq(b.T, a.T)[0]
x2 = dot(a, linalg.pinv(b)) 
