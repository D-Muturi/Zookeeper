# input values for one mökkis: size, size of sauna, distance to water, number of indoor bathrooms,
# proximity of neighbours

x = [155, 15, 5, 1, 200]
c = [3000, 200 , -50, 5000, 100]     # coefficient values

prediction = c[0]*x[0] + c[1]*x[1] + c[2]*x[2] + c[3]*x[3] + c[4]*x[4]

print(prediction)

import numpy as np

x = np.array([66, 5, 15, 2, 500])
c = np.array([3000, 200 , -50, 5000, 100])

print(x @ c)

import numpy as np

x = np.array([[66, 5, 15, 2, 500],
              [21, 3, 50, 1, 100]])
c = np.array([3000, 200 , -50, 5000, 100])

print(x @ c)

import numpy as np


x = np.array([
             [25, 2, 50, 1, 500],
             [39, 3, 10, 1, 1000],
             [13, 2, 13, 1, 1000],
             [82, 5, 20, 2, 120],
             [130, 6, 10, 2, 600]
            ])
y = np.array([127900, 222100, 143750, 268000, 460700])

c = np.linalg.lstsq(x, y)[0]
print(c)
print(x @ c)

import numpy as np

def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)

import numpy as np

def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)