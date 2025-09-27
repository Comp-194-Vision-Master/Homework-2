"""
File: hw2Checker.py

This file contains test functions that check solutions for Homework 2, using assert to check if the results are fine
or indicating to the user that they should visually check the work.

Fall 2025
Author: Susan Fox
"""

# TODO: Change  hw2CodeSoln below to match your solution filename
import hw2CodeSoln as hw2
import cv2


# ==========================================================================================
# Testing main program


def runTests():
    """Calls testing functions"""
    print("Running tests...")

    check_divisBy()       # Question 1
    check_randomCrop()    # Question 3
    check_cropAndBlend()
    check_findMedian()    # Question 4
    check_colorBlink()    # Question 5
    check_sepia()         # Question 6


# ----------------------------------------------------------------------------------------------------------------
# Question 1


def check_divisBy():
    """Tests divisBy to see if it works"""
    print("Testing divisBy...")
    # Check even/odd up to 1000
    for x in range(0, 1002, 2):
        assert hw2.divisBy(x, 2) is True
        assert hw2.divisBy(x + 1, 2) is False

    # Check multiples of 5, positive and negative
    for x in range(-1000, 1005, 5):
        assert hw2.divisBy(x, 5) is True
        assert hw2.divisBy(x + 1, 5) is False
        assert hw2.divisBy(x + 2, 5) is False
        assert hw2.divisBy(x + 3, 5) is False
        assert hw2.divisBy(x + 4, 5) is False

    # Check divisible by negative 3
    for x in range(-999, 1000, 3):
        assert hw2.divisBy(x, -3) is True
        assert hw2.divisBy(x + 1, -3) is False
        assert hw2.divisBy(x + 2, -3) is False

    print("divisBy passed all tests!")


# ----------------------------------------------------------------------------------------------------------------
# Question 3

def check_randomCrop():
    """Tests randomCrop alone to see if it works"""
    print("Testing randomCrop...")
    print("----> Must check visually! <----")
    img1 = cv2.imread("SampleImages/landscape1.jpg")
    print("   Checking 5 calls to randomCrop with 300x300")
    for i in range(5):
        newIm = hw2.randomCrop(img1, 300, 300)
        cv2.imshow("RandomCrop" + str(i), newIm)
        cv2.waitKey(250)
    print("   Checking 5 calls to randomCrop with 1000x750")
    for i in range(5):
        newIm = hw2.randomCrop(img1, 1000, 750)
        cv2.imshow("RandomCrop" + str(i), newIm)
        cv2.waitKey(250)
    cv2.waitKey()
    cv2.destroyAllWindows()
    print("Check visually to see if cropAndBlend passed tests.")


def check_cropAndBlend():
    """Tests cropAndBlend, which relies on randomCrop"""
    print("Testing cropAndBlend...")
    print("----> Must check visually! <----")
    img1 = cv2.imread("SampleImages/landscape1.jpg")
    img2 = cv2.imread("SampleImages/chicago.jpg")
    print("   Checking 5 calls to cropBlend")
    for i in range(5):
        blendIm = hw2.cropAndBlend(img1, img2)
        cv2.imshow("CropBlend" + str(i), blendIm)
        cv2.waitKey(250)
    cv2.waitKey()
    cv2.destroyAllWindows()
    print("Check visually to see if cropAndBlend passed tests.")


# ----------------------------------------------------------------------------------------------------------------
# Question 4

def check_findMedian():
    """Tests findMedian"""
    print("Testing findMedian...")
    nums1 = [193]
    med = hw2.findMedian(nums1)
    assert med == 193

    nums2 = [50, 80]
    med = hw2.findMedian(nums2)
    assert med == 65

    nums3 = [5, 25, 10, 20, 15]
    med = hw2.findMedian(nums3)
    assert med == 15

    nums4 = [1, 9, 4, 6, 3, 12, 8, 2, 7, 10, 5, 11]
    med = hw2.findMedian(nums4)
    assert med == 6.5

    print("findMedian passed all tests!")


# ----------------------------------------------------------------------------------------------------------------
# Question 5

def check_colorBlink():
    """Tests colorBlink"""
    print("Testing colorBlink...")
    print("----> Must check visually! <----")

    blinkIm = cv2.imread("SampleImages/grandTetons.jpg")
    hw2.colorBlink(blinkIm)
    cv2.waitKey()
    cv2.destroyAllWindows()
    print("Check visually if program works correctly.")


# ----------------------------------------------------------------------------------------------------------------
# Question 5

def check_sepia():
    """Tests sepia"""
    print("Testing sepia...")
    print("----> Must check visually! <----")

    im1 = cv2.imread("SampleImages/landscape1.jpg")
    im2 = cv2.imread("SampleImages/chicago.jpg")
    im3 = cv2.imread("SampleImages/wildColumbine.jpg")
    im4 = cv2.imread("SampleImages/grandTetons.jpg")

    sep1 = hw2.sepia(im1)
    sep2 = hw2.sepia(im2)
    sep3 = hw2.sepia(im3)
    sep4 = hw2.sepia(im4)
    cv2.imshow("Sepia image 1", sep1)
    cv2.imshow("Sepia image 2", sep2)
    cv2.imshow("Sepia image 3", sep3)
    cv2.imshow("Sepia image 4", sep4)
    cv2.waitKey()
    cv2.destroyAllWindows()
    print("Check visually if sepia works correctly.")


# ==========================================================================================
# Main script, calls main function

runTests()
