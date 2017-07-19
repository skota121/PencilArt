import cv2
import sys
import os
import numpy as np 


#TODO: Request input from user
input_img = cv2.imread('practice.jpeg', 1)

# Convert color image to grayscale
input_image_gray = cv2.cvtColor(input_img, cv2.COLOR_RGB2GRAY)

# Take the negative of inputted image
input_img_negative = cv2.bitwise_not(input_image_gray)

# Gaussian Blur the image to smooth any edges

negative_input_blurred = cv2.GaussianBlur(input_img_negative, (5,5), 0)

cv2.imshow('Blurred Image', negative_input_blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
