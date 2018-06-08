#!usr/bin/python3

import cv2

print("okay")
im1=cv2.imread("tree.jpg")
im2=cv2.imread("dog.jpg")

i=cv2.addWeighted(im1,0.4,im2,0.6,0)

print (im1.shape)
print (im2.shape)
cv2.imshow("ad",i)
cv2.waitKey(0)
cv2.destroyAllWindows()
