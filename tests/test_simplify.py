import pytest

import test_util

import img2cmplx as i2c

def test_playground():
    img = test_util.load_an_emnist()
    # img = test_util.load_an_mpeg7()

    bdd = i2c.simplify.extract_boundary(img)
    test_util.display_contour(img, bdd, 'contour.png')

    cmplx = i2c.simplify.curve_to_complex(bdd)
    test_util.display_graph(cmplx, 'graph.png')

    i2c.simplify.img_to_complex(img)


def test_simplify_extract_boundary():
    # img = test_util.load_an_emnist()
    img = test_util.load_an_mpeg7()

    bdd = i2c.simplify.extract_boundary(img)
    test_util.display_contour(img, bdd, 'contour.png')


def test_simplify_curve_to_complex_happy_path():
    bdd = [
        [[0, 0]],
        [[20, 5]],
        [[17, 10]],
        [[4, 10]],
    ]
    cmplx = i2c.simplify.curve_to_complex(bdd)
    test_util.display_graph(cmplx, 'graph.png')

def test_simplify_curve_to_complex_duplicate_verts():
    bdd = [
        [[0, 0]],
        [[20, 5]],
        [[17, 10]],
        [[20, 5]],
    ]
    with pytest.raises(i2c.simplify.PreconditionFailedError):
        i2c.simplify.curve_to_complex(bdd)

