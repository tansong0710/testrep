import math
def fun_quadratic(a,b,c):
    d = math.sqrt(b**2 - 4*a*c)
    return (-b + d)/(2*a), (-b-d)/(2*a)