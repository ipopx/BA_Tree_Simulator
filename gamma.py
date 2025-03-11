from scipy.special import gamma, factorial
import numpy as np

delta = -0.4

constant = 2*(2+delta)*gamma(3+2*delta)/gamma(1+delta)
infinite_sum = 0
for k in range(2, 150):
    infinite_sum += np.sqrt(k-1) * gamma(k+delta)/gamma(k+3+2*delta)

print(constant*infinite_sum)