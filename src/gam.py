import math

def create_basis(x, degree):
    basis = []  
    n = len(x)
    basis.append([1] * n)

    for d in range(1, degree + 1):
        basis.append([math.pow(xi, d) for xi in x])
        
    return basis
