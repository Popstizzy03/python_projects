from scipy import integrate

def integrand(z, y, x):
    return 1  

def z_limit(y, x):
    return 0, 4 - y**2

def y_limit(x):
    return 0, 2

x_lower = 0
x_upper = 3

result, error = integrate.tplquad(integrand, 0, 3, lambda x: 0, lambda x: 2, lambda x, y: 0, lambda x, y: 4 - y**2)

print(f"The result of the triple integral is: {result}") 
#The answer is 16
