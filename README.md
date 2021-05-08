# img2cmplx
Extract a simplicial complex from a raster

**Warning** The library only has very basic functionality to extract the longest
contour from the mpeg7 or emnist datasets.  It is not particularly well tested,
so if something is not working as you would expect, let me know, it is probably
my fault.

## Getting Started

To install the library, run pip:

    pip install img2cmplx

And import the library into ALL THE CODES!

    import img2cmplx as i2c

Many of the example codes below use a few libraries, so go ahead and import
away:

    import os
    import cv2

Load a file from mpeg7 (such as "apple-10"):

    fname = os.path.join('data','mpeg7', 'apple-10.gif')
    img = i2c.io.MPEG7Reader().load(fname)
    cv2.imwrite('mpeg7.png', img)

Or from emnist (such as the very famous class 10 example 1):

    emnist_path = os.path.join('data','emnist','emnist-byclass.mat')
    class_num = 10
    example_num = 1
    img = i2c.io.EMNISTReader(emnist_path).load(class_num, example_num)
    cv2.imwrite('emnist.png', img)

Either way, once you have an image that you want to use, you can extract the
boundary and then convert the curve to a complex as:

    cmplx = i2c.simplify.img_to_complex(img)


## Potential future features

In other projects, other things that we have implemented (and can easilyadd
here) include:

- curve simplification with DP algo
- verify/fix curves that have vertex sets that are not in general position
- detect/fix curve that is non-simple

If you have others please, let me know!

## Getting data sets

While you can byod (bring your own data), for development, the makefile provides
a tool that will download and organize the mpeg7 and emnist datasets for you.
Just run

	make data-init

Feel free to lend a hand or provide suggestions, but as my students and I have
written and re-written code to do this over and over again, I figured that I
would make everybody's life easier and put it in a library for all to use.
