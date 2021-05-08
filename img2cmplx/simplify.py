from collections import namedtuple

import cv2
import networkx as nx

class PreconditionFailedError(Exception):
    """ Exception raised when we detect an error in the input

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message):
        self.message = message


def extract_boundary(img):
    """ Extract the boundary from an image.

    We define the boundary as the longest contour of the image.

    Attributes:
        img -- the image from which to extract the boundary
    """

    # convert image to binary
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _, imbin = cv2.threshold(imgray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # get the longest contour
    contours, _ = cv2.findContours(
        imbin,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE,
    )
    longest_contour = sorted(
        contours,
        key=lambda x: cv2.arcLength(x, True),
        reverse=True,
    )[0]

    # simplify the contour as a function of curve length
    # currently we have disabled contour simplification as openCv simplification
    # will sometimes break a contour into multiple closed cuves
    simplified_longest_contour = longest_contour
    # epsilon = eps * cv2.arcLength(curve=longest_contour, closed=True)
    # simplified_longest_contour = cv2.approxPolyDP(
    #     curve=longest_contour,
    #     epsilon=epsilon,
    #     closed=True,
    # )

    return simplified_longest_contour


def curve_to_complex(curve):
    """
    Convert the curve to a networkx graph

    Each node of the graphs has its coordinates as the "pos" attribute

    Attributes:
        curve -- curve to convert into a complex.  Curve is expected to be of
        output produced by opencv's contour functions.  For example:
            curve = [
                [[0, 0]],
                [[20, 5]],
                [[17, 10]],
                [[4, 10]],
            ]
    """
    graph = nx.Graph()

    # assign index to each point and add vertex to graph
    verts = set()
    for pt in curve:
        idx = len(verts)
        v = (pt[0][0], pt[0][1])

        if v in verts:
            raise PreconditionFailedError("duplicate vertex in curve")

        verts.add(v)
        graph.add_node(idx, pos=v)

    # add edges for the contour
    for i in range(0, len(curve)-1):
        graph.add_edge(i, i+1)
    graph.add_edge(len(curve)-1, 0)

    return graph

    # # visualization functions for debugging
    # # save_contour_img(thresh, contours, copy.deepcopy(img), "test")
    # # draw_graph(G)


def img_to_complex(img):
    """ Create a complex from the image

    The complex is created by extracting the boundary of the largest contour.
    (basicalliy just calls `extract_boundary` and `curve_to_complex`.  The
    complex is represented as a networkx graph in which the vertex positions are
    the `pos` attribute.

    Attributes:
        img -- the image from which to create a complex
    """
    bdd = extract_boundary(img)
    return curve_to_complex(bdd)
