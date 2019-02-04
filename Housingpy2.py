import numpy as np
import math
import ml_housing as hs

M,N,X,y,headers = hs.load_data("housing.csv")

y = X[:,4]

def h(theta, x):
    out = 0
    for i in range(M):
        if i!=4:
            out = out + theta[i]*x[i]
    out = out + theta[-1]
    sig = 1/(1+math.exp(-out))
    return sig

def cost(theta):
    out = 0
    for i in range(N):
        out = out + (h(thetas,X[i,:])-y[i])**2
    return out/2


thetas = np.zeros(M+1)
hs = []
alpha = 0.000002
for i in range(1000):
    for k in range(N):
        arr = np.zeros(M+1)
        for j in range(M+1):
            arr[j] = thetas[j]
        for j in range(M+1):
            if j==M:
                thetas[j] = thetas[j] + alpha*(y[k]-h(arr,X[k,:]))
            else:
                thetas[j] = thetas[j] + alpha*(y[k]-h(arr,X[k,:]))*X[k,j]
    hs.append(cost(thetas))
    #print(i)
    #print(hs[i])
    #if hs[i] < 10:
    #    break

print(hs[-1])
