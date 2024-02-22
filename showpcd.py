import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
 
# 定义点坐标列表
points = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
 
# 将点坐标转换为NumPy数组
pointcloud = np.array(points)
print(pointcloud[0])
print(pointcloud[0:2])
#print(pointcloud[:, 0])
# 创建三维图形对象
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
 
# 设置点云颜色和大小
color = 'b' # 默认为蓝色
size = 10   # 默认为10像素
 
# 在图形上添加点云
ax.scatter(pointcloud[:, 0], pointcloud[:, 1], pointcloud[:, 2], c=color, s=size)
 
# 设置坐标轴名称
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
 
# 显示图形
plt.show()