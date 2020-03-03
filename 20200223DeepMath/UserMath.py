import numpy as np
from scipy.misc import derivative
from sympy import symbols, diff

def Sigmoid(x):
        return 1/(1+np.exp(-x))

# def SigmoidDerivative(x):
#         return Sigmoid(x) * (1-Sigmoid(x))

def SigmoidDerivative(x):
        return derivative(Sigmoid, x, dx=1e-6)

def PartialDerivative(z, x):
        diff(z, x)
'''
PartialDerivativeTemplate:
>>> from sympy import symbols, diff
>>> x, y = symbols('x y', real=True)
>>> diff( x**2 + y**3, y)
3*y**2
>>> diff( x**2 + y**3, y).subs({x:3, y:1})
3
'''