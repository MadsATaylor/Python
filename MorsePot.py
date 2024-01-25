# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 21:34:01 2020

@author: AlexandriaTaylor
"""

r = 1.40
k = 1850.0
r_eq = 1.1283
F = D * (1 - exp[-a*(r-r)])
for i in range(1000):
    rnew = r - (517.8*r_eq*(r - r_eq)/r**3)/((517.8*r_eq*(-2*r + 3*r_eq)/r**4))
    #rnew = r - (F)/((517.8*r_eq*(-2*r + 3*r_eq)/r**4))
    if abs(rnew-r) < 0.01: break
    #if abs(rnew-r) <0.01: break
    r = rnew
print(" %f, %f, %f " % (i, r, rnew-r))
