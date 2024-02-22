from pyuul import VolumeMaker # the main PyUUL module
from pyuul import utils # the PyUUL utility module
import time,os,urllib # some standard python modules we are going to use

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


if __name__ == "__main__":
  # os.mkdir('exampleStructures')
  # urllib.request.urlretrieve('http://files.rcsb.org/download/101M.pdb', 'exampleStructures/101m.pdb')
  # urllib.request.urlretrieve('http://files.rcsb.org/download/5BMZ.pdb', 'exampleStructures/5bmz.pdb')
  # urllib.request.urlretrieve('http://files.rcsb.org/download/5BOX.pdb', 'exampleStructures/5box.pdb')

  coords, atname = utils.parsePDB("exampleStructures/") # get coordinates and atom names
  atoms_channel = utils.atomlistToChannels(atname) # calculates the corresponding channel of each atom
  radius = utils.atomlistToRadius(atname) # calculates the radius of each atom

  device = "cpu" # runs the volumes on CPU
  VoxelsObject = VolumeMaker.Voxels(device=device,sparse=True)
  PointCloudSurfaceObject = VolumeMaker.PointCloudVolume(device=device)
  PointCloudVolumeObject = VolumeMaker.PointCloudSurface(device=device)

  coords = coords.to(device)
  radius = radius.to(device)
  atoms_channel = atoms_channel.to(device)

  SurfacePoitCloud = PointCloudSurfaceObject(coords, radius)
  print(SurfacePoitCloud.shape)
  VolumePoitCloud = PointCloudVolumeObject(coords, radius)
  print(VolumePoitCloud)
  # 创建三维图形对象
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