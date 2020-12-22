import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt

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

    def massProperties(self):
        # Inspired by https://www.geometrictools.com/Documentation/PolyhedralMassProperties.pdf

        def Subexpressions(w0, w1, w2):
            temp0 = w0+w1
            temp1 = w0*w0
            temp2 = temp1+w1*temp0
            f1 = temp0+w2
            f2 = temp2+w2*f1
            f3 = w0*temp1+w1*temp2+w2*f2
            g0 = f2+w0*(f1+w0)
            g1 = f2+w1*(f1+w1)
            g2 = f2+w2*(f1+w2)
            return f1, f2, f3, g0, g1, g2

        mult = np.array([1/6, 1/24, 1/24, 1/24, 1/60, 1/60, 1/60, 1/120, 1/120, 1/120])
        intg = np.zeros(10, dtype=float)
        tri = self.triangles()

        for t in tri:
            x0, y0, z0 = t.Point1.x, t.Point1.y, t.Point1.z
            x1, y1, z1 = t.Point2.x, t.Point2.y, t.Point2.z
            x2, y2, z2 = t.Point3.x, t.Point3.y, t.Point3.z

            a1, b1, c1 = x1-x0, y1-y0, z1-z0
            a2, b2, c2 = x2-x0, y2-y0, z2-z0
            d0 = b1*c2-b2*c1
            d1 = a2*c1-a1*c2
            d2 = a1*b2-a2*b1

            f1x, f2x, f3x, g0x, g1x, g2x = Subexpressions(x0, x1, x2)
            f1y, f2y, f3y, g0y, g1y, g2y = Subexpressions(y0, y1, y2)
            f1z, f2z, f3z, g0z, g1z, g2z = Subexpressions(z0, z1, z2)

            intg[0] += d0*f1x
            intg[1] += d0*f2x
            intg[2] += d1*f2y
            intg[3] += d2*f2z
            intg[4] += d0*f3x
            intg[5] += d1*f3y
            intg[6] += d2*f3z
            intg[7] += d0*(y0*g0x+y1*g1x+y2*g2x)
            intg[8] += d1*(z0*g0y+z1*g1y+z2*g2y)
            intg[9] += d2*(x0*g0z+x1*g1z+x2*g2z)

        intg *= mult
        volume = intg[0]
        cog = np.array([intg[1]/volume, intg[2]/volume, intg[3]/volume])
        ixx = intg[5]+intg[6]-volume*(cog[1]**2+cog[2]**2)
        iyy = intg[4]+intg[6]-volume*(cog[2]**2+cog[0]**2)
        izz = intg[4]+intg[5]-volume*(cog[0]**2+cog[1]**2)
        ixy = -(intg[7]-volume*cog[0]*cog[1])
        iyz = -(intg[8]-volume*cog[1]*cog[2])
        ixz = -(intg[9]-volume*cog[2]*cog[0])
        inertia = np.array([[ixx, ixy, ixz], [ixy, iyy, iyz], [ixz, iyz, izz]])

        return volume, cog, inertia

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
