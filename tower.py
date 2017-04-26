#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


data = np.loadtxt("droptower_vdata.txt", unpack = True)
time = data[0]
velocity = data[1]
position = integrate.cumtrapz(velocity, initial = 0) + 30
acceleration = np.diff(velocity)
acc_times = np.arange(0.5, 10.5, 1)

#Position is Blue
plt.plot(time,position,'bo:', label= "Position (m)")

#Velocity is Green
plt.plot(time,velocity,'g^-', label= "Velocity (m/s)")

#Acceleration is red
plt.plot(acc_times,acceleration, 'r*', linestyle= "dashed", label= "Acceleration (m/s^2)")

plt.title('Drop Tower Data', size = 20)
plt.xlabel('Time (Seconds)')
plt.legend()

plt.show()



