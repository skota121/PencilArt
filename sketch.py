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

# Blended the edges using cv2's divide function

final_blend = cv2.divide(input_img_negative, negative_input_blurred, scale = 215)


cv2.imshow('Sketched Image', final_blend)
cv2.waitKey(0)
cv2.destroyAllWindows()
