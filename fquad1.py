#file inputs
import numpy as np
import matplotlib.pyplot as plt

 
with open("file.txt", "r") as f:
   a=float(f.readline())
   b=float(f.readline())
   c=int(f.readline())
    
x=np.linspace(0,10,100)
y=a*x**2 + b*x +c

plt.plot(x,y,c="black",lw=2)
plt.xlabel('time')
plt.ylabel('temperature')
plt.show()

