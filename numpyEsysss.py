import numpy as np

a = np.array(list(range(10)))
b = np.array(list(range(10)))
print(a+b) #add this two arrays
print(a*b)
print(a.ndim) #number of dimension
print(a.shape) #the number of elements in column and row and...
c = np.array([[1,2,3,4],[5,6,7,8]],dtype='int64') #a 2D array
print(c.dtype)
print(c.shape)
print(c.size)
print(c[1,1]) # to access them
print(a[0:-1:2]) #you can specify the steps in arrays $# and we call this fancy indexing

d = np.arange(25).reshape(5,5)
e = d
e[0,0]=999
print(d)

print(e.flags)
print(e.data)

f = np.array([1,2,-1,-2,5,-6])
negatives = f<0 #we call this a mask
print(f[negatives]) # it give you an array of negatives
negatives = f[f<0] # it's still work
a = np.arange(25).reshape(5,5)
print(a[(a<15)&(a>5)])
b = np.zeros((5,5))
print(b)
idx = (a<15)&(a>5)
b[idx]=10
print(np.nonzero(idx)) # you can get the position of the conditions
print(b)

aLike = np.empty_like(a,dtype='float') # it give me an list like 'a' with garbage inside
aLike.fill(np.nan)
print(aLike)
aLike[idx]=10
print(aLike)

#we can do this easier
del aLike
aLike = np.where(a%3==0,a,np.nan) #it gets a boolian and put 'a' where it's True and puts 'np.nan' where it's False
print(aLike)

#to work with multi dimensions
arr = np.arange(24).reshape(6,4)
print(arr)
print(np.mean(arr,axis=0)) #it calculate the mean in columns
print(np.mean(arr,axis=1)) #it does it on the rows

print(np.max(arr)) #the maximum/minimum of the array
print(np.argmax(arr)) #it's the location of the max/min5
print(np.unravel_index(np.argmax(arr),arr.shape)) # it gives the exact location
row,col = np.where(arr==arr.max())
print(row,col)

npToList = np.arange(9).reshape(3,3).tolist()
[print(row) for row in npToList]
