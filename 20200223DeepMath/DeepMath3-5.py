# 深度学习的数学 3-5
# The model has three layers, they are Input layer, Hiden layer, Output layer.
# The structure of model is 12(Input)-3(Hiden)-2(Output)
# The Hiden layer Weight is w2(12*3)，Bias is b2(3).
# The Output layer Weight is w3(3*2)，Bias is b3(2).

import numpy as np
import BoxMullerMethod
import UserMath
import TrainData
from sympy import symbols, diff


'''
# Only run once, assign initial value to w2、b2、w3 and b3.
list = BoxMullerMethod.boxmullersampling(mu=0, sigma=1, size=47)
print(list)
print(type(list))
for i in range(len(list)):
        if (i < 36):
                w2.append(round(list[i],8))
        if (i >= 36 and i < 39):
                b2.append(round(list[i],8))
        if (i >= 39 and i < 45):
                w3.append(round(list[i],8))
        if (i >= 45 and i < 47):
                b3.append(round(list[i],8))
print(w2)
print(b2)
print(w3)
print(b3)
'''


# For
# 00-31 positive solution variable t1 = 1, t2 = 0.
# 32-64 positive solution variable t1 = 0, t2 = 1.
data = ([[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
        [[0, 1, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
        [[1, 1, 0], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 1, 0]],
        [[1, 1, 1], [1, 0, 1], [1, 0, 1], [0, 1, 1]],
        [[0, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[0, 0, 0], [1, 1, 0], [1, 0, 1], [1, 1, 1]],
        [[0, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 0]],
        [[0, 0, 0], [1, 1, 1], [1, 0, 1], [0, 1, 1]],
        [[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 0]],
        [[0, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 0]],
        [[1, 1, 0], [1, 0, 1], [1, 1, 1], [0, 0, 0]],
        [[1, 1, 1], [1, 0, 1], [1, 1, 0], [0, 0, 0]],
        [[1, 1, 1], [1, 0, 1], [0, 1, 1], [0, 0, 0]],
        [[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 0, 1], [1, 0, 0], [1, 1, 1]],
        [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1]],
        [[1, 1, 1], [1, 0, 1], [0, 0, 1], [1, 1, 1]],
        [[1, 1, 1], [0, 0, 1], [1, 0, 1], [1, 1, 1]],
        [[0, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
        [[0, 1, 1], [1, 0, 0], [0, 0, 1], [1, 1, 1]],
        [[0, 1, 1], [1, 0, 1], [1, 0, 0], [1, 1, 1]],
        [[0, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1]],
        [[0, 1, 1], [1, 0, 1], [0, 0, 1], [1, 1, 1]],
        [[0, 1, 1], [0, 0, 1], [1, 0, 1], [1, 1, 1]],
        [[1, 1, 0], [1, 0, 0], [1, 0, 1], [1, 1, 1]],
        [[1, 1, 0], [1, 0, 1], [1, 0, 0], [1, 1, 1]],
        [[1, 1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1]],
        [[1, 1, 0], [1, 0, 1], [0, 0, 1], [1, 1, 1]],
        [[1, 1, 0], [0, 0, 1], [1, 0, 1], [1, 1, 1]],
        [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]],
        [[1, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]],
        [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]],
        [[0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 0]],
        [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 1]],
        [[1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 0]],
        [[1, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 1]],
        [[1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]],
        [[0, 1, 0], [0, 1, 1], [0, 1, 0], [0, 1, 0]],
        [[0, 1, 0], [0, 1, 0], [0, 1, 1], [0, 1, 0]],
        [[1, 1, 0], [0, 1, 1], [0, 1, 0], [0, 1, 0]],
        [[1, 1, 0], [0, 1, 0], [0, 1, 1], [0, 1, 0]],
        [[0, 1, 0], [0, 1, 1], [0, 1, 0], [1, 1, 0]],
        [[0, 1, 0], [0, 1, 0], [0, 1, 1], [1, 1, 0]],
        [[0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]],
        [[1, 1, 0], [0, 1, 1], [0, 1, 1], [1, 1, 1]],
        [[1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 0]],
        [[0, 1, 1], [0, 1, 1], [0, 1, 1], [0, 1, 1]],
        [[1, 1, 0], [1, 1, 0], [0, 1, 0], [0, 1, 0]],
        [[1, 1, 0], [0, 1, 0], [1, 1, 0], [0, 1, 0]],
        [[1, 1, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0]],
        [[1, 1, 0], [0, 1, 0], [0, 0, 0], [0, 1, 0]],
        [[0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 0, 0]],
        [[1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]],
        [[1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1]],
        [[0, 1, 0], [0, 0, 0], [0, 1, 0], [1, 1, 0]],
        [[0, 1, 0], [0, 1, 0], [0, 0, 0], [1, 1, 0]],
        [[0, 0, 0], [0, 1, 0], [0, 1, 0], [1, 1, 0]],
        [[0, 0, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]],
        [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 0, 0]],
        [[0, 1, 0], [0, 0, 1], [0, 0, 1], [0, 1, 0]],
        [[0, 1, 0], [1, 0, 0], [1, 0, 0], [0, 1, 0]])

# Hiden layer weights and bias
w2 = np.array([[
    -0.45444516, -1.83510657, 1.27247984, -1.45458804, 1.08766694, -0.37151135,
    -0.8573246, -0.05739722, -1.4002747, 0.42005857, 0.99200974, -0.87716348
],
               [
                   0.0327783, -0.72105977, -0.7385377, 0.06201517, 0.29853099,
                   -0.26401057, 0.3584689, 0.08528764, -0.30570022,
                   -0.54182688, -0.22010296, 0.75816668
               ],
               [
                   -0.75117284, 0.27116044, -0.60955939, -0.2098032,
                   0.38849476, -0.44462426, 2.00073451, 0.34762639,
                   -1.22162309, -0.86771674, -1.46696489, 0.69337321
               ]],
              dtype=float)
# eg: w2[0][0], w2[1][5], w2[2][11]
b2 = np.array([[0.19351774], [-1.53711558], [-1.66900736]], dtype=float)
# eg: b2[0], b2[1], b2[2]

# Output layer weights and bias
w3 = np.array([[1.03787369, 0.96802939, -1.68155971],
               [1.07910857, 1.12244615, 0.2843331]],
              dtype=float)
# eg: w3[0][0], w3[1][2]
b3 = np.array([[0.3667967], [-0.77614244]], dtype=float)
# eg: b3[0], b3[1]

lr = 0.001 # Learning rate.
steps = 10 # Steps.

# Save Initial Value of w2, b2, w3, b3 for backup.
SaveInitialVal_w2 = w2
SaveInitialVal_b2 = b2
SaveInitialVal_w3 = w3
SaveInitialVal_b2 = b3

a1 = np.zeros((12, 1))

# Steps
for step in range(0, steps):

        CostFunAll = 0
        PDcw3All = np.zeros((2, 3))
        PDcb3All = np.zeros((2, 1))
        PDcw2All = np.zeros((3, 12))
        PDcb2All = np.zeros((3, 1))

        for No in range(0, 64):
                # No = 0
                a1[0][0] = data[No][0][0]
                a1[1][0] = data[No][0][1]
                a1[2][0] = data[No][0][2]
                a1[3][0] = data[No][1][0]
                a1[4][0] = data[No][1][1]
                a1[5][0] = data[No][1][2]
                a1[6][0] = data[No][2][0]
                a1[7][0] = data[No][2][1]
                a1[8][0] = data[No][2][2]
                a1[9][0] = data[No][3][0]
                a1[10][0] = data[No][3][1]
                a1[11][0] = data[No][3][2]

                # Compute the values of Hidden layer.
                z2 = np.zeros((3, 1))
                z2 = np.dot(w2, a1) + b2
                # Activation function: Sigmoid(x) = 1/(1+exp(-x))
                a2 = np.zeros((3, 1))
                a2 = UserMath.Sigmoid(z2)

                # Compute the values of Output layer.
                z3 = np.zeros((2, 1))
                z3 = np.dot(w3, a2) + b3
                # Activation function: Sigmoid(x) = 1/(1+exp(-x))
                a3 = np.zeros((2, 1))
                a3 = UserMath.Sigmoid(z3)

                # Positive solution variable
                # If data is 0.
                if (No < 32):
                        t1 = 0
                        t2 = 1
                # If data is 1.
                else:
                        t1 = 1
                        t2 = 0

                CostFun = (1/2*(np.square(a3[0][0]-t1)+np.square(a3[1][0]-t2)))

                # Neural unit error.
                # Delta3[0][0], Delta3[1][0].
                Delta3 = np.zeros((2 ,1))
                # Delta3[0][0] = (UserMath.Sigmoid(z3[0][0])-t1) * UserMath.Sigmoid(z3[0][0]) * (1-UserMath.Sigmoid(z3[0][0]))
                # Delta3[1][0] = (UserMath.Sigmoid(z3[1][0])-t2) * UserMath.Sigmoid(z3[1][0]) * (1-UserMath.Sigmoid(z3[1][0]))
                t = np.zeros((2, 1))
                t[0][0] = t1
                t[1][0] = t2
                Delta3 = (UserMath.Sigmoid(z3)-t) * UserMath.SigmoidDerivative(z3)
                # Delta2[0][0], Delta2[1][0], Delta[2][0].
                Delta2 = np.zeros((3, 1))
                # Delta2[0][0] = (Delta3[0][0]*w3[0][0] + Delta3[1][0]*w3[1][0]) * UserMath.Sigmoid(z2[0][0])*(1-UserMath.Sigmoid(z2[0][0]))
                # Delta2[1][0] = (Delta3[0][0]*w3[0][1] + Delta3[1][0]*w3[1][1]) * UserMath.Sigmoid(z2[1][0])*(1-UserMath.Sigmoid(z2[1][0])) 
                # Delta2[2][0] = (Delta3[0][0]*w3[0][2] + Delta3[1][0]*w3[1][2]) * UserMath.Sigmoid(z2[2][0])*(1-UserMath.Sigmoid(z2[2][0])) 
                Delta2 = np.dot(Delta3.T, w3).T * UserMath.SigmoidDerivative(z2)
                # print(Delta3, Delta2)

                # Gradient Compute.
                # Partial Derivative
                PDcw3 = np.zeros((2, 3))
                for i in range(0, 3):
                        for j in range(0, 2):
                                PDcw3[j][i] = Delta3[j][0] * a2[i][0]
                
                PDcb3 = np.zeros((2, 1))
                for i in range(0, 2):
                        PDcb3[i][0] = Delta3[i][0]

                PDcw2 = np.zeros((3, 12))
                for i in range(0, 12):
                        for j in range(0, 3):
                                PDcw2[j][i] = Delta2[j][0] * a1[i][0]

                PDcb2 = np.zeros((3, 1))
                for i in range(0, 3):
                        PDcb2[i][0] = Delta2[i][0]
                
                PDcw3All = PDcw3All + PDcw3
                PDcb3All = PDcb3All + PDcb3
                PDcw2All = PDcw2All + PDcw2
                PDcb2All = PDcb2All + PDcb2
                CostFunAll = CostFunAll + CostFun
                
                #print(str(No) + 'CostFun' + str(CostFun))
                #print(str(No) + 'PDcw3' + str(PDcw3))
        #print(CostFunAll)
        #print(PDcw3All)

        # Gradient Partial Descent.
        GPDcw3 = PDcw3All * (-lr)
        GPDcb3 = PDcb3All * (-lr)
        GPDcw2 = PDcw2All * (-lr)
        GPDcb2 = PDcb2All * (-lr)

        w3 = w3 + GPDcw3
        b3 = b3 + GPDcb3
        w2 = w2 + GPDcw2
        b2 = b2 + GPDcb2
        
        # CostFunAll = (1/2*(np.square(a3[0][0]-t1)+np.square(a3[1][0]-t2)))
        print(CostFunAll)

# Final results.
print(CostFunAll)
print(b3)
print(w3)

'''
        # Print results.
        # print('---------------------Steps:'+str(step)+'---------------------')
        print('------------------w3:------------------')
        print(w3)
        print('------------------b3:------------------')
        print(b3)
        print('------------------w2:------------------')
        print(w2)
        print('------------------b2:------------------')
        print(b2)
        # print('------------------------CostFun:------------------------')
        print(b2[0][0])
        # print('------------------------CostFun:------------------------')

print('------------------w3:------------------')
print(w3)
print('------------------b3:------------------')
print(b3)
print('------------------w2:------------------')
print(w2)
print('------------------b2:------------------')
print(b2)

'''
