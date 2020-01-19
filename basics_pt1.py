#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import imutils
# noinspection PyPackageRequirements
import cv2
import matplotlib.pyplot as plt


def basics_pt1():
    print("Start Open CV Test")

    # Display image
    img_path = os.path.join(os.getcwd(), "img_src", "jp.png")
    print(img_path)
    image = cv2.imread(img_path)
    cv2.imshow('image', image)
    cv2.waitKey(0)

    # Print image size
    # The return is in a tuple of height, width, and depth
    # width = 600, height = 322, depth = 3
    (h, w, d) = image.shape
    print(f"width={w}, height={h}, depth={d}")

    # Print a pixel's BGR tuple taken at row 100, and column 50
    # B = 37, G = 49, R = 41
    (B, G, R) = image[100, 50]
    print(f"B={B}, G={G}, R={R}")

    # extract a 100x100 pixel square ROI (Region of Interest) from the
    # input image starting at x=320,y=60 at ending at x=420,y=160
    # This is an image of Jeff Goldblum's face
    roi = image[60:160, 320:420]
    cv2.imshow("ROI", roi)
    cv2.waitKey(0)

    # Resizing the image without aspect ratio to 200x200
    img_resized = cv2.resize(image, (200, 200))
    cv2.imshow("Fixed Resizing", img_resized)
    cv2.waitKey(0)

    # Resizing the image with correct aspect ratio,
    # with width of 300px (w/2), and height of 161px (h/2)
    # This results in an image a quarter of the original size
    img_cor_resized = cv2.resize(image, (w//2, h//2))
    cv2.imshow("Corrected Resizing", img_cor_resized)
    cv2.waitKey(0)

    # using imutils library, you can always get the correct aspect ratio
    # just by entering the desired pixel for height or width
    # in this we make an image half the size, by having 450 pix width
    resized = imutils.resize(image, width=450)
    cv2.imshow("Imutils Resize", resized)
    cv2.waitKey(0)

    # Here we rotate the image counter-clockwise based on the center
    # computing the image center, then constructing the rotation matrix,
    # and then finally applying the affine warp
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, -45, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("OpenCV Rotation", rotated)
    cv2.waitKey(0)

    # Here we blur an image using a Gaussian Blur with a 11x11 kernel to the image to smooth it,
    # useful when reducing high frequency noise
    img_blurred = cv2.GaussianBlur(image, (11,11), 0)
    cv2.imshow("Blurred", img_blurred)
    cv2.waitKey(0)

    # Here we draw a 2px thick red rectangle surrounding the faces
    # starting point or pt1 is 320, 60 at the top left corner
    # endpoint or pt2 is 420, 160 at the bottom right corner
    # then it's BGR color, and finally thickness in pixels
    output = image.copy()
    top_left_start = (320, 60)
    bot_right_end = (420, 160)
    BGR = (0, 0, 255)
    line_thickness = 2
    cv2.rectangle(output,
                  top_left_start,
                  bot_right_end,
                  BGR, line_thickness)
    # and here we have a filled circle of a radius of 20 pix
    # with the center at 300,150, and the color blue
    circ_center = (300, 150)
    radius_in_pix = 20
    BGR = (255, 0, 0)
    line_thickness = -1 # -1 means filled
    cv2.circle(output, circ_center, radius_in_pix, BGR, line_thickness)
    cv2.imshow("With Rectangle & circle", output)
    cv2.waitKey(0)

    # Here we create a line, similar format as rectangle
    output_line = image.copy()
    line_thickness = 2
    BGR = (0, 255, 0)
    cv2.line(output_line,
             top_left_start,
             bot_right_end,
             BGR,
             line_thickness)
    cv2.imshow("With line", output_line)
    cv2.waitKey(0)

    # Lastly we learn about writing in opencv
    output_text_img = image.copy()
    text = "Just trying it out"
    startpoint = (50, 150)
    font = cv2.FONT_HERSHEY_COMPLEX
    font_size = 2.2
    BGR = (100, 100, 100)
    font_thickness =2
    cv2.putText(output_text_img,
                text,
                startpoint,
                font,
                font_size,
                BGR,
                font_thickness)
    cv2.imshow("Show Text", output_text_img)
    cv2.waitKey(0)


if __name__ == '__main__':
    basics_pt1()
