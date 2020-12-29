import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt

class Mesh:
    def __init__(self, path):
        self.path = path
        self.raw = self.raw()
        self.center()

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
        raw = np.unique(self.raw, axis=0)
        return np.array([Point(i[0],i[1],i[2]) for i in raw])

    def triangles(self):
        raw = self.raw
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

    def show(self):
        t = self.triangles()
        triangles = [((i.Point1.x, i.Point1.y, i.Point1.z), (i.Point2.x, i.Point2.y, i.Point2.z), (i.Point3.x, i.Point3.y, i.Point3.z)) for i in t]
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.add_collection(Poly3DCollection(triangles, facecolors='w', edgecolors='black', linewidths=1))
        plt.show()

    def translate(self, translation):
        self.raw += translation

    def center(self):
        self.raw -= self.massProperties()[1]

    def slice(self, z):
        tri = [i for i in self.triangles() if i.zExtremums()[0]<=z<=i.zExtremums()[1]]
        return [i.zIntersection(z) for i in tri]

    def showSlice(self, z):
        lines = self.slice(z)
        for i in lines:
            plt.plot([i.Point1.x, i.Point2.x], [i.Point1.y, i.Point2.y], c='blue')
        plt.axis('equal')
        plt.show()
        
    def maxRadius(self):
        radii = np.array([i.cylindrical()[0] for i in self.points()])
        return np.amax(radii)
    
    def maxCoordinates(self):
        x = np.array([i.cartesian()[0] for i in self.points()])
        y = np.array([i.cartesian()[1] for i in self.points()])
        z = np.array([i.cartesian()[2] for i in self.points()])
        xmin, xmax = np.amin(x), np.amax(x)
        ymin, ymax = np.amin(y), np.amax(y)
        zmin, zmax = np.amin(z), np.amax(z)
        return xmin, xmax, ymin, ymax, zmin, zmax

class Point:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def cartesian(self):
        return np.array([self.x, self.y, self.z])
    
    def cylindrical(self):
        x, y, z = self.x, self.y, self.z
        r = (x**2+y**2)**(1/2)
        theta = np.arctan(y/x)
        return np.array([r, theta, z])

class Line:
    def __init__(self, Point1: Point, Point2: Point):
        self.Point1 = Point1
        self.Point2 = Point2

    def vector(self):
        x = self.Point2.x-self.Point1.x
        y = self.Point2.y-self.Point1.y
        z = self.Point2.z-self.Point1.z
        return np.array([x, y, z])/np.linalg.norm(np.array([x, y, z]))

    def zIntersection(self, z):
        # Inspired by https://rosettacode.org/wiki/Find_the_intersection_of_a_line_with_a_plane#Python
        planeNormal = np.array([0,0,1])
        planePoint = np.array([0,0,z])
        rayDirection = self.vector()
        rayPoint = self.Point1.cartesian()
        epsilon = 1e-6

        ndotu = planeNormal.dot(rayDirection)
        if abs(ndotu) < epsilon:
            return Point(1e99,1e99,1e99)

        w = rayPoint - planePoint
        si = -planeNormal.dot(w) / ndotu
        Psi = w + si * rayDirection + planePoint
        return Point(Psi[0], Psi[1], Psi[2])
    
    def hasXIntersection(self, x):
        return (self.Point1.x>x and self.Point2.x<x)^(self.Point1.x<x and self.Point2.x>x)

    def hasZIntersection(self, z):
        return (self.Point1.z>z and self.Point2.z<z)^(self.Point1.z<z and self.Point2.z>z)

class Triangle:
    def __init__(self, Point1: Point, Point2: Point, Point3: Point):
        self.Point1 = Point1
        self.Point2 = Point2
        self.Point3 = Point3

    def edges(self):
        return Line(self.Point1, self.Point2), Line(self.Point1, self.Point3), Line(self.Point3, self.Point2)

    def zExtremums(self):
        return min(self.Point1.z, self.Point2.z, self.Point3.z), max(self.Point1.z, self.Point2.z, self.Point3.z)

    def zIntersection(self, z):
        e = self.edges()
        p = [i.zIntersection(z) for i in e if i.hasZIntersection(z)]
        return Line(p[0], p[1])

class Slice:
    def __init__(self, Mesh, z):
        self.Mesh = Mesh
        self.z = z
    
    def lines(self):
        tri = [i for i in self.Mesh.triangles() if i.zExtremums()[0]<=self.z<=i.zExtremums()[1]]
        return [i.zIntersection(self.z) for i in tri]
    
    def show(self):
        lines = self.lines()
        for i in lines:
            plt.plot([i.Point1.x, i.Point2.x], [i.Point1.y, i.Point2.y], c='blue')
        plt.axis('equal')
        plt.show()
    
    def radon(self, r, res):
        Xlist = (np.linspace(-r, r, int(2*r/res))).tolist()
        
        def intersectedLines(x, r):
            L = [i for i in self.lines() if i.hasXIntersection(x)]
            return L
        
        def intersection(Line1, Line2):
            # Inspired by https://rosettacode.org/wiki/Find_the_intersection_of_two_lines#Python
            Ax1, Ay1 = Line1.Point1.x, Line1.Point1.y
            Ax2, Ay2 = Line1.Point2.x, Line1.Point2.y
            Bx1, By1 = Line2.Point1.x, Line2.Point1.y
            Bx2, By2 = Line2.Point2.x, Line2.Point2.y
            d = (By2 - By1) * (Ax2 - Ax1) - (Bx2 - Bx1) * (Ay2 - Ay1)
            if d:
                uA = ((Bx2 - Bx1) * (Ay1 - By1) - (By2 - By1) * (Ax1 - Bx1)) / d
                uB = ((Ax2 - Ax1) * (Ay1 - By1) - (Ay2 - Ay1) * (Ax1 - Bx1)) / d
            else:
                return
            if not(0 <= uA <= 1 and 0 <= uB <= 1):
                return
            x = Ax1 + uA * (Ax2 - Ax1)
            y = Ay1 + uA * (Ay2 - Ay1)
        
            return Point(x, y, self.z)
        
        def length(x, r):
            ray = Line(Point(x, -r, self.z), Point(x, r, self.z))
            lines = intersectedLines(x, r)
            y = [intersection(i, ray).y for i in lines]
            y.sort()
            l = [y[2*i+1]-y[2*i] for i in range(int(len(y)/2))]
            return sum(l)
        
        Rlist = [length(i, r) for i in Xlist]
        
        return Rlist
        
        
class Transform:
    def __init__(self, Mesh, Res, nbProj):
        self.Mesh = Mesh
        self.Res = Res
        self.nbProj = nbProj
    
    def projShape(self):
        x = (self.Mesh.maxRadius()*2)//(self.Res)
        y = (self.Mesh.maxCoordinates()[5]-self.Mesh.maxCoordinates()[4])//(self.Res)
        w = self.nbProj
        return x, y, w
