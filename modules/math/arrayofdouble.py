import double
import numpy as np

class ArrayOfDouble:
    #_array = np.array((1, 0))
    _array = np.array([])
    _dimension = 0

    def __init__(self, dimension = 0, value = None):
        self._dimension = dimension
        self._array = np.full(dimension, value)

    def __setitem__(self, index, value):
        self._array[index] = value

    def __getitem__(self, index, value):
        return self._array[index]

    def __str__(self):
        return str(self._array)

    def display(self):
        return self.__str__()
