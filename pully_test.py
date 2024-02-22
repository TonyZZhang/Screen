from pyuul import VolumeMaker # the main PyUUL module
from pyuul import utils # the PyUUL utility module
import torch

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

device = "cpu"
VoxelsObject = VolumeMaker.Voxels(device=device,sparse=True)
PointCloudVolumeObject = VolumeMaker.PointCloudVolume(device=device)
PointCloudSurfaceObject = VolumeMaker.PointCloudSurface(device=device)

#coordinates = torch.rand((5,10,3),device=device) #5 molecules of 10 atoms each
points = [(0, 0, 0), (0, 0, 1), (0, 0, 2)]  
  
# 将坐标列表转换为张量  
coordinates = torch.tensor(points, dtype=torch.float32)
coordinates_3d = coordinates.unsqueeze(0)  

print(coordinates)
radius = torch.rand((1,3),device=device) #radius of each atom


SurfacePoitCloud = PointCloudSurfaceObject(coordinates_3d, radius)
#VolumePoitCloud = PointCloudVolumeObject(coordinates, radius)
print(SurfacePoitCloud)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 设置点云颜色和大小
color = 'b' # 默认为蓝色
size = 10   # 默认为10像素
pointcloud = np.array(SurfacePoitCloud)
print(pointcloud)
print(pointcloud[:, 0])
# 在图形上添加点云
# x_coordinates = [row[0] for row in SurfacePoitCloud]
# y_coordinates = [row[1] for row in SurfacePoitCloud]
# z_coordinates = [row[2] for row in SurfacePoitCloud]
# print(x_coordinates)
ax.scatter(pointcloud[:,:,0], pointcloud[:,:,1], pointcloud[:,:,2], c=color, s=size)

# 设置坐标轴名称
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 显示图形
plt.show()
# file = open("matrix.txt", "w")
# for row in VolumePoitCloud:
#   file.write(' '.join([str(x) for x in row]) + '\n')
# VoxelRepresentation = VoxelsObject(coords, radius, atoms_channel)
print('hello word')