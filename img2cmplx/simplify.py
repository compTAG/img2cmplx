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



# takes an img from the MNIST data set and returns a networkx graph with the
# perimeter data
# @param img: the image
# @param eps: the epsilon value used in contour approximation
# returns a networkx graph with vertices on the perimeter and edges along the
# contour. Note that the vertices are a SIMPLE approx of the actual contour
# data. The second return value is pertaining to general position. -2 means it was not
# a simple polygon, -1 means it did not mean gen pos, 0 means it has duplicate
# vertices in the contour  and 1 means success
# Note that original eps is .005
def extract_boundary(img, eps=.005):
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
    epsilon = eps * cv2.arcLength(curve=longest_contour, closed=True)
    simplified_longest_contour = cv2.approxPolyDP(
        curve=longest_contour,
        epsilon=epsilon,
        closed=True,
    )
    return simplified_longest_contour


def curve_to_complex(curve):
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
