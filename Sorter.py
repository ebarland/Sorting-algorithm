from numpy import *
import matplotlib.pyplot as plt
from random import *

# Define empty array of length 500:
A = zeros(500)

# Generate random array of values between -100 and 100:
for i in range(len(A)):
    A[i] = uniform(-1, 1)*100

# Generate timeline corresponding to data in A
t = linspace(0, len(A)-1, len(A))  

# Plot the initial data-structure:
plt.plot(t, A)
plt.ylabel('Temperature')
plt.xlabel('Sensor')

# Sort the array from lowest to largest value:
holder = 0 #placeholder variable to hold an array-value while it is being moved from one place to another.
for i in range(len(A)):
    for j in range(len(A)):
        if A[i] < A[j]:
            holder = A[i]
            A[i] = A[j]
            A[j] = holder

# Plot the sorted data-structure:
plt.plot(t, A)

# Iterate through array A and identify intervals with change in value larger than 1.2:
for i in range(len(A)-1):
    if (A[i+1] - A[i])/(t[i+1] - t[i]) > 1.2:
        print 'Excessive temperatures measured between sensors at points %1d and %1d' % (t[i], t[i+1])