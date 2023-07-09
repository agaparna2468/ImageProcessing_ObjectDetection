from ultralytics import YOLO
import cv2

model = YOLO('../YOLOWeights/yolov8n.pt')              # yolo version 8 nano, this is a weight #.. means go back
# nano is faster than medium which is faster than large(l)
# File of large is bigger and we get better results

results = model('3.png', show=True)     # show says that we want to view the image

# First it will download the weights, running on GPU, speed and size
# Image opened and closed very quickly because of which we couldn't see it
cv2.waitKey(0)
# waitKey 0 says wait until a key is pressed
# Gives confidence level also, if confidence is close to 1 then better the prediction is
# Don't download for each package

# Closer it is to camera it detects well, farther from camera poor results
# Better to classify if clear image, confidence level is higher

# Having certain constraints like detect only cars or in a specific region, can mask regions, this will give better solutions

