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
        return np.unique(self.data(), axis = 0)

    def verticesNumber(self):
        return np.shape(self.vertices())[0]

    def facesNumber(self):
        return (np.shape(self.data())[0])//3

    def faces(self):
        array = np.zeros((self.facesNumber(), 3), dtype=np.ndarray)
        data = self.data()
        for i in range(np.shape(array)[0]):
            array[i, 0] = data[i]
            array[i, 1] = data[i+1]
            array[i, 2] = data[i+2]
        return array
