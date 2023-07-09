from ultralytics import YOLO
import cv2
import cvzone
# cvzone used to display all detections

img = cv2.imread('1.png')       # Read image using imread() of opencv

model = YOLO('../YOLOWeights/yolov8m.pt')  # Building a YOLO Object

results = model(img, stream=True)       # stream = True means it will use generators which is more efficient
ctr = 0         # counter
areas = 0
for r in results:
    boxes = r.boxes
    for box in boxes:       # bounding box
        ctr += 1
        x1, y1, x2, y2 = box.xyxy[0]   # returns top left and bottom right coordinates
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)     # convert in integer
        area = (x2 - x1) * (y2 - y1)                            # calculate area of bounding box
        cvzone.cornerRect(img, (x1, y1, (x2-x1), (y2-y1)), 30, 5, 1, (255, 0, 0), (0, 255, 0))      # create a bounding box
        cvzone.putTextRect(img, f'{ctr} {area}', (max(x1, 0), max(35, y1 - 10)), scale=1, thickness=1)      # display text on bbox
        areas += area

        print(f'{ctr} {area}')

cv2.imshow('Image', img)
cv2.waitKey(0)
print(f'Total number of objects are {ctr}')
print(f'Total area is {areas}')
