# Syed Hussain
# 08/14/2022
#Problem number 4 - Write a program to compute the approximation and then print that value as well as the value of
# math.pi from the math module
# Import math Library
# Initialize denominator
# Initialize sum
# even index elements are positive
# odd index elements are negative
# denominator is odd

import math
k = 1
s = 0
for i in range(1000000):
    if i % 2 == 0:
        s += 4/k
    else:
        s -= 4 / k
    k += 2
print("Value of estimated pi:" ,s)
print('Value of pi from math module: ',math.pi)
