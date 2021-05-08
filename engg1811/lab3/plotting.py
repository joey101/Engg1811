
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Lecture Week 02 

Plots the bearings and angles

Writing your first function 

"""
import matplotlib.pyplot as plt

bearing = [0, 60, 90, 150, 180, 240, 269, 270, 310, 360];
angle =   [90, 30, 0, 300,-90, 210, -179, 180, 140,90];

grad_low = (240 - 150) / (210 -300)
y_low = 90

# grad_high = 
# y_high = 


fig1 = plt.figure() # Create the table
plt.plot(bearing, angle, 'x') # Plot the axis which i have specified

plt.show() # This prints the actual plot out


plt.xlabel('Bearing') # Label for the X- Axis
plt.ylabel('Angle') # Label for the Y- Axis
fig1.savefig('bangle.png') # Save theplot as a png