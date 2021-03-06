import numpy as np

# Training data
# 1-32 positive solution variable t1 = 1, t2 = 0.
data1 = [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]]
data2 = [[0, 1, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]]
data3 = [[1, 1, 0], [1, 0, 1], [1, 0, 1], [1, 1, 1]]
data4 = [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 1, 0]]
data5 = [[1, 1, 1], [1, 0, 1], [1, 0, 1], [0, 1, 1]]
data6 = [[0, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]]
data7 = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
data8 = [[0, 0, 0], [1, 1, 0], [1, 0, 1], [1, 1, 1]]
data9 = [[0, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 0]]
data10 = [[0, 0, 0], [1, 1, 1], [1, 0, 1], [0, 1, 1]]
data11 = [[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 0]]
data12 = [[0, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 0]]
data13 = [[1, 1, 0], [1, 0, 1], [1, 1, 1], [0, 0, 0]]
data14 = [[1, 1, 1], [1, 0, 1], [1, 1, 0], [0, 0, 0]]
data15 = [[1, 1, 1], [1, 0, 1], [0, 1, 1], [0, 0, 0]]
data16 = [[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]]
data17 = [[1, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 1]]
data18 = [[1, 1, 1], [1, 0, 1], [1, 0, 0], [1, 1, 1]]
data19 = [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1]]
data20 = [[1, 1, 1], [1, 0, 1], [0, 0, 1], [1, 1, 1]]
data21 = [[1, 1, 1], [0, 0, 1], [1, 0, 1], [1, 1, 1]]
data22 = [[0, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]]
data23 = [[0, 1, 1], [1, 0, 0], [0, 0, 1], [1, 1, 1]]
data24 = [[0, 1, 1], [1, 0, 1], [1, 0, 0], [1, 1, 1]]
data25 = [[0, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1]]
data26 = [[0, 1, 1], [1, 0, 1], [0, 0, 1], [1, 1, 1]]
data27 = [[0, 1, 1], [0, 0, 1], [1, 0, 1], [1, 1, 1]]
data28 = [[1, 1, 0], [1, 0, 0], [1, 0, 1], [1, 1, 1]]
data29 = [[1, 1, 0], [1, 0, 1], [1, 0, 0], [1, 1, 1]]
data30 = [[1, 1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1]]
data31 = [[1, 1, 0], [1, 0, 1], [0, 0, 1], [1, 1, 1]]
data32 = [[1, 1, 0], [0, 0, 1], [1, 0, 1], [1, 1, 1]]

# 33-64 positive solution variable t1 = 0, t2 = 1.
data33 = [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
data34 = [[1, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
data35 = [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
data36 = [[0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 0]]
data37 = [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 1]]
data38 = [[1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 0]]
data39 = [[1, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 1]]
data40 = [[1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]]
data41 = [[0, 1, 0], [0, 1, 1], [0, 1, 0], [0, 1, 0]]
data42 = [[0, 1, 0], [0, 1, 0], [0, 1, 1], [0, 1, 0]]
data43 = [[1, 1, 0], [0, 1, 1], [0, 1, 0], [0, 1, 0]]
data44 = [[1, 1, 0], [0, 1, 0], [0, 1, 1], [0, 1, 0]]
data45 = [[0, 1, 0], [0, 1, 1], [0, 1, 0], [1, 1, 0]]
data46 = [[0, 1, 0], [0, 1, 0], [0, 1, 1], [1, 1, 0]]
data47 = [[0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]]
data48 = [[1, 1, 0], [0, 1, 1], [0, 1, 1], [1, 1, 1]]
data49 = [[1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 0]]
data50 = [[0, 1, 1], [0, 1, 1], [0, 1, 1], [0, 1, 1]]
data51 = [[1, 1, 0], [1, 1, 0], [0, 1, 0], [0, 1, 0]]
data52 = [[1, 1, 0], [0, 1, 0], [1, 1, 0], [0, 1, 0]]
data53 = [[1, 1, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0]]
data54 = [[1, 1, 0], [0, 1, 0], [0, 0, 0], [0, 1, 0]]
data55 = [[0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 0, 0]]
data56 = [[1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
data57 = [[1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1]]
data58 = [[0, 1, 0], [0, 0, 0], [0, 1, 0], [1, 1, 0]]
data59 = [[0, 1, 0], [0, 1, 0], [0, 0, 0], [1, 1, 0]]
data60 = [[0, 0, 0], [0, 1, 0], [0, 1, 0], [1, 1, 0]]
data61 = [[0, 0, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
data62 = [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 0, 0]]
data63 = [[0, 1, 0], [0, 0, 1], [0, 0, 1], [0, 1, 0]]
data64 = [[0, 1, 0], [1, 0, 0], [1, 0, 0], [0, 1, 0]]

# Assign values to each varibale in the Input layer.
a1 = np.empty((12, 1))
a1[0][0] = data1[0][0]
a1[1][0] = data1[0][1]
a1[2][0] = data1[0][2]
a1[3][0] = data1[1][0]
a1[4][0] = data1[1][1]
a1[5][0] = data1[1][2]
a1[6][0] = data1[2][0]
a1[7][0] = data1[2][1]
a1[8][0] = data1[2][2]
a1[9][0] = data1[3][0]
a1[10][0] = data1[3][1]
a1[11][0] = data1[3][2]


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



# Training data
# 1-32 positive solution variable t1 = 1, t2 = 0.
data1 = [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]]
data2 = [[0, 1, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]]
data3 = [[1, 1, 0], [1, 0, 1], [1, 0, 1], [1, 1, 1]]
data4 = [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 1, 0]]
data5 = [[1, 1, 1], [1, 0, 1], [1, 0, 1], [0, 1, 1]]
data6 = [[0, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]]
data7 = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
data8 = [[0, 0, 0], [1, 1, 0], [1, 0, 1], [1, 1, 1]]
data9 = [[0, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 0]]
data10 = [[0, 0, 0], [1, 1, 1], [1, 0, 1], [0, 1, 1]]
data11 = [[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 0]]
data12 = [[0, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 0]]
data13 = [[1, 1, 0], [1, 0, 1], [1, 1, 1], [0, 0, 0]]
data14 = [[1, 1, 1], [1, 0, 1], [1, 1, 0], [0, 0, 0]]
data15 = [[1, 1, 1], [1, 0, 1], [0, 1, 1], [0, 0, 0]]
data16 = [[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]]
data17 = [[1, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 1]]
data18 = [[1, 1, 1], [1, 0, 1], [1, 0, 0], [1, 1, 1]]
data19 = [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1]]
data20 = [[1, 1, 1], [1, 0, 1], [0, 0, 1], [1, 1, 1]]
data21 = [[1, 1, 1], [0, 0, 1], [1, 0, 1], [1, 1, 1]]
data22 = [[0, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]]
data23 = [[0, 1, 1], [1, 0, 0], [0, 0, 1], [1, 1, 1]]
data24 = [[0, 1, 1], [1, 0, 1], [1, 0, 0], [1, 1, 1]]
data25 = [[0, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1]]
data26 = [[0, 1, 1], [1, 0, 1], [0, 0, 1], [1, 1, 1]]
data27 = [[0, 1, 1], [0, 0, 1], [1, 0, 1], [1, 1, 1]]
data28 = [[1, 1, 0], [1, 0, 0], [1, 0, 1], [1, 1, 1]]
data29 = [[1, 1, 0], [1, 0, 1], [1, 0, 0], [1, 1, 1]]
data30 = [[1, 1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1]]
data31 = [[1, 1, 0], [1, 0, 1], [0, 0, 1], [1, 1, 1]]
data32 = [[1, 1, 0], [0, 0, 1], [1, 0, 1], [1, 1, 1]]

# 33-64 positive solution variable t1 = 0, t2 = 1.
data33 = [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
data34 = [[1, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
data35 = [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
data36 = [[0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 0]]
data37 = [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 1]]
data38 = [[1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 0]]
data39 = [[1, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 1]]
data40 = [[1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]]
data41 = [[0, 1, 0], [0, 1, 1], [0, 1, 0], [0, 1, 0]]
data42 = [[0, 1, 0], [0, 1, 0], [0, 1, 1], [0, 1, 0]]
data43 = [[1, 1, 0], [0, 1, 1], [0, 1, 0], [0, 1, 0]]
data44 = [[1, 1, 0], [0, 1, 0], [0, 1, 1], [0, 1, 0]]
data45 = [[0, 1, 0], [0, 1, 1], [0, 1, 0], [1, 1, 0]]
data46 = [[0, 1, 0], [0, 1, 0], [0, 1, 1], [1, 1, 0]]
data47 = [[0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]]
data48 = [[1, 1, 0], [0, 1, 1], [0, 1, 1], [1, 1, 1]]
data49 = [[1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 0]]
data50 = [[0, 1, 1], [0, 1, 1], [0, 1, 1], [0, 1, 1]]
data51 = [[1, 1, 0], [1, 1, 0], [0, 1, 0], [0, 1, 0]]
data52 = [[1, 1, 0], [0, 1, 0], [1, 1, 0], [0, 1, 0]]
data53 = [[1, 1, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0]]
data54 = [[1, 1, 0], [0, 1, 0], [0, 0, 0], [0, 1, 0]]
data55 = [[0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 0, 0]]
data56 = [[1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
data57 = [[1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1]]
data58 = [[0, 1, 0], [0, 0, 0], [0, 1, 0], [1, 1, 0]]
data59 = [[0, 1, 0], [0, 1, 0], [0, 0, 0], [1, 1, 0]]
data60 = [[0, 0, 0], [0, 1, 0], [0, 1, 0], [1, 1, 0]]
data61 = [[0, 0, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
data62 = [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 0, 0]]
data63 = [[0, 1, 0], [0, 0, 1], [0, 0, 1], [0, 1, 0]]
data64 = [[0, 1, 0], [1, 0, 0], [1, 0, 0], [0, 1, 0]]