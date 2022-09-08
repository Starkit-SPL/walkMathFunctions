import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
import scipy.interpolate
import scipy as sp



def parabolicStep( dt,  time,  period,  deadTimeFraction):

  # normalised [0,1] step up
    deadTime = period * deadTimeFraction / 2
    if (time < deadTime + dt / 2):
        return 0
  
    if (time > period - deadTime - dt / 2): 
        return 1
  
    timeFraction = (time - deadTime) / (period - 2 * deadTime)
    if (time < period / 2):
        return 2.0 * timeFraction * timeFraction
  
    return 4 * timeFraction - 2 * timeFraction * timeFraction - 1


def parabolicReturnMod(f): # normalised [0,1] up and down 

    x = 0
    y = 0
    if (f < 0.25):
        # y: 0 -> 0.75
        y = 8 * f * f * 1.50
    if (f >= 0.25 and f < 0.5):
        # y: 0.75 -> 1.00
        x = 0.5 - f
        y = 8 * x * x
        y = y / 2
        y = 1.0 - y
    if (f >= 0.5 and f < 0.75):
        # y: 1.00 -> 0.75
        x = f - 0.5
        y = 8 * x * x
        y = y / 2
        y = 1.0 - y
    if (f >= 0.75 and f <= 1.0):
        # y: 0.75 -> 0
        x = 1.0 - f
        y = 8 * x * x * 1.50
    return y


x = [0.007301001581444, 0.048582782531122, 0.094979927821256, 0.163121933417136, 0.234980333319817, 0.281499128178095, 0.369196301853128, 0.497962369733587, 0.629629779814282, 0.719936336726005, 0.757544300717732, 0.838897449414054, 0.95352175499777, 0.993003122338916]
y = [0.002952029520295, 0.029520295202952, 0.118081180811808, 0.321771217712177, 0.678228782287823, 0.811070110701107, 0.932841328413284, 1.00369003690037, 0.930627306273063, 0.802214022140221, 0.691512915129151, 0.304059040590406, 0.027306273062731, -0.001476014760148]

fp, residuals, rank, sv, rcond = np.polyfit(x, y, 4, full=True)
func1 = sp.poly1d(fp)
for i in range(len(func1) + 1):
    if i == 1:
        tmp = 'x'
    if i == 0:
        tmp = '1'
    if i != 1 and i != 0:
        tmp = 'x*' * (i - 1) + 'x'
    print(str(func1[i]) + ' * ' + tmp + ' + ' ,end='')
print()
print(func1)

fraction = np.linspace(0, 1, 1000)
rezParabolicReturnMode = [parabolicReturnMod(i) for i in fraction]
cs = CubicSpline(x, y)
plt.scatter(fraction, cs(fraction), label='new', marker='v')
plt.scatter(fraction, list(map(lambda t: func1(t), fraction)), label='NEW', marker='o')
#plt.scatter(fraction, rezParabolicReturnMode, label='old')
plt.legend()
plt.show()
tck = scipy.interpolate.splrep(fraction, rezParabolicReturnMode)
# with open('coef.txt', 'w') as coefs:
#     zero, first, second, third = cs.c[0], cs.c[1], cs.c[2], cs.c[3]
#     for step in range(len(fraction) - 1):
#         tmp = [zero[step], first[step], second[step], third[step]]
#         bound = [fraction[step], fraction[step + 1]]





t = np.linspace(0, 0.25, 25)
rezParabolicStep = [parabolicStep(0.01, i, 0.25, 0.2) for i in t]



plt.scatter(fraction, rezParabolicReturnMode)
plt.savefig('rezParabolicReturnMode.png')
plt.clf()
plt.scatter(t, rezParabolicStep)
plt.savefig('rezParabolicStep.png')




