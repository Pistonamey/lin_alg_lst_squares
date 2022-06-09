import numpy as np
from matplotlib import pyplot as plt

#load the dataset 1
data=np.loadtxt("dataset1.txt")

#data in col 1
a=data[:,0]
#data in col 2
b=data[:,1]

#transpose the matrix a
X = np.array([a, np.ones(len(a))]).T

#storing list squares solutions
values, _,_,_=np.linalg.lstsq(X,b, rcond=None)

#plot the scatter graph
plt.scatter(a,b)

#slope values
m=values[0]

#intercept values
c=values[1]

#equation for the line
bb=a*m+c

#plot the line
plt.plot(a,bb,color='g')

#labels
plt.xlabel("X")
plt.ylabel("Y")

#show the graph
plt.show()