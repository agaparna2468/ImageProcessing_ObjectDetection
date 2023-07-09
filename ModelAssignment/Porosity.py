import cv2
import numpy as np

img = cv2.imread('Sample Image.jpg', cv2.IMREAD_GRAYSCALE)

retval, img_thresh = cv2.threshold(img, 60, 255, cv2.THRESH_BINARY)

x, y = img_thresh.shape
total_no = x*y
pores = total_no - np.count_nonzero(img_thresh == 255)
print(np.count_nonzero(img_thresh == 255))
print(total_no)
print(pores)
print(pores/total_no)

img_thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 7)

x, y = img_thresh.shape
total_no = x*y
pores = total_no - np.count_nonzero(img_thresh == 255)
print(np.count_nonzero(img_thresh == 255))
print(total_no)
print(pores)
print(pores/total_no)

