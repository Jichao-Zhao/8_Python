# -*- coding:utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


# Fixing random state for reproducibility
np.random.seed(19680801)

'''
# 函数名称：Gen_RandLine
# 函数功能：产生随机线条
# 参数：length：线段的树目
#      dims：数据的维数
# 返回值：
'''
def Gen_RandLine(length, dims=2):
    """
    Create a line using a random walk algorithm

    length is the number of points for the line.
    dims is the number of dimensions the line has.
    """
    lineData = np.empty((dims, length))
    lineData[:, 0] = np.random.rand(dims)
    for index in range(1, length):
        # scaling the random numbers by 0.1 so
        # movement is small compared to position.
        # subtraction by 0.5 is to change the range to [-0.5, 0.5]
        # to allow a line to move backwards.
        step = ((np.random.rand(dims) - 0.5) * 0.1)
        lineData[:, index] = lineData[:, index - 1] + step

    return lineData


def update_lines(num, dataLines, lines):
    for line, data in zip(lines, dataLines):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines


# Attaching 3D axis to the figure
Ax = [0, 8]
Ay = [0, 7]
Az = [0, 6]
Bx = [0, 6]
By = [0, 7]
Bz = [0, 8]

fig = plt.figure()
ax = p3.Axes3D(fig)

# 绘制三维直线
ax.plot(Ax, Ay, Az, color='red', linestyle='-')
# 绘制三维箭头
ax.quiver(Ax[-1], Ay[-1], Az[-1], Ax[-1]*0.1, Ay[-1]*0.1, Az[-1]
          * 0.1, color='red', linestyle='-', normalize=False)
# 绘制三维点
ax.scatter(Ax[-1]*1.1, Ay[-1]*1.1, Az[-1]*1.1, color='red')
# 添加三维文字注释
ax.text(Ax[-1]+1, Ay[-1]-1, Az[-1]-0, "Qb = [Qx', Qy', Qz']", color='black')
ax.text(Ax[-1]+1, Ay[-1]+1, Az[-1]+1, "Point_B", color='black')
ax.scatter(0, 0, 0, color='red')
ax.text(0, 0, 1, "Point_A", color='black')
ax.text(0+2, 0-1, 1-0, "Qa = [Qx, Qy, Qz]", color='black')

'''
ax.plot(Bx, By, Bz, color='blue', linestyle='-.')
ax.quiver(Bx[-1], By[-1], Bz[-1], Bx[-1]*0.1, By[-1]*0.1, Bz[-1]
          * 0.1, color='blue', linestyle='-.', normalize=False)
ax.scatter(Bx[-1]*1.1, By[-1]*1.1, Bz[-1]*1.1, color='blue')
ax.text(Bx[-1]-1, By[-1]-1, Bz[-1]+1, "Qb = [Qx', Qy', Qz']", color='black')
ax.text(Bx[-1]+1, By[-1]+1, Bz[-1]+1, "Point_B", color='black')
'''

ax.text2D(0.05, 0.95, "3D Axis", transform=ax.transAxes)

# Setting the axes properties
ax.set_xlim3d([-1, 10])
ax.set_xlabel('XAxis')
ax.set_ylim3d([-1, 10])
ax.set_ylabel('YAxis')
ax.set_zlim3d([-1, 10])
ax.set_zlabel('ZAxis')
# ax.set_title('Change the title')


plt.show()




