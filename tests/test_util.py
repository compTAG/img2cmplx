import os
import copy

import cv2
import numpy as np
from PIL import Image

import img2cmplx as i2c


MPEG7_DATA = os.path.join('tests','data', 'mpeg7.png')
EMNIST_DATA = os.path.join('tests','data', 'emnist.png')


def store_an_mpeg7():
    fname = os.path.join('data','mpeg7', 'apple-10.gif')
    mpeg7 = i2c.io.MPEG7Reader().load(fname)
    cv2.imwrite(MPEG7_DATA, mpeg7)


def store_an_emnist():
    emnist_path = os.path.join('data','emnist','emnist-byclass.mat')
    class_num = 10
    example_num = 1
    emnist = i2c.io.EMNISTReader(emnist_path).load(class_num, example_num)
    cv2.imwrite(EMNIST_DATA, emnist)


def load_an_mpeg7():
    return cv2.imread(MPEG7_DATA)


def load_an_emnist():
    return cv2.imread(EMNIST_DATA)


def display(data, fname):
    cv2.imwrite(fname, data)


def display_contour(img, contour, fname):
    img2 = cv2.drawContours(img, [contour], 0, (0,255,0), 3)
    cv2.imwrite(fname, img2)

