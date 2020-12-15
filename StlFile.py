import os
import numpy as np


class StlFile:
    def __init__(self, path):
        self.path = path

    def format(self):
        textchars = bytearray(
            {7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7F}
        )
        is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))
        if is_binary_string(open(self.path, "rb").read(1024)):
            return "Binary"
        else:
            return "Ascii"

    def text(self):
        if self.format() == "Binary":
            return open(self.path, "rb").read()
        else:
            return open(self.path, "r").read()

    def data(self):
        text = self.text()
        if self.format() == "Ascii":
            list = text.split('\n')
            list = [x for x in list if 'vertex' in x]
            list = [x.split(' ') for x in list]
            for i in range(len(list)):
                list[i]=[float(x) for x in list[i] if '.' in x]
            array = np.asarray(list)
            return array
        else:
            return text

    def vertices(self):
        array = np.unique(self.data(), axis = 0)
        array1 = np.empty((np.shape(array))[0], dtype=Point)
        for i in range(np.shape(array)[0]):
            array1[i] = Point(array[i,0], array[i,1], array[i,2])
        return array1

    def verticesNumber(self):
        return np.shape(self.vertices())[0]

    def facesNumber(self):
        return (np.shape(self.data())[0])//3

    def faces(self):
        array = np.empty(self.facesNumber(), dtype=Face)
        data = self.data()
        for i in range(np.shape(array)[0]):
            Point1 = Point(data[i,0],data[i,1],data[i,2])
            Point2 = Point(data[i+1,0],data[i+1,1],data[i+1,2])
            Point3 = Point(data[i+2,0],data[i+2,1],data[i+2,2])
            array[i] = Face(Point1, Point2, Point3)
        return array

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def coordinates(self):
        return self.x, self.y, self.z

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Segment:
    def __init__(self, Point1, Point2):
        self.Point1 = Point1
        self.Point2 = Point2

class Face:
    def __init__(self, Point1, Point2, Point3):
        self.Point1 = Point1
        self.Point2 = Point2
        self.Point3 = Point3

    def points(self):
        return self.Point1, self.Point2, self.Point3

    def coordinates(self):
        return self.Point1.coordinates(), self.Point2.coordinates(), self.Point3.coordinates()
