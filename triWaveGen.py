
import numpy as np
import matplotlib.pyplot as plt

def calculateTri(n,l,t):
    y=0
    for i in range(1,n+1):
        if i%2!=0:
            y=y+(-1)**((i-1)/2)*np.sin(i*np.pi*t/l)/i**2
    y=8*y/np.pi**2
    return y
    
    
t = np.linspace(0,100,1000)
f = 50
plt.ion()
for j in range(1,100):
    y = calculateTri(j,f,t)
    plt.plot(t,y)
    plt.draw()
    plt.pause(0.05)
    plt.clf()


