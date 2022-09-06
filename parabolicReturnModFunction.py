import matplotlib.pyplot as plt
import numpy as np

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



fraction = np.linspace(0, 1, 1000)
rezParabolicReturnMode = [parabolicReturnMod(i) for i in fraction]
t = np.linspace(0, 0.25, 25)
rezParabolicStep = [parabolicStep(0.01, i, 0.25, 0.2) for i in t]



plt.scatter(fraction, rezParabolicReturnMode)
plt.savefig('rezParabolicReturnMode.png')
plt.clf()
plt.scatter(t, rezParabolicStep)
plt.savefig('rezParabolicStep.png')




