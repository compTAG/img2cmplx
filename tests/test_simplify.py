import test_util

import img2cmplx as i2c

def test_simplify_extract_boundary():
    # img = test_util.load_an_emnist()
    img = test_util.load_an_mpeg7()

    bdd = i2c.simplify.extract_boundary(img)
    test_util.display_contour(img, bdd, 'contour.png')
