import math

def riemann_zeta(n):
    riemann = 0
    checks = 100000
    for x in range (1,checks):
        riemann = riemann + (1/(pow(x,n)))
    return (1/riemann)

random_checks = 2
print ("riemann: ", riemann_zeta(random_checks))