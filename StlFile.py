import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import os

os.chdir('d:\\desktop\\tipe\\code\\radon transform')

class Mesh:
    def __init__(self, path):
        self.path = path

    def raw(self):
        text = open(self.path, "r").read()
        list = text.split('\n')
        list = [x for x in list if 'vertex' in x]
        list = [x.split(' ') for x in list]
        for i in range(len(list)):
            list[i]=[float(x) for x in list[i] if '.' in x]
        array = np.asarray(list)
        return array

    def points(self):
        raw = np.unique(self.raw(), axis=0)
        return np.array([Point(i[0],i[1],i[2]) for i in raw])

    def triangles(self):
        raw = self.raw()
        points = np.array([Point(i[0],i[1],i[2]) for i in raw])
        return np.array([Triangle(points[3*i], points[3*i+1], points[3*i+2]) for i in range(np.shape(points)[0]//3)])

    def edges(self):
        triangles = self.triangles()
        list = []
        for i in triangles:
            list.append(Line(i.Point1, i.Point2))
            list.append(Line(i.Point2, i.Point3))
            list.append(Line(i.Point1, i.Point3))
        return np.asarray(list)

    def show(self):
        t = self.triangles()
        triangles = [((i.Point1.x, i.Point1.y, i.Point1.z), (i.Point2.x, i.Point2.y, i.Point2.z), (i.Point3.x, i.Point3.y, i.Point3.z)) for i in t]
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.add_collection(Poly3DCollection(triangles, facecolors='w', edgecolors='black', linewidths=1))
        plt.show()

class Point:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

class Line:
    def __init__(self, Point1: Point, Point2: Point):
        self.Point1 = Point1
        self.Point2 = Point2

class Triangle:
    def __init__(self, Point1: Point, Point2: Point, Point3: Point):
        self.Point1 = Point1
        self.Point2 = Point2
        self.Point3 = Point3
