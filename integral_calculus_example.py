import numpy as np
from scipy.integrate import quad

def integrand(theta):
    return np.cos((1 + np.cos(theta))**3 / 3)

theta_lower = 0
theta_upper = 2 * np.pi

I1, error = quad(integrand, theta_lower, theta_upper)

I2 = (1/3) * (2 * np.pi)

I = I1 - I2
I, error
