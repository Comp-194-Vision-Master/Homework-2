"""
File: hw2Code.py

This file contains the functions for Homework 2, along with some sample tests.

Fall 2025
Author: ???
"""
# TODO: Add your name as author of this code file

import random
import math
import cv2
import numpy as np

# ----------------------------------------------------------------------------------------------------------------
# Question 1

# TODO: Put your definition of divisBy here


# ----------------------------------------------------------------------------------------------------------------
# Question 2

# TODO: Write pseudocode for findPeaks here in the comment below

"""
Algorithm findPeaks(tempList)
--- Takes in a list of numbers, temperature readings




"""


# ----------------------------------------------------------------------------------------------------------------
# Question 3


def cropAndBlend(img1, img2):
    """Takes in two images, and determines the smallest width and heigh between the two. It then
    randomly crops each image to make two images the same size, and then blends them, returning the
    blended image."""
    (h1, w1, d1) = img1.shape
    (h2, w2, d2) = img2.shape

    wid = min(w1, w2)
    hgt = min(h1, h2)

    crop1 = randomCrop(img1, wid, hgt)
    crop2 = randomCrop(img2, wid, hgt)

    blended = cv2.addWeighted(crop1, 0.5, crop2, 0.5, 0)
    return blended


# TODO: Put your definition of randomCrop here


# ----------------------------------------------------------------------------------------------------------------
# Question 4


# TODO: Convert findMinMax below to be findMedian

def findMinMax(numList):
    """Takes in a list of numbers and finds the minimum and maximum by first sorting
    the list and then accessing the first and last values."""
    n = len(numList)
    numList.sort()
    return numList[0], numList[n - 1]


# ----------------------------------------------------------------------------------------------------------------
# Question 5

# TODO: Debug the program below (6 bugs, two per function)

def colorBlink(img):
    """Given an image, it color-shuffles the right half of the image, and displays the result, waiting half a second
    before repeating the process. It repeats this until the user types the 'q' key."""
    while True:
        img2 = halfColorShuffle()
        cv2.imshow("Blink", img2)
       x = cv2.waitKey(1000)
        if x >= 0 and chr(x) == 'q':
            break


def halfColorShuffle(img):
    """Given an image, it determines a region of interest that is the right half of
    the image, and it calls colorShuffle on that to change the order of the color
    channel arrays. It returns the changed image."""
    (h, w, d) = img.shape
    halfX = w // 2
    roi = img[:, halfX:]
    newRoo = colorShuffle(roi)
    img[:, halfX:] = newRoi
    return newRoi


def colorShuffle(img):
    """Given an image, it randomly shuffles the three color channels, returning the new image created."""
    (bChan, gChan, rChan) = cv2.split(img)
    chanList = [bChan, rChan, rChan]
    random.shuffle(chanList)
    newImg = cv2.merge(channList)
    return newImg


# ----------------------------------------------------------------------------------------------------------------
# Question 6

# TODO: Put your definition of sepia here


# ----------------------------------------------------------------------------------------------------------------
# Main script

# TODO: Put your additional test calls and sample calls to each function in the main script below.

if __name__ == "__main__":
    # -------------------------------------------------------------
    # Question 1 sample calls
    print("Testing question 1:  divisBy")
    # for i in range(1, 6):
    #     res = divisBy(25, i)
    #     print(25, i, res)
    # for i in range(1, 11):
    #     res2 = divisBy(12382, i)
    #     print(12382, i, res2)

    # -------------------------------------------------------------
    # Question 3 sample calls
    print("Testing question 3:  randomCrop")
    im1 = cv2.imread("SampleImages/mightyMidway.jpg")
    im2 = cv2.imread("SampleImages/chicago.jpg")
    #
    # for i in range(10):
    #     crop = randomCrop(im1, 250, 250)
    #     cv2.imshow("cropped", crop)
    #     cv2.waitKey()
    #
    print("Testing question 3:  randomCrop and blend")
    # for i in range(4):
    #     newIm = cropAndBlend(im1, im2)
    #     cv2.imshow("Cropped and blended", newIm)
    #     cv2.waitKey()

    # -------------------------------------------------------------
    # Question 4 sample calls
    print("Testing question 4:  findMedian")

    nlist1 = [5, 1, 2, 4, 3]
    nlist2 = [10, 20, 30, 40, 50, 55, 45, 35, 25, 15]
    nlist3 = [6, 6, 6, 6, 3, 3, 3, 3, 1, 1, 1, 1]
    # med1 = findMedian(nlist1)
    # med2 = findMedian(nlist2)
    # med3 = findMedian(nlist3)
    # print("Correct:", 3, "Actual:", med1)
    # print("Correct:", 32.5, "Actual:", med2)
    # print("Correct:", 3.0, "Actual:", med3)

    # -------------------------------------------------------------
    # Question 5 sample calls
    print("Testing question 5:  halfColorShuffle")
    im3 = cv2.imread("SampleImages/wildColumbine.jpg")

    # colorBlink(im3)

    # -------------------------------------------------------------
    # Question 6 sample calls
    print("Testing question 6:  sepia")

    # sep1 = sepia(im1)
    # sep2 = sepia(im2)
    # sep3 = sepia(im3)
    # cv2.imshow("sepia1", sep1)
    # cv2.imshow("sepia2", sep2)
    # cv2.imshow("sepia3", sep3)
    # cv2.waitKey()
