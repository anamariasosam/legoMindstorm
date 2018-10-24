import math
import numpy as np
from matplotlib  import pyplot as plt

Xob = 8
Yob = 8
v = 1

x = 0
y = 2

tetha = 0
L = 4

xc = [(0)]
yc = [(0.5)]

i = False
while i == False:
    x = -v * math.sin(tetha) + x
    y = v * math.cos(tetha) + y
    deltaX = (Xob - x) * math.cos(tetha) + (Yob - y) * math.sin(tetha)
    curvatura = -(2 * deltaX)/(L**2)
    tetha = tetha + v * curvatura
    xc.append(x)
    yc.append(y)
    print(deltaX,curvatura, math.degrees(tetha))
    if math.fabs(x) >= Xob or math.fabs(y) >= Yob:
        i = True

X2 = np.linspace(0,8,num = 101)
Y2 = X2

plt.plot(X2,Y2)
plt.plot(xc,yc)
plt.show()