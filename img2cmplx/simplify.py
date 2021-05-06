from collections import namedtuple

import cv2

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




    # convert to networkx graph
    # Vertex = namedtuple('Point', ['x', 'y'])
    # G = nx.Graph()
    # node_id = 0
    # dup_vertices = False

    #     index = get_node_index(pt[0][0], pt[0][1], G)
    #     # check to make sure we haven't already added this vertex
    #     if index == -1:
    #         G.add_node(node_id, v=Vertex(node_id,
    #                                     float(pt[0][0]),
    #                                     float(pt[0][1])))
    #         node_id+=1
    #     # vertices have to be unique, so if it isn't, we exit
    #     else:
    #         print("There is a duplicate vertex")
    #         print(pt)
    #         dup_vertices = True
    # # add in the appropriate edges for the contour
    # for i in range(0, len(c)-1):
    #     v1 = c[i]
    #     v2 = c[i+1]
    #     G.add_edge(get_node_index(v1[0][0], v1[0][1], G),
    #         get_node_index(v2[0][0], v2[0][1], G))
    # # add edge from last to first vertex in contour to make closed curve
    # v1 = c[len(c)-1]
    # v2 = c[0]
    # G.add_edge(get_node_index(v1[0][0], v1[0][1], G),
    #     get_node_index(v2[0][0], v2[0][1], G))
    #
    # # visualization functions for debugging
    # # save_contour_img(thresh, contours, copy.deepcopy(img), "test")
    # # draw_graph(G)
