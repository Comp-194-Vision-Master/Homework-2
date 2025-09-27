
import cv2

img = cv2.imread("SampleImages/landscape1.jpg")

h, w, d = img.shape

cropW = 1500
cropH = 1200

currx = 0
while currx + cropW < w:
    # print(currx, currx + cropW, w)
    visImg = img.copy()
    cv2.rectangle(visImg, (currx, 250), (currx+cropW, 250 + cropH), (255, 255, 255), 2)
    cv2.putText(visImg, str(currx), (currx, 220), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 2)
    cv2.putText(visImg, str(currx+cropW), (currx+cropW-75, 220), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 2)
    cv2.imshow("landscape", visImg)
    cv2.waitKey(5)
    currx += 1

cv2.waitKey()
