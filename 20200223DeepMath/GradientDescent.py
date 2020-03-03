import numpy as np
from sympy import symbols, diff

# Function: z = x**2 + y**2
xsym, ysym, zsym = symbols('xsym ysym zsym', real = True)
zsym = xsym**2 + ysym**2

x = 3
y = 2
lr = 0.1 # Learning rate
step = 10 # Learning times

print('---------Begin:------------')
for i in range(1, 30):
    # Partial Derivative
    z = x**2 + y**2
    print('z:' + str(z))
    
    PDzx = diff(zsym,xsym).subs({xsym:x})
    PDzy = diff(zsym,ysym).subs({ysym:y})
    print('PDzx:' + str(PDzx) + ' | PDzy:' + str(PDzy))

    # Gradient Descent
    GPDzx = PDzx * (-lr)
    GPDzy = PDzy * (-lr)
    print('GPDzx:'+ str(GPDzx) + ' | GPDzy' + str(GPDzy))

    x = x + GPDzx
    y = y + GPDzy
    print('x:' + str(x) + ' | y:' + str(y))

    print('---------Step:'+ str(i) +'------------')




