"""
Exercise 2: methods for vectors represented as Numpy 1*3 arrays
"""
import math 
import numpy as np

#The square magnitude of some vector, v
def sqrmag(v):
    return v[0]**2+v[1]**2+v[2]**2


#The magnitude of some vector, v
def mag(v):
    return math.sqrt(v[0]**2+v[1]**2+v[2]**2)

#Some vector, v, multiplied by scalar constant, k
def scalarM(v,k):
    return v*k


#Some vector, v, divided by scalar constant, k
def scalarD(v,k):
    return v/k

#The sum of two vectors
def sum(v,w):
    a = v[0]+w[0]
    b = v[1]+w[1]
    c = v[2]+w[2]
    return np.array([a,b,c])

#The difference between two vectors
def diff(v,w):
    a = v[0]-w[0]
    b = v[1]-w[1]
    c = v[2]-w[2]
    return np.array([a,b,c])

#The cross product of two vectors where we calculate each individual element (a,b,c) and then put them into an array
def cross(v,w):
    a = (v[1]*w[2])-(v[2]*w[1])
    b = (v[2]*w[0])-(v[0]*w[2])
    c = (v[0]*w[1])-(v[1]*w[0])
    return np.array([a,b,c])


#The dot product of two vectors
def dot(v,w):
    return (v[0]*w[0])+(v[1]*w[1])+(v[2]*w[2])


    



