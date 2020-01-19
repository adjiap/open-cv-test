#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import numpy as np
import skimage
import imutils
# noinspection PyPackageRequirements
import cv2
import matplotlib.pyplot as plt


def mean_square_error(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def img_compare():
    print("We begin the images comparison using Mean Square Error Method")
    tgt_shp = (200, 200)
    img1_path = os.path.join(os.getcwd(), "img_src", "jp_gate.png")
    img2_path = os.path.join(os.getcwd(), "img_src", "jp_gate_dark.png")
    img3_path = os.path.join(os.getcwd(), "img_src", "jp_gate_shp.png")
    img1 = cv2.imread(img1_path)
    img1 = cv2.resize(img1, tgt_shp)
    img2 = cv2.imread(img2_path)
    img2 = cv2.resize(img2, tgt_shp)
    img3 = cv2.imread(img3_path)
    img3 = cv2.resize(img3, tgt_shp)
    err1 = mean_square_error(img1, img2)
    err2 = mean_square_error(img1, img3)
    print(f"The original with dark image has an error of {err1}")
    print(f"The original with shopped image has an error of {err2}")


if __name__ == '__main__':
    img_compare()