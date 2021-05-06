import test_util

def test_init_mpeg7():
    test_util.store_an_mpeg7()
    x = test_util.load_an_mpeg7()
    test_util.display(x, 'mpeg7.png')


def test_init_emnist():
    test_util.store_an_emnist()
    y = test_util.load_an_emnist()
    test_util.display(y, 'emnist.png')
