import numpy as np
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
y=np.array([[9,8,7],[6,5,4],[3,2,1]])
z=np.dot(x,y)
print(z)
p=x @ y
print(p)
