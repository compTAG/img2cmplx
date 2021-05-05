import numpy as np
import scipy.io

from PIL import Image


class MPEG7Reader:

    def load(self, path):
        with Image.open(path) as im:
            mat = np.array(im)
        return mat

class EMNISTReader:
    def __init__(self, matlab_by_class_fname):
        self._data = scipy.io.loadmat(matlab_by_class_fname)

    def load(self, class_label, num):
        images = self._data['dataset'][0][0][0][0][0][0]
        labels = self._data['dataset'][0][0][0][0][0][1]
        idx = [i for i, label in enumerate(x[0] for x in labels) if label == class_label][num]
        # images are returned as an array with 784 elements, so we reshape to be a 2d array
        return (images[idx]).reshape(28, 28).transpose()


