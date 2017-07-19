import cv2
import sys
import os
import numpy as np 

#TODO: Request input from user
input_img = cv2.imread('practice.jpeg', 0)
input_img = cv2.cvtColor(input_img, cv2.COLOR_RGB2GRAY)

# Take the negative of inputted image
input_img_negative = cv2.bitwise_not(input_img)