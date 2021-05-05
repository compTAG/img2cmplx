import os

import numpy as np

import img2cmplx as i2c


ENMIST_DATA = 'tests/data/emnist.npy'
MPEG7_DATA = 'tests/data/emnist.npy'


def store_an_mpeg7():
    fname = os.path.join('data','mpeg7', 'apple-10.gif')
    mpeg7 = i2c.io.MPEG7Reader().load(fname)
    with open('tests/data/mpeg7.npy', 'wb') as f:
        np.save(f, mpeg7)


def store_an_emnist():
    emnist_path = os.path.join('data','emnist','emnist-byclass.mat')
    class_num = 1
    example_num = 1
    emnist = i2c.io.EMNISTReader(emnist_path).load(class_num, example_num)
    with open('tests/data/emnist.npy', 'wb') as f:
        np.save(f, emnist)


def load_an_emnist():
    with open('tests/data/emnist.npy', 'rb') as f:
        emnist = np.load(f)
    return emnist


def load_an_mpeg7():
    with open('tests/data/mpeg7.npy', 'rb') as f:
        mpeg7 = np.load(f)
    return mpeg7


# def test_init_mpeg7():
#     store_an_mpeg7()
#     x = load_an_mpeg7()
#     print(x)
#     assert False


# def test_init_emnist():
#     store_an_emnist()
#     y = load_an_emnist()
#     print(y)
#     assert False
