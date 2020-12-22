# -*- coding: utf-8 -*-

import math

print("The First Programming Encounter: a Formula")

v0 = initial_velocity = 5
g = acceleration_of_gravity = 9.81
TIME = 0.6
VerticalPositionOfBall = initial_velocity*TIME - \
    0.5*acceleration_of_gravity*TIME**2
print("The Vertical Position Of The Ball is {} meters".format(VerticalPositionOfBall))

yc = 0.2

t1 = (v0 - math.sqrt(v0**2 - 2*g*yc))/g
t2 = (v0 + math.sqrt(v0**2 - 2*g*yc))/g

print('At t={:.2f} s and {:.2f} s, the height is {} m.'.format(t1, t2, yc))

# Calculation of sinh using exponential function

x = 2*math.pi
r1 = math.sinh(x)
r2 = 0.5 * (math.exp(x) - math.exp(-x))
r3 = 0.5 * (math.e**(x) - math.e**(-x))

print (r1, r2, r3)