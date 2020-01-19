#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import imutils
import cv2
import matplotlib.pyplot as plt


def basics_pt2():
    print("Start Open CV Grayscale Test")
    img_path = os.path.join(os.getcwd(), "img_src", "tetris_blocks.png")
    print(img_path)

    # load the input image (whose path was supplied via command line
    # argument) and display the image to our screen
    image = cv2.imread(img_path)
    cv2.imshow("Image", image)
    cv2.waitKey(0)

    # convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray", gray)
    cv2.waitKey(0)

    # Edge detection works by firstly changing the colors to grayscale, and then
    # we run the cv2.Canny function that is the Canny Algorithm to find its edges.
    # minimum and maximum threshold is to track the edges by hysteresis.
    min_thres = 30
    max_thres = 150
    edged = cv2.Canny(gray, min_thres, max_thres)
    # The image returned is the tetris edge maps.
    cv2.imshow("Edged", edged)
    cv2.waitKey(0)

    # using the cv2 Threshold function, we can segment the grayscale image by setting
    # things to either black or white.
    # low_threshold will set anything below that in image to be valued 0 (black)
    # Anything above that, will be set to max_value
    low_threshold = 225
    max_value = 255
    thresh = cv2.threshold(gray, low_threshold, max_value, cv2.THRESH_BINARY_INV)[1]
    cv2.imshow("Threshold", thresh)
    cv2.waitKey(0)

    # Now that we learn that, we can learn how to make contours, which is going to use the
    # firstly we get the countours as a tuple of a list with its edge points
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    # The imutils is important for compatibility reasons
    cnts = imutils.grab_contours(cnts)
    output = image.copy()

    # loop over the contours
    for c in cnts:
        # draw each contour on the output image with a 3px thick purple
        # outline, then display the output contours one at a time
        cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
        cv2.imshow("Contours", output)
        cv2.waitKey(0)

    # Erosions and Dilations are used to reduce noise in binary images that was caused by
    # thresholding.
    # Here we reduce the foreground by 5 iterations using Erosion.
    mask = thresh.copy()
    eroded_mask = cv2.erode(mask, None, iterations=5)
    cv2.imshow("Eroded", eroded_mask)
    cv2.waitKey(0)
    # Here we increase the foreground by 5 iterations using Dilation.
    mask = thresh.copy()
    dilated_mask = cv2.dilate(mask, None, iterations=5)
    cv2.imshow("Dilated", dilated_mask)
    cv2.waitKey(0)

    # And finally we learn here masking and bitwise operations to remove unwanted areas.
    mask = thresh.copy()
    output = cv2.bitwise_and(image, image, mask=eroded_mask)
    cv2.imshow("Output_And", output)
    cv2.waitKey(0)

if __name__ == '__main__':
    basics_pt2()
