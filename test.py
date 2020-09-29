from sympy import *
import numpy as np

P1 = [330.55, 97.97, 103.28]
P2 = [319.07, 87.30, -125.34]
P3 = [508.58, 95.75, -15.32]

# x = P1[0]+f*(P2[0]-P1[0])
# y = P1[1]+f*(P2[1]-P1[1])
# z = P1[2]+f*(P2[2]-P1[2])

# x + 0*y + 0*z - f*(P2[0]-P1[0]) = P1[0]
# 0*x + y + 0*z - f*(P2[1]-P1[1]) = P1[1]
# 0*x + 0*y + z - f*(P2[2]-P1[2]) = P1[2]
# - x*(P2[0]-P1[0]) + + y*(P2[1]-P1[1])  + z*(P2[2]-P1[2]) + f= (-P3[0]*(P2[0]-P1[0]) - P3[1]*(P2[1]-P1[1]) -P3[2]*(P2[2]-P1[2]))

# f = x*(P2[0]-P1[0]) - P3[0]*(P2[0]-P1[0]) + y*(P2[1]-P1[1])  - P3[1]*(P2[1]-P1[1]) + z*(P2[2]-P1[2]) - P3[2]*(P2[2]-P1[2])
# P3[0]*(P2[0]-P1[0]) + P3[1]*(P2[1]-P1[1]) + P3[2]*(P2[2]-P1[2]) = x*(P2[0]-P1[0])  + y*(P2[1]-P1[1])   + z*(P2[2]-P1[2]) - f

A = np.matrix([
    [1,0,0,-(P2[0]-P1[0])],
    [0,1,0,-(P2[1]-P1[1])],
    [0,0,1,-(P2[2]-P1[2])],
    [(P2[0]-P1[0]), (P2[1]-P1[1]), (P2[2]-P1[2]), -1]
])

b = np.transpose(np.matrix([
    [P1[0], P1[1], P1[2], P3[0]*(P2[0]-P1[0]) + P3[1]*(P2[1]-P1[1]) + P3[2]*(P2[2]-P1[2]) ]
]))

sol = np.linalg.solve(A,b)
x = sol[0]
y = sol[1]
z = sol[2]
f = sol[3]

print(A)
print(b)
print(sol)

# f - (x-P3[0])*(P2[0]-P1[0]) + (y-P3[1])*(P2[1]-P1[1]) + (z-P3[2])*(P2[2]-P1[2]) = 0
# f = eval(solve((x-P3[0])*(P2[0]-P1[0]) + (y-P3[1])*(P2[1]-P1[1]) + (z-P3[2])*(P2[2]-P1[2]), f))