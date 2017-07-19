import cv2
import sys
import os
import numpy as np 
from matplotlib import pyplot as plt
#TODO: Request input from user
input_img = cv2.imread('practice.jpeg', 0)
input_img = cv2.cvtColor(input_img, cv2.COLOR_RGB2GRAY)

# Take the negative of inputted image
input_img_negative = cv2.bitwise_not(input_img)

# Gaussian Blur the image to smooth any edges

negative_input_blurred = cv2.GuassianBlur(input_img_negative, (5,5), 0)

plt.imshow(negative_input_blurred)
plt.show()